# Back-Running MEV Bot

A Python-based **Back-Running** MEV bot that listens to the Ethereum mempool, detects target transactions (e.g., large buys, liquidity additions), and submits its own transaction immediately after the target to capitalize on the price movement.

## How Back-Running Works

1. **Mempool Monitoring** — The bot subscribes to pending transactions via WebSocket.
2. **Target Detection** — When a transaction matches a target pattern (e.g., large buy on a specific token), it's flagged.
3. **Back-Run Execution** — The bot submits its own transaction with a slightly higher gas fee to be included in the same block immediately after the target.
4. **Profit Realization** — The bot sells the position later for a profit.

## Features

- Real-time mempool monitoring via WebSocket
- Configurable target patterns (token addresses, thresholds)
- MEV-resistant transaction submission (Flashbots Protect or private RPC)
- Profit/loss tracking and metrics
- Dockerized deployment

## Requirements

- Python 3.10+
- Ethereum node with WebSocket access (e.g., Alchemy, Infura, or self-hosted)
- Private key with ETH for gas fees

## Quick Start

```bash
cp .env.example .env
# Edit .env with your configuration
docker compose up -d
```

Or run locally:

```bash
pip install -e .
python src/main.py
```

## Configuration

See `config/settings.py` and `config/targets.json` for all options.

## License

MIT
