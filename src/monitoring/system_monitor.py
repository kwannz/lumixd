import os
import psutil
from typing import Dict, Any, Optional
import time
from datetime import datetime
from typing import Dict, Any
from src.data.chainstack_client import ChainStackClient
from src.monitoring.performance_monitor import PerformanceMonitor

class SystemMonitor:
    def __init__(self, performance_monitor: PerformanceMonitor):
        self.client = ChainStackClient()
        self.performance_monitor = performance_monitor
        self.last_check = datetime.now()
        self.instance_metrics: Dict[str, Dict[str, Any]] = {}
        self.active_trades: Dict[str, List[Dict[str, Any]]] = {}
        
    def check_system_health(self) -> Dict[str, Any]:
        try:
            start_time = time.time()
            rpc_latency = int((time.time() - start_time) * 1000)
            
            metrics = {
                'cpu_usage': psutil.cpu_percent(),
                'memory_usage': psutil.virtual_memory().percent,
                'rpc_latency': rpc_latency,
                'active_instances': len(self.instance_metrics),
                'total_active_trades': sum(len(trades) for trades in self.active_trades.values()),
                'status': 'healthy'
            }
            
            self.performance_monitor.log_system_health(metrics)
            return metrics
            
    def check_instance_health(self, instance_id: str) -> Dict[str, Any]:
        try:
            wallet_address = os.getenv("WALLET_ADDRESS")
            if not wallet_address:
                return {'status': 'error', 'message': 'Wallet address not set'}
                
            wallet_balance = self.client.get_wallet_balance(wallet_address)
            active_trades = self.active_trades.get(instance_id, [])
            
            metrics = {
                'instance_id': instance_id,
                'wallet_balance': wallet_balance,
                'active_trades': len(active_trades),
                'last_trade_time': self.instance_metrics.get(instance_id, {}).get('last_trade_time'),
                'cpu_usage': psutil.cpu_percent(),
                'memory_usage': psutil.virtual_memory().percent,
                'status': 'healthy'
            }
            
            self.instance_metrics[instance_id] = metrics
            return metrics
        except Exception as e:
            self.performance_monitor.logger.error(f"System health check failed: {str(e)}")
            return {
                'status': 'unhealthy',
                'error': str(e)
            }
            
    def monitor_trading_interval(self, instance_id: str, token: str, last_trade_time: datetime):
        current_time = datetime.now()
        interval_seconds = int((current_time - last_trade_time).total_seconds())
        self.performance_monitor.log_trading_interval(token, interval_seconds)
        
        if instance_id in self.instance_metrics:
            self.instance_metrics[instance_id]['last_trade_time'] = current_time
        self.last_check = current_time
        
    def track_trade(self, instance_id: str, trade_data: Dict[str, Any]) -> None:
        if instance_id not in self.active_trades:
            self.active_trades[instance_id] = []
            
        self.active_trades[instance_id].append({
            'token': trade_data['token'],
            'direction': trade_data['direction'],
            'amount': trade_data['amount'],
            'start_time': datetime.now(),
            'status': 'active'
        })
        
    def complete_trade(self, instance_id: str, token: str, success: bool) -> None:
        if instance_id in self.active_trades:
            trades = self.active_trades[instance_id]
            for trade in trades:
                if trade['token'] == token and trade['status'] == 'active':
                    trade['status'] = 'completed' if success else 'failed'
                    trade['end_time'] = datetime.now()
                    break
                    
            # Clean up completed trades
            self.active_trades[instance_id] = [
                t for t in trades if t['status'] == 'active'
            ]
