"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetCommandExecutionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.command_execution_ids
    import capo_codebuild.types.command_executions


class BatchGetCommandExecutionsOutput(TypedDict, closed=True):
    command_executions: NotRequired[
        "capo_codebuild.types.command_executions.CommandExecutions"
    ]
    """<p>Information about the requested command executions.</p>"""
    command_executions_not_found: NotRequired[
        "capo_codebuild.types.command_execution_ids.CommandExecutionIds"
    ]
    """<p>The IDs of command executions for which information could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCommandExecutionsOutput) -> dict:
    out: dict = {}
    if "command_executions" in value:
        import capo_codebuild.types.command_executions

        out["commandExecutions"] = (
            capo_codebuild.types.command_executions.serialize_aws_json_1_1(
                value["command_executions"]
            )
        )
    if "command_executions_not_found" in value:
        import capo_codebuild.types.command_execution_ids

        out["commandExecutionsNotFound"] = (
            capo_codebuild.types.command_execution_ids.serialize_aws_json_1_1(
                value["command_executions_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCommandExecutionsOutput:
    out: BatchGetCommandExecutionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("commandExecutions") is not None:
        import capo_codebuild.types.command_executions

        out["command_executions"] = (
            capo_codebuild.types.command_executions.deserialize_aws_json_1_1(
                data["commandExecutions"]
            )
        )
    if data.get("commandExecutionsNotFound") is not None:
        import capo_codebuild.types.command_execution_ids

        out["command_executions_not_found"] = (
            capo_codebuild.types.command_execution_ids.deserialize_aws_json_1_1(
                data["commandExecutionsNotFound"]
            )
        )
    return out


def redact_sensitive(value: BatchGetCommandExecutionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "command_executions" in value:
        import capo_codebuild.types.command_executions

        out["command_executions"] = (
            capo_codebuild.types.command_executions.redact_sensitive(
                value["command_executions"]
            )
        )
    return out
