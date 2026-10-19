"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateSecurityRequirementPackInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_pack_id
    import capo_securityagent.types.security_requirement_pack_name
    import capo_securityagent.types.security_requirement_pack_status


class UpdateSecurityRequirementPackInput(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the security requirement pack to update.</p>"""
    name: NotRequired[
        "capo_securityagent.types.security_requirement_pack_name.SecurityRequirementPackName"
    ]
    """<p>The updated name of the security requirement pack.</p>"""
    description: NotRequired["str"]
    """<p>The updated description of the security requirement pack.</p>"""
    status: NotRequired[
        "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
    ]
    """<p>The updated status of the security requirement pack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityRequirementPackInput) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_securityagent.types.security_requirement_pack_status

        out["status"] = (
            capo_securityagent.types.security_requirement_pack_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSecurityRequirementPackInput:
    out: UpdateSecurityRequirementPackInput = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_securityagent.types.security_requirement_pack_status

        out["status"] = (
            capo_securityagent.types.security_requirement_pack_status.deserialize_json(
                data["status"]
            )
        )
    return out
