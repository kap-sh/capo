"""Generated from Smithy shape ``com.amazonaws.b2bi#DeletePartnershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.partnership_id


class DeletePartnershipRequest(TypedDict, closed=True):
    partnership_id: "capo_b2bi.types.partnership_id.PartnershipId"
    """<p>Specifies the unique, system-generated identifier for a partnership.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePartnershipRequest) -> dict:
    out: dict = {}
    out["partnershipId"] = value["partnership_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePartnershipRequest:
    out: DeletePartnershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("partnershipId") is not None:
        out["partnership_id"] = data["partnershipId"]
    else:
        out["partnership_id"] = ""
    return out
