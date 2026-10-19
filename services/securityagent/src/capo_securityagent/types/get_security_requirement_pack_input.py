"""Generated from Smithy shape ``com.amazonaws.securityagent#GetSecurityRequirementPackInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_pack_id


class GetSecurityRequirementPackInput(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the security requirement pack to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSecurityRequirementPackInput) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    return out


def deserialize_json(data: dict) -> GetSecurityRequirementPackInput:
    out: GetSecurityRequirementPackInput = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    return out
