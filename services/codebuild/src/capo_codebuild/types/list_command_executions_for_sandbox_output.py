"""Generated from Smithy shape ``com.amazonaws.codebuild#ListCommandExecutionsForSandboxOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.command_executions
    import capo_codebuild.types.string


class ListCommandExecutionsForSandboxOutput(TypedDict, closed=True):
    command_executions: NotRequired[
        "capo_codebuild.types.command_executions.CommandExecutions"
    ]
    """<p>Information about the requested command executions.</p>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>Information about the next token to get paginated results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandExecutionsForSandboxOutput) -> dict:
    out: dict = {}
    if "command_executions" in value:
        import capo_codebuild.types.command_executions

        out["commandExecutions"] = (
            capo_codebuild.types.command_executions.serialize_aws_json_1_1(
                value["command_executions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommandExecutionsForSandboxOutput:
    out: ListCommandExecutionsForSandboxOutput = {}  # type: ignore[typeddict-item]
    if data.get("commandExecutions") is not None:
        import capo_codebuild.types.command_executions

        out["command_executions"] = (
            capo_codebuild.types.command_executions.deserialize_aws_json_1_1(
                data["commandExecutions"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListCommandExecutionsForSandboxOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "command_executions" in value:
        import capo_codebuild.types.command_executions

        out["command_executions"] = (
            capo_codebuild.types.command_executions.redact_sensitive(
                value["command_executions"]
            )
        )
    return out
