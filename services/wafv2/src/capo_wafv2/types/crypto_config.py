"""Generated from Smithy shape ``com.amazonaws.wafv2#CryptoConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.payment_networks


class CryptoConfig(TypedDict, closed=True):
    payment_networks: "capo_wafv2.types.payment_networks.PaymentNetworks"
    """<p>The blockchain payment networks configured to receive payments. You can specify 1 to 2 networks. All networks must be in the same environment-either all production networks (Base, Solana) or all test networks (Base Sepolia, Solana Devnet).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CryptoConfig) -> dict:
    out: dict = {}
    import capo_wafv2.types.payment_networks

    out["PaymentNetworks"] = capo_wafv2.types.payment_networks.serialize_aws_json_1_1(
        value["payment_networks"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CryptoConfig:
    out: CryptoConfig = {}  # type: ignore[typeddict-item]
    if data.get("PaymentNetworks") is not None:
        import capo_wafv2.types.payment_networks

        out["payment_networks"] = (
            capo_wafv2.types.payment_networks.deserialize_aws_json_1_1(
                data["PaymentNetworks"]
            )
        )
    else:
        out["payment_networks"] = []
    return out
