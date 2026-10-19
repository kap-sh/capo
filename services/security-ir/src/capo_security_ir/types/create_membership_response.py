"""Generated from Smithy shape ``com.amazonaws.securityir#CreateMembershipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.membership_id


class CreateMembershipResponse(TypedDict, closed=True):
    membership_id: "capo_security_ir.types.membership_id.MembershipId"
    """<p>Response element for CreateMembership providing the newly created membership ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembershipResponse) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    return out


def deserialize_json(data: dict) -> CreateMembershipResponse:
    out: CreateMembershipResponse = {}  # type: ignore[typeddict-item]
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    return out
