"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RejectAgreementPaymentRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.payment_request_id
    import capo_marketplace_agreement.types.payment_request_rejection_reason


class RejectAgreementPaymentRequestInput(TypedDict, closed=True):
    payment_request_id: (
        "capo_marketplace_agreement.types.payment_request_id.PaymentRequestId"
    )
    """<p>The unique identifier of the payment request to reject.</p>"""
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the payment request.</p>"""
    rejection_reason: NotRequired[
        "capo_marketplace_agreement.types.payment_request_rejection_reason.PaymentRequestRejectionReason"
    ]
    """<p>An optional reason for rejecting the payment request (1-250 characters). This message is visible to the seller.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectAgreementPaymentRequestInput) -> dict:
    out: dict = {}
    out["paymentRequestId"] = value["payment_request_id"]
    out["agreementId"] = value["agreement_id"]
    if "rejection_reason" in value:
        out["rejectionReason"] = value["rejection_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectAgreementPaymentRequestInput:
    out: RejectAgreementPaymentRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("paymentRequestId") is not None:
        out["payment_request_id"] = data["paymentRequestId"]
    else:
        out["payment_request_id"] = ""
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    if data.get("rejectionReason") is not None:
        out["rejection_reason"] = data["rejectionReason"]
    return out
