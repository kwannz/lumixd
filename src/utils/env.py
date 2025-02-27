import os
from typing import List, Optional
from pathlib import Path
from dotenv import load_dotenv

def load_environment() -> bool:
    """Load environment variables from .env file"""
    env_path = Path(".env")
    if not env_path.exists():
        return False
    load_dotenv(env_path)
    return True

def verify_environment(required_vars: List[str]) -> Optional[str]:
    """Verify all required environment variables are set"""
    for var in required_vars:
        if not os.getenv(var):
            return f"Missing required environment variable: {var}"
    return None

def get_env_var(var_name: str) -> str:
    """Get environment variable with error handling"""
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"Environment variable {var_name} not set")
    return value
