# Lumix DeFi Agent Dialogue Platform 🤖💬

An intelligent dialogue platform for DeFi interactions, powered by DeepSeek R1 1.5B model. The system enables natural language conversations for Solana DeFi operations through Jupiter V6 Swap API and Chainstack RPC, combining AI-driven decision making with secure trading execution.

## Dialogue System Features

### Natural Language Trading
- Conversational interface for DeFi operations
- Context-aware trading suggestions
- Risk assessment through dialogue
- Multi-language support (English/中文)

### AI Agent Capabilities
- Market analysis through natural dialogue
- Position management conversations
- Strategy discussions and execution
- Real-time market insights

## System Requirements
- Python 3.12+
- Node.js 18+
- Linux/macOS (recommended)

## Environment Setup 环境设置

1. Clone the repository:
   ```bash
   git clone https://github.com/kwannz/lumixd.git
   cd lumixd
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Required package versions:
   - websockets==12.0
   - PyQt6==6.6.1
   - qt-material==2.14
   - darkdetect==0.8.0
   - fastapi>=0.110.0
   - uvicorn>=0.29.0
   - python-dotenv>=1.0.0
   - pymongo>=4.11.0
   - motor>=3.7.0
   - dnspython>=2.7.0
   - jupiter-py>=6.0.0
   - solders>=0.19.0
   - apscheduler>=3.10.4

3. Configure environment variables:
   ```bash
   cp .env.example .env
   ```
   Required variables:
   - `DEEPSEEK_API_KEY`: DeepSeek API key for NLP model
   - `CHAINSTACK_API_KEY`: Chainstack API key for RPC access
   - `RPC_ENDPOINT`: Chainstack RPC endpoint (https://solana-mainnet.core.chainstack.com/YOUR_KEY)
   - `CHAINSTACK_WS_ENDPOINT`: Chainstack WebSocket endpoint
   - `SOLANA_PRIVATE_KEY`: Your Solana wallet private key (base58 format)
     - Ensure wallet has sufficient SOL for transaction fees
     - Minimum recommended balance: 0.1 SOL

4. Setup MongoDB:
   ```bash
   # Install MongoDB Community Edition 7.0+
   sudo apt-get install mongodb-org

   # Start MongoDB service
   sudo systemctl start mongod

   # Initialize database and collections
   python scripts/setup_mongodb.py
   ```
   The system uses MongoDB for order tracking and position management.

## Running the System 运行系统

1. Verify environment setup 验证环境配置:
   ```bash
   # Check environment and dependencies 检查环境和依赖
   python scripts/verify_env.py
   python scripts/verify_deps.py
   
   # Verify MongoDB connection 验证MongoDB连接
   python scripts/setup_mongodb.py
   ```

2. Start the trading system 启动交易系统:
   ```bash
   # Set Python path and start FastAPI server 设置Python路径并启动FastAPI服务器
   PYTHONPATH=/path/to/lumixd uvicorn src.api.v1.main:app --host 0.0.0.0 --port 8000
   ```

3. Run test scenarios 运行测试场景:
   ```bash
   # Run dialog test 运行对话测试
   PYTHONPATH=/path/to/lumixd python test_dialog.py

   # Run trading scenarios 运行交易场景
   PYTHONPATH=/path/to/lumixd python test_trading_scenarios.py
   ```

4. Monitor system operation 监控系统运行:
   - Check MongoDB collections 检查MongoDB集合: `mongo lumixd`
   - View WebSocket status 查看WebSocket状态: `http://localhost:8000/api/v1/monitor/health`
   - Monitor order execution 监控订单执行: `http://localhost:8000/api/v1/monitor/orders`
   - Track system metrics 追踪系统指标: `http://localhost:8000/api/v1/monitor/metrics`

## Raydium Integration / Raydium集成

The system integrates with Raydium V3 API for enhanced liquidity and trading capabilities. / 系统集成了Raydium V3 API以提供增强的流动性和交易功能。

### Features / 功能
- Pool information retrieval / 池信息检索
- Token price queries / 代币价格查询
- AMM integration / AMM集成
- Comprehensive error handling / 全面的错误处理
- Bilingual support / 双语支持

### Configuration / 配置
```python
RAYDIUM_CONFIG = {
    "enabled": True,              # Enable/disable Raydium integration / 启用/禁用Raydium集成
    "base_url": "https://api-v3.raydium.io",  # Raydium API endpoint / Raydium API端点
    "retry_attempts": 3,          # Number of retry attempts / 重试次数
    "retry_delay": 1.0,          # Initial delay between retries (seconds) / 重试间隔（秒）
    "timeout": 30                 # Request timeout (seconds) / 请求超时（秒）
}
```

