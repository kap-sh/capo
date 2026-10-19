"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.billing_adjustment_request_id
    import capo_marketplace_agreement.types.client_token


class BatchCreateBillingAdjustmentItem(TypedDict, closed=True):
    billing_adjustment_request_id: "capo_marketplace_agreement.types.billing_adjustment_request_id.BillingAdjustmentRequestId"
    """<p>The unique identifier of the created billing adjustment request.</p>"""
    client_token: "capo_marketplace_agreement.types.client_token.ClientToken"
    """<p>The client token provided in the corresponding request entry.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentItem) -> dict:
    out: dict = {}
    out["billingAdjustmentRequestId"] = value["billing_adjustment_request_id"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillingAdjustmentItem:
    out: BatchCreateBillingAdjustmentItem = {}  # type: ignore[typeddict-item]
    if data.get("billingAdjustmentRequestId") is not None:
        out["billing_adjustment_request_id"] = data["billingAdjustmentRequestId"]
    else:
        out["billing_adjustment_request_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    return out
