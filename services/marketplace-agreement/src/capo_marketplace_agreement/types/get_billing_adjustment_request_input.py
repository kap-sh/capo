"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetBillingAdjustmentRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.billing_adjustment_request_id


class GetBillingAdjustmentRequestInput(TypedDict, closed=True):
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the billing adjustment request.</p>"""
    billing_adjustment_request_id: "capo_marketplace_agreement.types.billing_adjustment_request_id.BillingAdjustmentRequestId"
    """<p>The unique identifier of the billing adjustment request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillingAdjustmentRequestInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    out["billingAdjustmentRequestId"] = value["billing_adjustment_request_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillingAdjustmentRequestInput:
    out: GetBillingAdjustmentRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    if data.get("billingAdjustmentRequestId") is not None:
        out["billing_adjustment_request_id"] = data["billingAdjustmentRequestId"]
    else:
        out["billing_adjustment_request_id"] = ""
    return out
