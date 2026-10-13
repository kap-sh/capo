"""Generated from Smithy shape ``com.amazonaws.codebuild#CommandExecutions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.command_execution

CommandExecutions: TypeAlias = list[
    "capo_codebuild.types.command_execution.CommandExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandExecutions) -> list:
    import capo_codebuild.types.command_execution

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.command_execution.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommandExecutions:
    import capo_codebuild.types.command_execution

    out: CommandExecutions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.command_execution.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: CommandExecutions) -> list[Any]:
    import capo_codebuild.types.command_execution

    return [
        capo_codebuild.types.command_execution.redact_sensitive(item) for item in value
    ]
