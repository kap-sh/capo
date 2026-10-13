"""Generated from Smithy shape ``com.amazonaws.sfn#ValidateStateMachineDefinitionDiagnosticList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_sfn.types.validate_state_machine_definition_diagnostic

ValidateStateMachineDefinitionDiagnosticList: TypeAlias = list[
    "capo_sfn.types.validate_state_machine_definition_diagnostic.ValidateStateMachineDefinitionDiagnostic"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidateStateMachineDefinitionDiagnosticList) -> list:
    import capo_sfn.types.validate_state_machine_definition_diagnostic

    out: list = []
    for item in value:
        out.append(
            capo_sfn.types.validate_state_machine_definition_diagnostic.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> ValidateStateMachineDefinitionDiagnosticList:
    import capo_sfn.types.validate_state_machine_definition_diagnostic

    out: ValidateStateMachineDefinitionDiagnosticList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sfn.types.validate_state_machine_definition_diagnostic.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: ValidateStateMachineDefinitionDiagnosticList) -> list[Any]:
    import capo_sfn.types.validate_state_machine_definition_diagnostic

    return [
        capo_sfn.types.validate_state_machine_definition_diagnostic.redact_sensitive(
            item
        )
        for item in value
    ]
