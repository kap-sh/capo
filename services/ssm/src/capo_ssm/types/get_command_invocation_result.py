"""Generated from Smithy shape ``com.amazonaws.ssm#GetCommandInvocationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_watch_output_config
    import capo_ssm.types.command_id
    import capo_ssm.types.command_invocation_status
    import capo_ssm.types.command_plugin_name
    import capo_ssm.types.comment
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version
    import capo_ssm.types.instance_id
    import capo_ssm.types.response_code
    import capo_ssm.types.standard_error_content
    import capo_ssm.types.standard_output_content
    import capo_ssm.types.status_details
    import capo_ssm.types.string_date_time
    import capo_ssm.types.url


class GetCommandInvocationResult(TypedDict, closed=True):
    command_id: NotRequired["capo_ssm.types.command_id.CommandId"]
    """<p>The parent command ID of the invocation plugin.</p>"""
    instance_id: NotRequired["capo_ssm.types.instance_id.InstanceId"]
    """<p>The ID of the managed node targeted by the command. A <i>managed node</i> can be an Amazon Elastic Compute Cloud (Amazon EC2) instance, edge device, or on-premises server or VM in your hybrid environment that is configured for Amazon Web Services Systems Manager.</p>"""
    comment: NotRequired["capo_ssm.types.comment.Comment"]
    """<p>The comment text for the command.</p>"""
    document_name: NotRequired["capo_ssm.types.document_name.DocumentName"]
    """<p>The name of the document that was run. For example, <code>AWS-RunShellScript</code>.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The Systems Manager document (SSM document) version used in the request.</p>"""
    plugin_name: NotRequired["capo_ssm.types.command_plugin_name.CommandPluginName"]
    """<p>The name of the plugin, or <i>step name</i>, for which details are reported. For example, <code>aws:RunShellScript</code> is a plugin.</p>"""
    response_code: "capo_ssm.types.response_code.ResponseCode"
    """<p>The error level response code for the plugin script. If the response code is <code>-1</code>, then the command hasn't started running on the managed node, or it wasn't received by the node.</p>"""
    execution_start_date_time: NotRequired[
        "capo_ssm.types.string_date_time.StringDateTime"
    ]
    """<p>The date and time the plugin started running. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample Amazon Web Services CLI command uses the <code>InvokedBefore</code> filter.</p> <p> <code>aws ssm list-commands --filters key=InvokedBefore,value=2017-06-07T00:00:00Z</code> </p> <p>If the plugin hasn't started to run, the string is empty.</p>"""
    execution_elapsed_time: NotRequired[
        "capo_ssm.types.string_date_time.StringDateTime"
    ]
    """<p>Duration since <code>ExecutionStartDateTime</code>.</p>"""
    execution_end_date_time: NotRequired[
        "capo_ssm.types.string_date_time.StringDateTime"
    ]
    """<p>The date and time the plugin finished running. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample Amazon Web Services CLI command uses the <code>InvokedAfter</code> filter.</p> <p> <code>aws ssm list-commands --filters key=InvokedAfter,value=2017-06-07T00:00:00Z</code> </p> <p>If the plugin hasn't started to run, the string is empty.</p>"""
    status: NotRequired[
        "capo_ssm.types.command_invocation_status.CommandInvocationStatus"
    ]
    """<p>The status of this invocation plugin. This status can be different than <code>StatusDetails</code>.</p>"""
    status_details: NotRequired["capo_ssm.types.status_details.StatusDetails"]
    """<p>A detailed status of the command execution for an invocation. <code>StatusDetails</code> includes more information than <code>Status</code> because it includes states resulting from error and concurrency control parameters. <code>StatusDetails</code> can show different results than <code>Status</code>. For more information about these statuses, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html">Understanding command statuses</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. <code>StatusDetails</code> can be one of the following values:</p> <ul> <li> <p>Pending: The command hasn't been sent to the managed node.</p> </li> <li> <p>In Progress: The command has been sent to the managed node but hasn't reached a terminal state.</p> </li> <li> <p>Delayed: The system attempted to send the command to the target, but the target wasn't available. The managed node might not be available because of network issues, because the node was stopped, or for similar reasons. The system will try to send the command again.</p> </li> <li> <p>Success: The command or plugin ran successfully. This is a terminal state.</p> </li> <li> <p>Delivery Timed Out: The command wasn't delivered to the managed node before the delivery timeout expired. Delivery timeouts don't count against the parent command's <code>MaxErrors</code> limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.</p> </li> <li> <p>Execution Timed Out: The command started to run on the managed node, but the execution wasn't complete before the timeout expired. Execution timeouts count against the <code>MaxErrors</code> limit of the parent command. This is a terminal state.</p> </li> <li> <p>Failed: The command wasn't run successfully on the managed node. For a plugin, this indicates that the result code wasn't zero. For a command invocation, this indicates that the result code for one or more plugins wasn't zero. Invocation failures count against the <code>MaxErrors</code> limit of the parent command. This is a terminal state.</p> </li> <li> <p>Cancelled: The command was terminated before it was completed. This is a terminal state.</p> </li> <li> <p>Undeliverable: The command can't be delivered to the managed node. The node might not exist or might not be responding. Undeliverable invocations don't count against the parent command's <code>MaxErrors</code> limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.</p> </li> <li> <p>Terminated: The parent command exceeded its <code>MaxErrors</code> limit and subsequent command invocations were canceled by the system. This is a terminal state.</p> </li> </ul>"""
    standard_output_content: NotRequired[
        "capo_ssm.types.standard_output_content.StandardOutputContent"
    ]
    """<p>The first 24,000 characters written by the plugin to <code>stdout</code>. If the command hasn't finished running, if <code>ExecutionStatus</code> is neither Succeeded nor Failed, then this string is empty.</p>"""
    standard_output_url: NotRequired["capo_ssm.types.url.Url"]
    """<p>The URL for the complete text written by the plugin to <code>stdout</code> in Amazon Simple Storage Service (Amazon S3). If an S3 bucket wasn't specified, then this string is empty.</p>"""
    standard_error_content: NotRequired[
        "capo_ssm.types.standard_error_content.StandardErrorContent"
    ]
    """<p>The first 8,000 characters written by the plugin to <code>stderr</code>. If the command hasn't finished running, then this string is empty.</p>"""
    standard_error_url: NotRequired["capo_ssm.types.url.Url"]
    """<p>The URL for the complete text written by the plugin to <code>stderr</code>. If the command hasn't finished running, then this string is empty.</p>"""
    cloud_watch_output_config: NotRequired[
        "capo_ssm.types.cloud_watch_output_config.CloudWatchOutputConfig"
    ]
    """<p>Amazon CloudWatch Logs information where Systems Manager sent the command output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommandInvocationResult) -> dict:
    out: dict = {}
    if "command_id" in value:
        out["CommandId"] = value["command_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "document_name" in value:
        out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "plugin_name" in value:
        out["PluginName"] = value["plugin_name"]
    out["ResponseCode"] = value.get("response_code", 0)
    if "execution_start_date_time" in value:
        out["ExecutionStartDateTime"] = value["execution_start_date_time"]
    if "execution_elapsed_time" in value:
        out["ExecutionElapsedTime"] = value["execution_elapsed_time"]
    if "execution_end_date_time" in value:
        out["ExecutionEndDateTime"] = value["execution_end_date_time"]
    if "status" in value:
        import capo_ssm.types.command_invocation_status

        out["Status"] = capo_ssm.types.command_invocation_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "standard_output_content" in value:
        out["StandardOutputContent"] = value["standard_output_content"]
    if "standard_output_url" in value:
        out["StandardOutputUrl"] = value["standard_output_url"]
    if "standard_error_content" in value:
        out["StandardErrorContent"] = value["standard_error_content"]
    if "standard_error_url" in value:
        out["StandardErrorUrl"] = value["standard_error_url"]
    if "cloud_watch_output_config" in value:
        import capo_ssm.types.cloud_watch_output_config

        out["CloudWatchOutputConfig"] = (
            capo_ssm.types.cloud_watch_output_config.serialize_aws_json_1_1(
                value["cloud_watch_output_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommandInvocationResult:
    out: GetCommandInvocationResult = {}  # type: ignore[typeddict-item]
    if data.get("CommandId") is not None:
        out["command_id"] = data["CommandId"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("Comment") is not None:
        out["comment"] = data["Comment"]
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("PluginName") is not None:
        out["plugin_name"] = data["PluginName"]
    if data.get("ResponseCode") is not None:
        out["response_code"] = data["ResponseCode"]
    else:
        out["response_code"] = 0
    if data.get("ExecutionStartDateTime") is not None:
        out["execution_start_date_time"] = data["ExecutionStartDateTime"]
    if data.get("ExecutionElapsedTime") is not None:
        out["execution_elapsed_time"] = data["ExecutionElapsedTime"]
    if data.get("ExecutionEndDateTime") is not None:
        out["execution_end_date_time"] = data["ExecutionEndDateTime"]
    if data.get("Status") is not None:
        import capo_ssm.types.command_invocation_status

        out["status"] = (
            capo_ssm.types.command_invocation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusDetails") is not None:
        out["status_details"] = data["StatusDetails"]
    if data.get("StandardOutputContent") is not None:
        out["standard_output_content"] = data["StandardOutputContent"]
    if data.get("StandardOutputUrl") is not None:
        out["standard_output_url"] = data["StandardOutputUrl"]
    if data.get("StandardErrorContent") is not None:
        out["standard_error_content"] = data["StandardErrorContent"]
    if data.get("StandardErrorUrl") is not None:
        out["standard_error_url"] = data["StandardErrorUrl"]
    if data.get("CloudWatchOutputConfig") is not None:
        import capo_ssm.types.cloud_watch_output_config

        out["cloud_watch_output_config"] = (
            capo_ssm.types.cloud_watch_output_config.deserialize_aws_json_1_1(
                data["CloudWatchOutputConfig"]
            )
        )
    return out
