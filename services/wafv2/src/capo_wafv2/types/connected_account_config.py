"""Generated from Smithy shape ``com.amazonaws.wafv2#ConnectedAccountConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.connected_account_arn
    import capo_wafv2.types.connected_account_payment_networks


class ConnectedAccountConfig(TypedDict, closed=True):
    connected_account_arn: "capo_wafv2.types.connected_account_arn.ConnectedAccountArn"
    """<p>The Amazon Resource Name (ARN) of the connected account that payments settle to. You obtain this ARN from Payment preferences > Connected accounts in the Amazon Web Services Billing and Cost Management console. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-connected-accounts.html">Managing connected accounts</a>. The connected account must be active and enabled for crypto settlement; otherwise the request is rejected. To use a connected account, you must have the <code>payments:GetConnectedAccount</code> permission on this ARN.</p>"""
    payment_networks: "capo_wafv2.types.connected_account_payment_networks.ConnectedAccountPaymentNetworks"
    """<p>The per-network configurations for the connected account. You can specify 1 to 2 networks. Each entry specifies a blockchain network and the price for each request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedAccountConfig) -> dict:
    out: dict = {}
    out["ConnectedAccountArn"] = value["connected_account_arn"]
    import capo_wafv2.types.connected_account_payment_networks

    out["PaymentNetworks"] = (
        capo_wafv2.types.connected_account_payment_networks.serialize_aws_json_1_1(
            value["payment_networks"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectedAccountConfig:
    out: ConnectedAccountConfig = {}  # type: ignore[typeddict-item]
    if data.get("ConnectedAccountArn") is not None:
        out["connected_account_arn"] = data["ConnectedAccountArn"]
    else:
        out["connected_account_arn"] = ""
    if data.get("PaymentNetworks") is not None:
        import capo_wafv2.types.connected_account_payment_networks

        out["payment_networks"] = (
            capo_wafv2.types.connected_account_payment_networks.deserialize_aws_json_1_1(
                data["PaymentNetworks"]
            )
        )
    else:
        out["payment_networks"] = []
    return out
