"""Generated from Smithy shape ``com.amazonaws.sfn#ValidateStateMachineDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.definition
    import capo_sfn.types.state_machine_type
    import capo_sfn.types.validate_state_machine_definition_max_result
    import capo_sfn.types.validate_state_machine_definition_severity


class ValidateStateMachineDefinitionInput(TypedDict, closed=True):
    definition: "capo_sfn.types.definition.Definition"
    """<p>The Amazon States Language definition of the state machine. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a> (ASL).</p>"""
    type: NotRequired["capo_sfn.types.state_machine_type.StateMachineType"]
    """<p>The target type of state machine for this definition. The default is <code>STANDARD</code>.</p>"""
    severity: NotRequired[
        "capo_sfn.types.validate_state_machine_definition_severity.ValidateStateMachineDefinitionSeverity"
    ]
    """<p>Minimum level of diagnostics to return. <code>ERROR</code> returns only <code>ERROR</code> diagnostics, whereas <code>WARNING</code> returns both <code>WARNING</code> and <code>ERROR</code> diagnostics. The default is <code>ERROR</code>. </p>"""
    max_results: "capo_sfn.types.validate_state_machine_definition_max_result.ValidateStateMachineDefinitionMaxResult"
    """<p>The maximum number of diagnostics that are returned per call. The default and maximum value is 100. Setting the value to 0 will also use the default of 100.</p> <p>If the number of diagnostics returned in the response exceeds <code>maxResults</code>, the value of the <code>truncated</code> field in the response will be set to <code>true</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidateStateMachineDefinitionInput) -> dict:
    out: dict = {}
    out["definition"] = value["definition"]
    if "type" in value:
        import capo_sfn.types.state_machine_type

        out["type"] = capo_sfn.types.state_machine_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "severity" in value:
        import capo_sfn.types.validate_state_machine_definition_severity

        out["severity"] = (
            capo_sfn.types.validate_state_machine_definition_severity.serialize_aws_json_1_0(
                value["severity"]
            )
        )
    out["maxResults"] = value.get("max_results", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidateStateMachineDefinitionInput:
    out: ValidateStateMachineDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError(
            "ValidateStateMachineDefinitionInput.definition required"
        )
    if data.get("type") is not None:
        import capo_sfn.types.state_machine_type

        out["type"] = capo_sfn.types.state_machine_type.deserialize_aws_json_1_0(
            data["type"]
        )
    if data.get("severity") is not None:
        import capo_sfn.types.validate_state_machine_definition_severity

        out["severity"] = (
            capo_sfn.types.validate_state_machine_definition_severity.deserialize_aws_json_1_0(
                data["severity"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 0
    return out