### Usage Examples / 使用示例
```python
async with RaydiumClient() as client:
    # Get pool information / 获取池信息
    pool_info = await client.get_pool_info(["pool_id"])
    
    # Get token price / 获取代币价格
    price = await client.get_token_price("token_mint_address")
    
    # Error handling example / 错误处理示例
    try:
        price = await client.get_token_price("invalid_address")
    except Exception as e:
        print(f"Error: {str(e)}")
```

## Trading Parameters 交易参数

### Default Settings 默认设置
- Default slippage 默认滑点: 2.5%
- Maximum position size 最大仓位: 20%
- Cash buffer 现金缓冲: 30%
- Stop loss 止损: -5%
- Rate limits RPC限制: 1 request per second

### Order Types 订单类型
1. Immediate Orders 即时订单
   - Full position buy 全仓买入
   - Partial position sell 部分仓位卖出
   - Market price execution 市价执行

2. Timed Orders 定时订单
   - Scheduled execution 定时执行
   - Delay in minutes 分钟延迟
   - Position size control 仓位控制

3. Conditional Orders 条件单
   - Price-based triggers 价格触发
   - Entry price tracking 入场价格追踪
   - Multiple conditions 多重条件

## Monitoring System 监控系统

1. Transaction Verification 交易验证
   - View transactions on Solscan 查看Solscan交易: https://solscan.io/account/4BKPzFyjBaRP3L1PNDf3xTerJmbbxxESmDmZJ2CZYdQ5
   - Check transaction status and fees 检查交易状态和费用
   - Verify Jupiter swaps execution 验证Jupiter交换执行

2. Order Tracking 订单追踪
   - MongoDB order status monitoring MongoDB订单状态监控
   - Real-time position updates 实时仓位更新
   - Order execution verification 订单执行验证
   - Historical order analysis 历史订单分析

3. Market Data 市场数据
   - Real-time price updates 实时价格更新
   - WebSocket market data streaming WebSocket市场数据流
   - Price trend analysis 价格趋势分析
   - Liquidity monitoring 流动性监控

4. System Health 系统健康
   - MongoDB connection status MongoDB连接状态
   - WebSocket connection health WebSocket连接健康
   - API rate limit monitoring API速率限制监控
   - Error tracking and alerts 错误追踪和警报

## Troubleshooting 故障排除

1. RPC Connection Issues:
   - Verify RPC_ENDPOINT in .env
   - Check Chainstack dashboard for rate limits
   - Ensure proper API authentication

2. Trading Errors:
   - Check SOL balance for transaction fees
   - Verify slippage settings
   - Monitor Jupiter API status

3. AI Model Issues:
   - Ensure Ollama server is running
   - Check DEEPSEEK_KEY configuration
   - Monitor model response times

## License
MIT License

## Multi-Instance Trading Support / 多实例交易支持

The system supports running multiple trading instances simultaneously, each with its own strategy, token pairs, and balance allocation. See [Multi-Instance Guide](docs/multi_instance_guide.md) for details.

Key features:
- Independent trading strategies per instance
- Isolated balance tracking
- Custom risk parameters
- Real-time performance monitoring
- Instance-specific metrics

## API Documentation / API文档

### Instance API / 实例API
- POST /api/v1/instances/create - Create trading instance / 创建交易实例
- GET /api/v1/instances/list - List all instances / 列出所有实例
- GET /api/v1/instances/{id} - Get instance details / 获取实例详情
- PUT /api/v1/instances/{id}/update - Update instance / 更新实例
- POST /api/v1/instances/{id}/toggle - Toggle instance / 切换实例状态
- GET /api/v1/instances/{id}/metrics - Get instance metrics / 获取实例指标
- GET /api/v1/instances/{id}/performance - Get instance performance / 获取实例性能

### Trading API / 交易API
- POST /api/v1/trades/execute - Execute trade / 执行交易
- GET /api/v1/trades/history - Get trade history / 获取交易历史
- GET /api/v1/trades/status - Get trading status / 获取交易状态

### Strategy API / 策略API
- POST /api/v1/strategies/create - Create custom strategy / 创建自定义策略
- GET /api/v1/strategies/list - List all strategies / 列出所有策略
- PUT /api/v1/strategies/{id}/update - Update strategy / 更新策略
- POST /api/v1/strategies/{id}/execute - Execute strategy / 执行策略

### Configuration API / 配置API
- GET /api/v1/config - Get system config / 获取系统配置
- PUT /api/v1/config/update - Update config / 更新配置

### Monitoring API / 监控API
- GET /api/v1/monitor/health - System health / 系统健康
- GET /api/v1/monitor/performance - Performance metrics / 性能指标
