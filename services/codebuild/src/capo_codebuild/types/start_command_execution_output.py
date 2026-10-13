"""Generated from Smithy shape ``com.amazonaws.codebuild#StartCommandExecutionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.command_execution


class StartCommandExecutionOutput(TypedDict, closed=True):
    command_execution: NotRequired[
        "capo_codebuild.types.command_execution.CommandExecution"
    ]
    """<p>Information about the requested command executions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCommandExecutionOutput) -> dict:
    out: dict = {}
    if "command_execution" in value:
        import capo_codebuild.types.command_execution

        out["commandExecution"] = (
            capo_codebuild.types.command_execution.serialize_aws_json_1_1(
                value["command_execution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCommandExecutionOutput:
    out: StartCommandExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("commandExecution") is not None:
        import capo_codebuild.types.command_execution

        out["command_execution"] = (
            capo_codebuild.types.command_execution.deserialize_aws_json_1_1(
                data["commandExecution"]
            )
        )
    return out


def redact_sensitive(value: StartCommandExecutionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "command_execution" in value:
        import capo_codebuild.types.command_execution

        out["command_execution"] = (
            capo_codebuild.types.command_execution.redact_sensitive(
                value["command_execution"]
            )
        )
    return out
