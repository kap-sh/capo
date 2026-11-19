"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_id


class GetAgreementRequestInput(TypedDict, closed=True):
    agreement_request_id: (
        "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    )
    """<p>The unique identifier of the agreement request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementRequestInput) -> dict:
    out: dict = {}
    out["agreementRequestId"] = value["agreement_request_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementRequestInput:
    out: GetAgreementRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    else:
        out["agreement_request_id"] = ""
    return out
