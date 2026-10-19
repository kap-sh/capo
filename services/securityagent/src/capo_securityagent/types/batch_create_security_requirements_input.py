"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchCreateSecurityRequirementsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.create_security_requirement_entry_list
    import capo_securityagent.types.security_requirement_pack_id


class BatchCreateSecurityRequirementsInput(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the security requirement pack to add requirements to.</p>"""
    security_requirements: "capo_securityagent.types.create_security_requirement_entry_list.CreateSecurityRequirementEntryList"
    """<p>The list of security requirements to create.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateSecurityRequirementsInput) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    import capo_securityagent.types.create_security_requirement_entry_list

    out["securityRequirements"] = (
        capo_securityagent.types.create_security_requirement_entry_list.serialize_json(
            value["security_requirements"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateSecurityRequirementsInput:
    out: BatchCreateSecurityRequirementsInput = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    if data.get("securityRequirements") is not None:
        import capo_securityagent.types.create_security_requirement_entry_list

        out["security_requirements"] = (
            capo_securityagent.types.create_security_requirement_entry_list.deserialize_json(
                data["securityRequirements"]
            )
        )
    else:
        out["security_requirements"] = []
    return out
