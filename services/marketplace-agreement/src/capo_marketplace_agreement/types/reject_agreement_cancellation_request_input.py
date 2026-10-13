"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RejectAgreementCancellationRequestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_cancellation_request_id
    import capo_marketplace_agreement.types.agreement_cancellation_request_rejection_reason
    import capo_marketplace_agreement.types.agreement_id


class RejectAgreementCancellationRequestInput(TypedDict, closed=True):
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the cancellation request.</p>"""
    agreement_cancellation_request_id: "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    """<p>The unique identifier of the cancellation request to reject.</p>"""
    rejection_reason: "capo_marketplace_agreement.types.agreement_cancellation_request_rejection_reason.AgreementCancellationRequestRejectionReason"
    """<p>The reason for rejecting the cancellation request (1-2000 characters). This message is visible to the seller.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectAgreementCancellationRequestInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    out["agreementCancellationRequestId"] = value["agreement_cancellation_request_id"]
    out["rejectionReason"] = value["rejection_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectAgreementCancellationRequestInput:
    out: RejectAgreementCancellationRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "RejectAgreementCancellationRequestInput.agreement_id required"
        )
    if data.get("agreementCancellationRequestId") is not None:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    else:
        raise DeserializationError(
            "RejectAgreementCancellationRequestInput.agreement_cancellation_request_id required"
        )
    if data.get("rejectionReason") is not None:
        out["rejection_reason"] = data["rejectionReason"]
    else:
        raise DeserializationError(
            "RejectAgreementCancellationRequestInput.rejection_reason required"
        )
    return out


def redact_sensitive(value: RejectAgreementCancellationRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rejection_reason" in value:
        out["rejection_reason"] = "*** Sensitive Data Redacted ***"
    return out
