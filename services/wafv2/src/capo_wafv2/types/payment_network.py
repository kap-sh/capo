"""Generated from Smithy shape ``com.amazonaws.wafv2#PaymentNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.blockchain_chain
    import capo_wafv2.types.prices
    import capo_wafv2.types.wallet_address


class PaymentNetwork(TypedDict, closed=True):
    chain: "capo_wafv2.types.blockchain_chain.BlockchainChain"
    """<p>The blockchain network for receiving payments. Production networks: <code>BASE</code> (Base mainnet), <code>SOLANA</code> (Solana mainnet). Test networks: <code>BASE_SEPOLIA</code> (Base Sepolia testnet), <code>SOLANA_DEVNET</code> (Solana Devnet).</p>"""
    wallet_address: "capo_wafv2.types.wallet_address.WalletAddress"
    """<p>Your wallet address on the specified blockchain where payments are sent. For EVM chains (Base, Base Sepolia), provide a valid Ethereum address (42 characters including 0x prefix). For Solana chains, provide a valid Base58-encoded public key (32-44 characters).</p> <p>For EVM addresses, WAF performs EIP-55 checksum validation for typo detection when the address uses a mix of lower and upper case letters. You can bypass this validation by providing the address in all lowercase or all uppercase.</p>"""
    prices: "capo_wafv2.types.prices.Prices"
    """<p>The price configuration for this payment network. Currently supports a single price entry in USDC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PaymentNetwork) -> dict:
    out: dict = {}
    import capo_wafv2.types.blockchain_chain

    out["Chain"] = capo_wafv2.types.blockchain_chain.serialize_aws_json_1_1(
        value["chain"]
    )
    out["WalletAddress"] = value["wallet_address"]
    import capo_wafv2.types.prices

    out["Prices"] = capo_wafv2.types.prices.serialize_aws_json_1_1(value["prices"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PaymentNetwork:
    out: PaymentNetwork = {}  # type: ignore[typeddict-item]
    if data.get("Chain") is not None:
        import capo_wafv2.types.blockchain_chain

        out["chain"] = capo_wafv2.types.blockchain_chain.deserialize_aws_json_1_1(
            data["Chain"]
        )
    else:
        import typing

        out["chain"] = typing.cast(
            "capo_wafv2.types.blockchain_chain.BlockchainChain", ""
        )
    if data.get("WalletAddress") is not None:
        out["wallet_address"] = data["WalletAddress"]
    else:
        out["wallet_address"] = ""
    if data.get("Prices") is not None:
        import capo_wafv2.types.prices

        out["prices"] = capo_wafv2.types.prices.deserialize_aws_json_1_1(data["Prices"])
    else:
        out["prices"] = []
    return out
