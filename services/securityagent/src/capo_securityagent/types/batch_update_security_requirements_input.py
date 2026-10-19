"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchUpdateSecurityRequirementsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_pack_id
    import capo_securityagent.types.update_security_requirement_entry_list


class BatchUpdateSecurityRequirementsInput(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the security requirement pack containing the requirements to update.</p>"""
    security_requirements: "capo_securityagent.types.update_security_requirement_entry_list.UpdateSecurityRequirementEntryList"
    """<p>The list of security requirement updates to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateSecurityRequirementsInput) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    import capo_securityagent.types.update_security_requirement_entry_list

    out["securityRequirements"] = (
        capo_securityagent.types.update_security_requirement_entry_list.serialize_json(
            value["security_requirements"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateSecurityRequirementsInput:
    out: BatchUpdateSecurityRequirementsInput = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    if data.get("securityRequirements") is not None:
        import capo_securityagent.types.update_security_requirement_entry_list

        out["security_requirements"] = (
            capo_securityagent.types.update_security_requirement_entry_list.deserialize_json(
                data["securityRequirements"]
            )
        )
    else:
        out["security_requirements"] = []
    return out
