"""Generated from Smithy shape ``com.amazonaws.sfn#ValidateStateMachineDefinitionDiagnostic``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.validate_state_machine_definition_code
    import capo_sfn.types.validate_state_machine_definition_location
    import capo_sfn.types.validate_state_machine_definition_message
    import capo_sfn.types.validate_state_machine_definition_severity


class ValidateStateMachineDefinitionDiagnostic(TypedDict, closed=True):
    severity: "capo_sfn.types.validate_state_machine_definition_severity.ValidateStateMachineDefinitionSeverity"
    """<p>A value of <code>ERROR</code> means that you cannot create or update a state machine with this definition.</p> <p> <code>WARNING</code> level diagnostics alert you to potential issues, but they will not prevent you from creating or updating your state machine.</p>"""
    code: "capo_sfn.types.validate_state_machine_definition_code.ValidateStateMachineDefinitionCode"
    """<p>Identifying code for the diagnostic.</p>"""
    message: "capo_sfn.types.validate_state_machine_definition_message.ValidateStateMachineDefinitionMessage"
    """<p>Message describing the diagnostic condition.</p>"""
    location: NotRequired[
        "capo_sfn.types.validate_state_machine_definition_location.ValidateStateMachineDefinitionLocation"
    ]
    """<p>Location of the issue in the state machine, if available.</p> <p>For errors specific to a field, the location could be in the format: <code>/States/<StateName>/<FieldName></code>, for example: <code>/States/FailState/ErrorPath</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidateStateMachineDefinitionDiagnostic) -> dict:
    out: dict = {}
    import capo_sfn.types.validate_state_machine_definition_severity

    out["severity"] = (
        capo_sfn.types.validate_state_machine_definition_severity.serialize_aws_json_1_0(
            value["severity"]
        )
    )
    out["code"] = value["code"]
    out["message"] = value["message"]
    if "location" in value:
        out["location"] = value["location"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidateStateMachineDefinitionDiagnostic:
    out: ValidateStateMachineDefinitionDiagnostic = {}  # type: ignore[typeddict-item]
    if data.get("severity") is not None:
        import capo_sfn.types.validate_state_machine_definition_severity

        out["severity"] = (
            capo_sfn.types.validate_state_machine_definition_severity.deserialize_aws_json_1_0(
                data["severity"]
            )
        )
    else:
        raise DeserializationError(
            "ValidateStateMachineDefinitionDiagnostic.severity required"
        )
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError(
            "ValidateStateMachineDefinitionDiagnostic.code required"
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "ValidateStateMachineDefinitionDiagnostic.message required"
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    return out


def redact_sensitive(value: ValidateStateMachineDefinitionDiagnostic) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code" in value:
        out["code"] = "*** Sensitive Data Redacted ***"
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    if "location" in value:
        out["location"] = "*** Sensitive Data Redacted ***"
    return out
