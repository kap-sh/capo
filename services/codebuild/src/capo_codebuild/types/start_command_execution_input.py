"""Generated from Smithy shape ``com.amazonaws.codebuild#StartCommandExecutionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.command_type
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.sensitive_non_empty_string


class StartCommandExecutionInput(TypedDict, closed=True):
    sandbox_id: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>"""
    command: "capo_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    """<p>The command that needs to be executed.</p>"""
    type: NotRequired["capo_codebuild.types.command_type.CommandType"]
    """<p>The command type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCommandExecutionInput) -> dict:
    out: dict = {}
    out["sandboxId"] = value["sandbox_id"]
    out["command"] = value["command"]
    if "type" in value:
        import capo_codebuild.types.command_type

        out["type"] = capo_codebuild.types.command_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCommandExecutionInput:
    out: StartCommandExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("sandboxId") is not None:
        out["sandbox_id"] = data["sandboxId"]
    else:
        out["sandbox_id"] = ""
    if data.get("command") is not None:
        out["command"] = data["command"]
    else:
        out["command"] = ""
    if data.get("type") is not None:
        import capo_codebuild.types.command_type

        out["type"] = capo_codebuild.types.command_type.deserialize_aws_json_1_1(
            data["type"]
        )
    return out


def redact_sensitive(value: StartCommandExecutionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "command" in value:
        out["command"] = "*** Sensitive Data Redacted ***"
    return out
