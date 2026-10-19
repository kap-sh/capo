"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementPaymentRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.payment_request_id


class GetAgreementPaymentRequestInput(TypedDict, closed=True):
    payment_request_id: (
        "capo_marketplace_agreement.types.payment_request_id.PaymentRequestId"
    )
    """<p>The identifier of the payment request.</p>"""
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the payment request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementPaymentRequestInput) -> dict:
    out: dict = {}
    out["paymentRequestId"] = value["payment_request_id"]
    out["agreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementPaymentRequestInput:
    out: GetAgreementPaymentRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("paymentRequestId") is not None:
        out["payment_request_id"] = data["paymentRequestId"]
    else:
        out["payment_request_id"] = ""
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    return out
