"""Generated from Smithy shape ``com.amazonaws.wafv2#ConnectedAccountChainConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.connected_account_chain
    import capo_wafv2.types.connected_account_prices


class ConnectedAccountChainConfig(TypedDict, closed=True):
    chain: "capo_wafv2.types.connected_account_chain.ConnectedAccountChain"
    """<p>The blockchain network for receiving payments through the connected account. Test networks are not supported for connected accounts.</p> <p>Valid values:</p> <ul> <li> <p> <code>BASE</code> - Base mainnet.</p> </li> <li> <p> <code>SOLANA</code> - Solana mainnet.</p> </li> </ul>"""
    prices: "capo_wafv2.types.connected_account_prices.ConnectedAccountPrices"
    """<p>The price configuration for this network. Currently supports a single price entry in USDC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedAccountChainConfig) -> dict:
    out: dict = {}
    import capo_wafv2.types.connected_account_chain

    out["Chain"] = capo_wafv2.types.connected_account_chain.serialize_aws_json_1_1(
        value["chain"]
    )
    import capo_wafv2.types.connected_account_prices

    out["Prices"] = capo_wafv2.types.connected_account_prices.serialize_aws_json_1_1(
        value["prices"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectedAccountChainConfig:
    out: ConnectedAccountChainConfig = {}  # type: ignore[typeddict-item]
    if data.get("Chain") is not None:
        import capo_wafv2.types.connected_account_chain

        out["chain"] = (
            capo_wafv2.types.connected_account_chain.deserialize_aws_json_1_1(
                data["Chain"]
            )
        )
    else:
        import typing

        out["chain"] = typing.cast(
            "capo_wafv2.types.connected_account_chain.ConnectedAccountChain", ""
        )
    if data.get("Prices") is not None:
        import capo_wafv2.types.connected_account_prices

        out["prices"] = (
            capo_wafv2.types.connected_account_prices.deserialize_aws_json_1_1(
                data["Prices"]
            )
        )
    else:
        out["prices"] = []
    return out
