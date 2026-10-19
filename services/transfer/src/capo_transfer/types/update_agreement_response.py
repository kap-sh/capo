"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateAgreementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.agreement_id


class UpdateAgreementResponse(TypedDict, closed=True):
    agreement_id: "capo_transfer.types.agreement_id.AgreementId"
    """<p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAgreementResponse) -> dict:
    out: dict = {}
    out["AgreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAgreementResponse:
    out: UpdateAgreementResponse = {}  # type: ignore[typeddict-item]
    if data.get("AgreementId") is not None:
        out["agreement_id"] = data["AgreementId"]
    else:
        out["agreement_id"] = ""
    return out
