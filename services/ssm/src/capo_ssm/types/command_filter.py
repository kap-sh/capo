"""Generated from Smithy shape ``com.amazonaws.ssm#CommandFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.command_filter_key
    import capo_ssm.types.command_filter_value


class CommandFilter(TypedDict, closed=True):
    key: "capo_ssm.types.command_filter_key.CommandFilterKey"
    """<p>The name of the filter.</p> <note> <p>The <code>ExecutionStage</code> filter can't be used with the <code>ListCommandInvocations</code> operation, only with <code>ListCommands</code>.</p> </note>"""
    value: "capo_ssm.types.command_filter_value.CommandFilterValue"
    """<p>The filter value. Valid values for each filter key are as follows:</p> <ul> <li> <p> <b>InvokedAfter</b>: Specify a timestamp to limit your results. For example, specify <code>2024-07-07T00:00:00Z</code> to see a list of command executions occurring July 7, 2021, and later.</p> </li> <li> <p> <b>InvokedBefore</b>: Specify a timestamp to limit your results. For example, specify <code>2024-07-07T00:00:00Z</code> to see a list of command executions from before July 7, 2021.</p> </li> <li> <p> <b>Status</b>: Specify a valid command status to see a list of all command executions with that status. The status choices depend on the API you call.</p> <p>The status values you can specify for <code>ListCommands</code> are:</p> <ul> <li> <p> <code>Pending</code> </p> </li> <li> <p> <code>InProgress</code> </p> </li> <li> <p> <code>Success</code> </p> </li> <li> <p> <code>Cancelled</code> </p> </li> <li> <p> <code>Failed</code> </p> </li> <li> <p> <code>TimedOut</code> (this includes both Delivery and Execution time outs) </p> </li> <li> <p> <code>AccessDenied</code> </p> </li> <li> <p> <code>DeliveryTimedOut</code> </p> </li> <li> <p> <code>ExecutionTimedOut</code> </p> </li> <li> <p> <code>Incomplete</code> </p> </li> <li> <p> <code>NoInstancesInTag</code> </p> </li> <li> <p> <code>LimitExceeded</code> </p> </li> </ul> <p>The status values you can specify for <code>ListCommandInvocations</code> are:</p> <ul> <li> <p> <code>Pending</code> </p> </li> <li> <p> <code>InProgress</code> </p> </li> <li> <p> <code>Delayed</code> </p> </li> <li> <p> <code>Success</code> </p> </li> <li> <p> <code>Cancelled</code> </p> </li> <li> <p> <code>Failed</code> </p> </li> <li> <p> <code>TimedOut</code> (this includes both Delivery and Execution time outs) </p> </li> <li> <p> <code>AccessDenied</code> </p> </li> <li> <p> <code>DeliveryTimedOut</code> </p> </li> <li> <p> <code>ExecutionTimedOut</code> </p> </li> <li> <p> <code>Undeliverable</code> </p> </li> <li> <p> <code>InvalidPlatform</code> </p> </li> <li> <p> <code>Terminated</code> </p> </li> </ul> </li> <li> <p> <b>DocumentName</b>: Specify name of the Amazon Web Services Systems Manager document (SSM document) for which you want to see command execution results. For example, specify <code>AWS-RunPatchBaseline</code> to see command executions that used this SSM document to perform security patching operations on managed nodes. </p> </li> <li> <p> <b>ExecutionStage</b>: Specify one of the following values (<code>ListCommands</code> operations only):</p> <ul> <li> <p> <code>Executing</code>: Returns a list of command executions that are currently still running.</p> </li> <li> <p> <code>Complete</code>: Returns a list of command executions that have already completed. </p> </li> </ul> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.command_filter_key

    out["key"] = capo_ssm.types.command_filter_key.serialize_aws_json_1_1(value["key"])
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CommandFilter:
    out: CommandFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        import capo_ssm.types.command_filter_key

        out["key"] = capo_ssm.types.command_filter_key.deserialize_aws_json_1_1(
            data["key"]
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.command_filter_key.CommandFilterKey", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
