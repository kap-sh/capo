"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchDeleteSecurityRequirementsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.batch_security_requirement_errors
    import capo_securityagent.types.security_requirement_name_list


class BatchDeleteSecurityRequirementsOutput(TypedDict, closed=True):
    deleted_security_requirement_names: "capo_securityagent.types.security_requirement_name_list.SecurityRequirementNameList"
    """<p>The list of security requirement names that were successfully deleted.</p>"""
    errors: "capo_securityagent.types.batch_security_requirement_errors.BatchSecurityRequirementErrors"
    """<p>The list of errors for security requirements that failed to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteSecurityRequirementsOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.security_requirement_name_list

    out["deletedSecurityRequirementNames"] = (
        capo_securityagent.types.security_requirement_name_list.serialize_json(
            value["deleted_security_requirement_names"]
        )
    )
    import capo_securityagent.types.batch_security_requirement_errors

    out["errors"] = (
        capo_securityagent.types.batch_security_requirement_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteSecurityRequirementsOutput:
    out: BatchDeleteSecurityRequirementsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deletedSecurityRequirementNames") is not None:
        import capo_securityagent.types.security_requirement_name_list

        out["deleted_security_requirement_names"] = (
            capo_securityagent.types.security_requirement_name_list.deserialize_json(
                data["deletedSecurityRequirementNames"]
            )
        )
    else:
        out["deleted_security_requirement_names"] = []
    if data.get("errors") is not None:
        import capo_securityagent.types.batch_security_requirement_errors

        out["errors"] = (
            capo_securityagent.types.batch_security_requirement_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
