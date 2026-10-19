"""Generated from Smithy shape ``com.amazonaws.transfer#ExecutionError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.execution_error_message
    import capo_transfer.types.execution_error_type


class ExecutionError(TypedDict, closed=True):
    type: "capo_transfer.types.execution_error_type.ExecutionErrorType"
    """<p>Specifies the error type.</p> <ul> <li> <p> <code>ALREADY_EXISTS</code>: occurs for a copy step, if the overwrite option is not selected and a file with the same name already exists in the target location.</p> </li> <li> <p> <code>BAD_REQUEST</code>: a general bad request: for example, a step that attempts to tag an EFS file returns <code>BAD_REQUEST</code>, as only S3 files can be tagged.</p> </li> <li> <p> <code>CUSTOM_STEP_FAILED</code>: occurs when the custom step provided a callback that indicates failure.</p> </li> <li> <p> <code>INTERNAL_SERVER_ERROR</code>: a catch-all error that can occur for a variety of reasons.</p> </li> <li> <p> <code>NOT_FOUND</code>: occurs when a requested entity, for example a source file for a copy step, does not exist.</p> </li> <li> <p> <code>PERMISSION_DENIED</code>: occurs if your policy does not contain the correct permissions to complete one or more of the steps in the workflow.</p> </li> <li> <p> <code>TIMEOUT</code>: occurs when the execution times out.</p> <note> <p> You can set the <code>TimeoutSeconds</code> for a custom step, anywhere from 1 second to 1800 seconds (30 minutes). </p> </note> </li> <li> <p> <code>THROTTLED</code>: occurs if you exceed the new execution refill rate of one workflow per second.</p> </li> </ul>"""
    message: "capo_transfer.types.execution_error_message.ExecutionErrorMessage"
    """<p>Specifies the descriptive message that corresponds to the <code>ErrorType</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionError) -> dict:
    out: dict = {}
    import capo_transfer.types.execution_error_type

    out["Type"] = capo_transfer.types.execution_error_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionError:
    out: ExecutionError = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_transfer.types.execution_error_type

        out["type"] = capo_transfer.types.execution_error_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_transfer.types.execution_error_type.ExecutionErrorType", ""
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
