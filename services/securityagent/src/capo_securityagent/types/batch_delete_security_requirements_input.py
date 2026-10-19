"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchDeleteSecurityRequirementsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_name_list
    import capo_securityagent.types.security_requirement_pack_id


class BatchDeleteSecurityRequirementsInput(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the security requirement pack to remove requirements from.</p>"""
    security_requirement_names: "capo_securityagent.types.security_requirement_name_list.SecurityRequirementNameList"
    """<p>The list of security requirement names to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteSecurityRequirementsInput) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    import capo_securityagent.types.security_requirement_name_list

    out["securityRequirementNames"] = (
        capo_securityagent.types.security_requirement_name_list.serialize_json(
            value["security_requirement_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteSecurityRequirementsInput:
    out: BatchDeleteSecurityRequirementsInput = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    if data.get("securityRequirementNames") is not None:
        import capo_securityagent.types.security_requirement_name_list

        out["security_requirement_names"] = (
            capo_securityagent.types.security_requirement_name_list.deserialize_json(
                data["securityRequirementNames"]
            )
        )
    else:
        out["security_requirement_names"] = []
    return out
