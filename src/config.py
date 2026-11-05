"""
Production-grade configuration using Pydantic.
All settings are validated at startup.
"""
import os
from typing import List, Optional
from pydantic import BaseModel, Field, validator


class NetworkConfig(BaseModel):
    """Network and RPC configuration."""
    eth_node_url: str = Field(..., description="WebSocket Ethereum node URL")
    chain_id: int = Field(default=1, description="Chain ID (1=Ethereum, 11155111=Sepolia)")
    flashbots_endpoint: Optional[str] = Field(None, description="Flashbots relay endpoint")
    use_flashbots: bool = Field(default=False, description="Use Flashbots for submission")

    @validator("eth_node_url")
    def validate_node_url(cls, v):
        if not v or v == "wss://":
            raise ValueError("ETH_NODE_URL must be configured")
        return v


class TradingConfig(BaseModel):
    """Trading and backrun configuration."""
    private_key: str = Field(..., description="Private key for signing transactions")
    target_liquidity_min_usd: int = Field(default=50_000, description="Minimum liquidity in USD")
    target_trade_size_min_eth: float = Field(default=0.1, description="Minimum ETH trade size")
    max_gas_gwei: float = Field(default=5.0, description="Maximum gas price in GWEI")
    gas_multiplier: float = Field(default=1.1, description="Gas multiplier vs target")
    backrun_slippage: float = Field(default=0.01, description="Slippage tolerance")
    dry_run: bool = Field(default=True, description="Simulation mode only")
    min_profit_threshold_usd: float = Field(default=0.01, description="Minimum profit threshold")
    max_backruns_per_minute: int = Field(default=10, description="Rate limit backruns")

    @validator("private_key")
    def validate_private_key(cls, v):
        if not v or v == "YOUR_PRIVATE_KEY":
            raise ValueError("PRIVATE_KEY must be configured")
        return v


class SafetyConfig(BaseModel):
    """Safety and risk management configuration."""
    exclude_honeypot: bool = Field(default=True, description="Check honeypot via DexScreener")
    exclude_high_tax: bool = Field(default=True, description="Check token tax rates")
    exclude_age_hours: int = Field(default=24, description="Minimum token age in hours")
    enable_rate_limiting: bool = Field(default=True, description="Enable rate limiting")
    consecutive_failure_limit: int = Field(default=5, description="Consecutive failures before pause")


class Settings(BaseModel):
    """Complete application settings."""
    network: NetworkConfig
    trading: TradingConfig
    safety: SafetyConfig
    environment: str = Field(default="production", description="deployment environment")
    log_level: str = Field(default="INFO", description="Logging level")

    @classmethod
    def from_env(cls):
        """Load settings from environment variables."""
        return cls(
            network=NetworkConfig(
                eth_node_url=os.getenv("ETH_NODE_URL", ""),
                chain_id=int(os.getenv("CHAIN_ID", "1")),
                flashbots_endpoint=os.getenv("FLASHBOTS_ENDPOINT", ""),
                use_flashbots=os.getenv("USE_FLASHBOTS", "false").lower() == "true",
            ),
            trading=TradingConfig(
                private_key=os.getenv("PRIVATE_KEY", ""),
                target_liquidity_min_usd=int(os.getenv("TARGET_LIQUIDITY_MIN_USD", "50000")),
                target_trade_size_min_eth=float(os.getenv("TARGET_TRADE_SIZE_MIN_ETH", "0.1")),
                max_gas_gwei=float(os.getenv("MAX_GAS_GWEI", "5")),
                gas_multiplier=float(os.getenv("GAS_MULTIPLIER", "1.1")),
                backrun_slippage=float(os.getenv("BACKRUN_SLIPPAGE", "0.01")),
                dry_run=os.getenv("DRY_RUN", "true").lower() == "true",
                min_profit_threshold_usd=float(os.getenv("MIN_PROFIT_THRESHOLD_USD", "0.01")),
                max_backruns_per_minute=int(os.getenv("MAX_BACKRUNS_PER_MINUTE", "10")),
            ),
            safety=SafetyConfig(
                exclude_honeypot=os.getenv("EXCLUDE_HONEYPOT", "true").lower() == "true",
                exclude_high_tax=os.getenv("EXCLUDE_HIGH_TAX", "true").lower() == "true",
                exclude_age_hours=int(os.getenv("EXCLUDE_AGE_HOURS", "24")),
                enable_rate_limiting=os.getenv("ENABLE_RATE_LIMITING", "true").lower() == "true",
                consecutive_failure_limit=int(os.getenv("CONSECUTIVE_FAILURE_LIMIT", "5")),
            ),
            environment=os.getenv("ENVIRONMENT", "production"),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )
