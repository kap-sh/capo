"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CancelAgreementCancellationRequestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_cancellation_request_cancellation_reason
    import capo_marketplace_agreement.types.agreement_cancellation_request_id
    import capo_marketplace_agreement.types.agreement_id


class CancelAgreementCancellationRequestInput(TypedDict, closed=True):
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the cancellation request.</p>"""
    agreement_cancellation_request_id: "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    """<p>The unique identifier of the cancellation request to cancel.</p>"""
    cancellation_reason: "capo_marketplace_agreement.types.agreement_cancellation_request_cancellation_reason.AgreementCancellationRequestCancellationReason"
    """<p>A required message explaining why the cancellation request is being withdrawn (1-2000 characters).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelAgreementCancellationRequestInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    out["agreementCancellationRequestId"] = value["agreement_cancellation_request_id"]
    out["cancellationReason"] = value["cancellation_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelAgreementCancellationRequestInput:
    out: CancelAgreementCancellationRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    if data.get("agreementCancellationRequestId") is not None:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    else:
        out["agreement_cancellation_request_id"] = ""
    if data.get("cancellationReason") is not None:
        out["cancellation_reason"] = data["cancellationReason"]
    else:
        out["cancellation_reason"] = ""
    return out


def redact_sensitive(value: CancelAgreementCancellationRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cancellation_reason" in value:
        out["cancellation_reason"] = "*** Sensitive Data Redacted ***"
    return out
