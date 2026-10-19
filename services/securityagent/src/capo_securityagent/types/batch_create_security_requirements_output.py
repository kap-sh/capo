"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchCreateSecurityRequirementsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.batch_create_security_requirement_result_list
    import capo_securityagent.types.batch_security_requirement_errors


class BatchCreateSecurityRequirementsOutput(TypedDict, closed=True):
    security_requirements: "capo_securityagent.types.batch_create_security_requirement_result_list.BatchCreateSecurityRequirementResultList"
    """<p>The list of security requirements that were successfully created.</p>"""
    errors: "capo_securityagent.types.batch_security_requirement_errors.BatchSecurityRequirementErrors"
    """<p>The list of errors for security requirements that failed to be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateSecurityRequirementsOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.batch_create_security_requirement_result_list

    out["securityRequirements"] = (
        capo_securityagent.types.batch_create_security_requirement_result_list.serialize_json(
            value["security_requirements"]
        )
    )
    import capo_securityagent.types.batch_security_requirement_errors

    out["errors"] = (
        capo_securityagent.types.batch_security_requirement_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateSecurityRequirementsOutput:
    out: BatchCreateSecurityRequirementsOutput = {}  # type: ignore[typeddict-item]
    if data.get("securityRequirements") is not None:
        import capo_securityagent.types.batch_create_security_requirement_result_list

        out["security_requirements"] = (
            capo_securityagent.types.batch_create_security_requirement_result_list.deserialize_json(
                data["securityRequirements"]
            )
        )
    else:
        out["security_requirements"] = []
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
