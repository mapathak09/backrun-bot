import os

# Network configuration
ETH_NODE_URL = os.getenv("ETH_NODE_URL", "wss://eth-mainnet.alchemyapi.io/v2/YOUR_API_KEY")
PRIVATE_KEY = os.getenv("PRIVATE_KEY", "YOUR_PRIVATE_KEY")

# Back-run configuration
TARGET_TOKEN_ADDRESS = os.getenv("TARGET_TOKEN_ADDRESS", "0x0000000000000000000000000000000000000000")
TARGET_AMOUNT_THRESHOLD = float(os.getenv("TARGET_AMOUNT_THRESHOLD", "1000"))  # ETH value threshold
BACKRUN_SLIPPAGE = float(os.getenv("BACKRUN_SLIPPAGE", "0.01"))  # 1% slippage tolerance
GAS_MULTIPLIER = float(os.getenv("GAS_MULTIPLIER", "1.1"))  # 10% higher gas than target

# MEV submission
USE_FLASHBOTS = os.getenv("USE_FLASHBOTS", "true").lower() == "true"
MEV_ENDPOINT = os.getenv("MEV_ENDPOINT", "https://mev.blockfusion.net")

# Monitoring intervals
MEMPOOL_POLLING_INTERVAL = int(os.getenv("MEMPOOL_POLLING_INTERVAL", "5"))
TARGET_RECHECK_INTERVAL = int(os.getenv("TARGET_RECHECK_INTERVAL", "30"))

# Profit tracking
MIN_PROFIT_THRESHOLD = float(os.getenv("MIN_PROFIT_THRESHOLD", "10.0"))  # Minimum profit in USD
