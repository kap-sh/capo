"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetCommandExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.command_execution_ids
    import capo_codebuild.types.non_empty_string


class BatchGetCommandExecutionsInput(TypedDict, closed=True):
    sandbox_id: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>"""
    command_execution_ids: (
        "capo_codebuild.types.command_execution_ids.CommandExecutionIds"
    )
    """<p>A comma separated list of <code>commandExecutionIds</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCommandExecutionsInput) -> dict:
    out: dict = {}
    out["sandboxId"] = value["sandbox_id"]
    import capo_codebuild.types.command_execution_ids

    out["commandExecutionIds"] = (
        capo_codebuild.types.command_execution_ids.serialize_aws_json_1_1(
            value["command_execution_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCommandExecutionsInput:
    out: BatchGetCommandExecutionsInput = {}  # type: ignore[typeddict-item]
    if data.get("sandboxId") is not None:
        out["sandbox_id"] = data["sandboxId"]
    else:
        out["sandbox_id"] = ""
    if data.get("commandExecutionIds") is not None:
        import capo_codebuild.types.command_execution_ids

        out["command_execution_ids"] = (
            capo_codebuild.types.command_execution_ids.deserialize_aws_json_1_1(
                data["commandExecutionIds"]
            )
        )
    else:
        out["command_execution_ids"] = []
    return out
