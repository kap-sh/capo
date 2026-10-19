"""Generated from Smithy shape ``com.amazonaws.transfer#CreateAgreementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.agreement_id


class CreateAgreementResponse(TypedDict, closed=True):
    agreement_id: "capo_transfer.types.agreement_id.AgreementId"
    """<p>The unique identifier for the agreement. Use this ID for deleting, or updating an agreement, as well as in any other API calls that require that you specify the agreement ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAgreementResponse) -> dict:
    out: dict = {}
    out["AgreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAgreementResponse:
    out: CreateAgreementResponse = {}  # type: ignore[typeddict-item]
    if data.get("AgreementId") is not None:
        out["agreement_id"] = data["AgreementId"]
    else:
        out["agreement_id"] = ""
    return out
