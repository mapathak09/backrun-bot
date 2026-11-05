#!/usr/bin/env python3
"""
Back-Running Logic Helper
Defines how a back-run transaction is constructed.
"""

def build_backrun_transaction(target_tx_hash: str, gas_price: int, amount: float) -> dict:
    """Build back-run tx that follows the target immediately."""
    return {
        "to": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "from": "0x",
        "value": 0,
        "gas": 200000,
        "maxFeePerGas": int(gas_price * 1.1),
        "maxPriorityFeePerGas": int(gas_price * 1.05),
        "chainId": 1,
        "metadata": {
            "backrun_target": target_tx_hash,
            "backrun_type": "immediate_after_target",
            "expected_profit": amount * 0.01,
        },
    }
