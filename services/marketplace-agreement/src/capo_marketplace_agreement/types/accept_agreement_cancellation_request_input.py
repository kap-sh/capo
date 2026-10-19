"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptAgreementCancellationRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_cancellation_request_id
    import capo_marketplace_agreement.types.agreement_id


class AcceptAgreementCancellationRequestInput(TypedDict, closed=True):
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the cancellation request.</p>"""
    agreement_cancellation_request_id: "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    """<p>The unique identifier of the cancellation request to accept.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAgreementCancellationRequestInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    out["agreementCancellationRequestId"] = value["agreement_cancellation_request_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptAgreementCancellationRequestInput:
    out: AcceptAgreementCancellationRequestInput = {}  # type: ignore[typeddict-item]
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
    return out
