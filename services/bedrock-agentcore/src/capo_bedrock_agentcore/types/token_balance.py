"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TokenBalance``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.blockchain_chain_id
    import capo_bedrock_agentcore.types.crypto_wallet_network
    import capo_bedrock_agentcore.types.instrument_balance_token


class TokenBalance(TypedDict, closed=True):
    amount: "str"
    """<p>Raw balance in the smallest denomination (e.g., USDC base units where 1 USDC = 1000000).</p>"""
    decimals: "int"
    """<p>Number of decimal places for the token (e.g., 6 for USDC).</p>"""
    token: (
        "capo_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken"
    )
    """<p>The supported token for this balance.</p>"""
    network: "capo_bedrock_agentcore.types.crypto_wallet_network.CryptoWalletNetwork"
    """<p>The blockchain network family (ETHEREUM or SOLANA).</p>"""
    chain: "capo_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId"
    """<p>The specific blockchain chain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenBalance) -> dict:
    out: dict = {}
    out["amount"] = value["amount"]
    out["decimals"] = value["decimals"]
    import capo_bedrock_agentcore.types.instrument_balance_token

    out["token"] = capo_bedrock_agentcore.types.instrument_balance_token.serialize_json(
        value["token"]
    )
    import capo_bedrock_agentcore.types.crypto_wallet_network

    out["network"] = capo_bedrock_agentcore.types.crypto_wallet_network.serialize_json(
        value["network"]
    )
    import capo_bedrock_agentcore.types.blockchain_chain_id

    out["chain"] = capo_bedrock_agentcore.types.blockchain_chain_id.serialize_json(
        value["chain"]
    )
    return out


def deserialize_json(data: dict) -> TokenBalance:
    out: TokenBalance = {}  # type: ignore[typeddict-item]
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    else:
        out["amount"] = ""
    if data.get("decimals") is not None:
        out["decimals"] = data["decimals"]
    else:
        out["decimals"] = 0
    if data.get("token") is not None:
        import capo_bedrock_agentcore.types.instrument_balance_token

        out["token"] = (
            capo_bedrock_agentcore.types.instrument_balance_token.deserialize_json(
                data["token"]
            )
        )
    else:
        import typing

        out["token"] = typing.cast(
            "capo_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken",
            "",
        )
    if data.get("network") is not None:
        import capo_bedrock_agentcore.types.crypto_wallet_network

        out["network"] = (
            capo_bedrock_agentcore.types.crypto_wallet_network.deserialize_json(
                data["network"]
            )
        )
    else:
        import typing

        out["network"] = typing.cast(
            "capo_bedrock_agentcore.types.crypto_wallet_network.CryptoWalletNetwork", ""
        )
    if data.get("chain") is not None:
        import capo_bedrock_agentcore.types.blockchain_chain_id

        out["chain"] = (
            capo_bedrock_agentcore.types.blockchain_chain_id.deserialize_json(
                data["chain"]
            )
        )
    else:
        import typing

        out["chain"] = typing.cast(
            "capo_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId", ""
        )
    return out
