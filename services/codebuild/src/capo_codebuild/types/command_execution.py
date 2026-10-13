"""Generated from Smithy shape ``com.amazonaws.codebuild#CommandExecution``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.command_type
    import capo_codebuild.types.logs_location
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.sensitive_non_empty_string
    import capo_codebuild.types.timestamp


class CommandExecution(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the command execution.</p>"""
    sandbox_id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>A <code>sandboxId</code>.</p>"""
    submit_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the command execution process was initially submitted, expressed in Unix time format.</p>"""
    start_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the command execution process started, expressed in Unix time format.</p>"""
    end_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the command execution process ended, expressed in Unix time format.</p>"""
    status: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The status of the command execution.</p>"""
    command: NotRequired[
        "capo_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The command that needs to be executed.</p>"""
    type: NotRequired["capo_codebuild.types.command_type.CommandType"]
    """<p>The command type.</p>"""
    exit_code: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The exit code to return upon completion.</p>"""
    standard_output_content: NotRequired[
        "capo_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The text written by the command to stdout.</p>"""
    standard_err_content: NotRequired[
        "capo_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The text written by the command to stderr.</p>"""
    logs: NotRequired["capo_codebuild.types.logs_location.LogsLocation"]
    sandbox_arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>A <code>sandboxArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandExecution) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "sandbox_id" in value:
        out["sandboxId"] = value["sandbox_id"]
    if "submit_time" in value:
        import capo_codebuild.types.timestamp

        out["submitTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["submit_time"]
        )
    if "start_time" in value:
        import capo_codebuild.types.timestamp

        out["startTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codebuild.types.timestamp

        out["endTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "command" in value:
        out["command"] = value["command"]
    if "type" in value:
        import capo_codebuild.types.command_type

        out["type"] = capo_codebuild.types.command_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "standard_output_content" in value:
        out["standardOutputContent"] = value["standard_output_content"]
    if "standard_err_content" in value:
        out["standardErrContent"] = value["standard_err_content"]
    if "logs" in value:
        import capo_codebuild.types.logs_location

        out["logs"] = capo_codebuild.types.logs_location.serialize_aws_json_1_1(
            value["logs"]
        )
    if "sandbox_arn" in value:
        out["sandboxArn"] = value["sandbox_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CommandExecution:
    out: CommandExecution = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("sandboxId") is not None:
        out["sandbox_id"] = data["sandboxId"]
    if data.get("submitTime") is not None:
        import capo_codebuild.types.timestamp

        out["submit_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["submitTime"]
        )
    if data.get("startTime") is not None:
        import capo_codebuild.types.timestamp

        out["start_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_codebuild.types.timestamp

        out["end_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("command") is not None:
        out["command"] = data["command"]
    if data.get("type") is not None:
        import capo_codebuild.types.command_type

        out["type"] = capo_codebuild.types.command_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("exitCode") is not None:
        out["exit_code"] = data["exitCode"]
    if data.get("standardOutputContent") is not None:
        out["standard_output_content"] = data["standardOutputContent"]
    if data.get("standardErrContent") is not None:
        out["standard_err_content"] = data["standardErrContent"]
    if data.get("logs") is not None:
        import capo_codebuild.types.logs_location

        out["logs"] = capo_codebuild.types.logs_location.deserialize_aws_json_1_1(
            data["logs"]
        )
    if data.get("sandboxArn") is not None:
        out["sandbox_arn"] = data["sandboxArn"]
    return out


def redact_sensitive(value: CommandExecution) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "command" in value:
        out["command"] = "*** Sensitive Data Redacted ***"
    if "standard_output_content" in value:
        out["standard_output_content"] = "*** Sensitive Data Redacted ***"
    if "standard_err_content" in value:
        out["standard_err_content"] = "*** Sensitive Data Redacted ***"
    return out
