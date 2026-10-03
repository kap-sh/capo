"""Generated from Smithy shape ``com.amazonaws.ssm#CommandInvocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_watch_output_config
    import capo_ssm.types.command_id
    import capo_ssm.types.command_invocation_status
    import capo_ssm.types.command_plugin_list
    import capo_ssm.types.comment
    import capo_ssm.types.date_time
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version
    import capo_ssm.types.instance_id
    import capo_ssm.types.instance_tag_name
    import capo_ssm.types.invocation_trace_output
    import capo_ssm.types.notification_config
    import capo_ssm.types.service_role
    import capo_ssm.types.status_details
    import capo_ssm.types.url


class CommandInvocation(TypedDict, closed=True):
    command_id: NotRequired["capo_ssm.types.command_id.CommandId"]
    """<p>The command against which this invocation was requested.</p>"""
    instance_id: NotRequired["capo_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID in which this invocation was requested.</p>"""
    instance_name: NotRequired["capo_ssm.types.instance_tag_name.InstanceTagName"]
    """<p>The fully qualified host name of the managed node.</p>"""
    comment: NotRequired["capo_ssm.types.comment.Comment"]
    """<p>User-specified information about the command, such as a brief description of what the command should do.</p>"""
    document_name: NotRequired["capo_ssm.types.document_name.DocumentName"]
    """<p>The document name that was requested for execution.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The Systems Manager document (SSM document) version.</p>"""
    requested_date_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time and date the request was sent to this managed node.</p>"""
    status: NotRequired[
        "capo_ssm.types.command_invocation_status.CommandInvocationStatus"
    ]
    """<p>Whether or not the invocation succeeded, failed, or is pending.</p>"""
    status_details: NotRequired["capo_ssm.types.status_details.StatusDetails"]
    """<p>A detailed status of the command execution for each invocation (each managed node targeted by the command). StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html">Understanding command statuses</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. StatusDetails can be one of the following values:</p> <ul> <li> <p>Pending: The command hasn't been sent to the managed node.</p> </li> <li> <p>In Progress: The command has been sent to the managed node but hasn't reached a terminal state.</p> </li> <li> <p>Success: The execution of the command or plugin was successfully completed. This is a terminal state.</p> </li> <li> <p>Delivery Timed Out: The command wasn't delivered to the managed node before the delivery timeout expired. Delivery timeouts don't count against the parent command's <code>MaxErrors</code> limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.</p> </li> <li> <p>Execution Timed Out: Command execution started on the managed node, but the execution wasn't complete before the execution timeout expired. Execution timeouts count against the <code>MaxErrors</code> limit of the parent command. This is a terminal state.</p> </li> <li> <p>Failed: The command wasn't successful on the managed node. For a plugin, this indicates that the result code wasn't zero. For a command invocation, this indicates that the result code for one or more plugins wasn't zero. Invocation failures count against the <code>MaxErrors</code> limit of the parent command. This is a terminal state.</p> </li> <li> <p>Cancelled: The command was terminated before it was completed. This is a terminal state.</p> </li> <li> <p>Undeliverable: The command can't be delivered to the managed node. The managed node might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.</p> </li> <li> <p>Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.</p> </li> <li> <p>Delayed: The system attempted to send the command to the managed node but wasn't successful. The system retries again.</p> </li> </ul>"""
    trace_output: NotRequired[
        "capo_ssm.types.invocation_trace_output.InvocationTraceOutput"
    ]
    """<p> Gets the trace output sent by the agent. </p>"""
    standard_output_url: NotRequired["capo_ssm.types.url.Url"]
    """<p>The URL to the plugin's StdOut file in Amazon Simple Storage Service (Amazon S3), if the S3 bucket was defined for the parent command. For an invocation, <code>StandardOutputUrl</code> is populated if there is just one plugin defined for the command, and the S3 bucket was defined for the command.</p>"""
    standard_error_url: NotRequired["capo_ssm.types.url.Url"]
    """<p>The URL to the plugin's StdErr file in Amazon Simple Storage Service (Amazon S3), if the S3 bucket was defined for the parent command. For an invocation, <code>StandardErrorUrl</code> is populated if there is just one plugin defined for the command, and the S3 bucket was defined for the command.</p>"""
    command_plugins: NotRequired["capo_ssm.types.command_plugin_list.CommandPluginList"]
    """<p>Plugins processed by the command.</p>"""
    service_role: NotRequired["capo_ssm.types.service_role.ServiceRole"]
    """<p>The Identity and Access Management (IAM) service role that Run Command, a tool in Amazon Web Services Systems Manager, uses to act on your behalf when sending notifications about command status changes on a per managed node basis.</p>"""
    notification_config: NotRequired[
        "capo_ssm.types.notification_config.NotificationConfig"
    ]
    """<p>Configurations for sending notifications about command status changes on a per managed node basis.</p>"""
    cloud_watch_output_config: NotRequired[
        "capo_ssm.types.cloud_watch_output_config.CloudWatchOutputConfig"
    ]
    """<p>Amazon CloudWatch Logs information where you want Amazon Web Services Systems Manager to send the command output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandInvocation) -> dict:
    out: dict = {}
    if "command_id" in value:
        out["CommandId"] = value["command_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "instance_name" in value:
        out["InstanceName"] = value["instance_name"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "document_name" in value:
        out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "requested_date_time" in value:
        import capo_ssm.types.date_time

        out["RequestedDateTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["requested_date_time"]
        )
    if "status" in value:
        import capo_ssm.types.command_invocation_status

        out["Status"] = capo_ssm.types.command_invocation_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "trace_output" in value:
        out["TraceOutput"] = value["trace_output"]
    if "standard_output_url" in value:
        out["StandardOutputUrl"] = value["standard_output_url"]
    if "standard_error_url" in value:
        out["StandardErrorUrl"] = value["standard_error_url"]
    if "command_plugins" in value:
        import capo_ssm.types.command_plugin_list

        out["CommandPlugins"] = (
            capo_ssm.types.command_plugin_list.serialize_aws_json_1_1(
                value["command_plugins"]
            )
        )
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "notification_config" in value:
        import capo_ssm.types.notification_config

        out["NotificationConfig"] = (
            capo_ssm.types.notification_config.serialize_aws_json_1_1(
                value["notification_config"]
            )
        )
    if "cloud_watch_output_config" in value:
        import capo_ssm.types.cloud_watch_output_config

        out["CloudWatchOutputConfig"] = (
            capo_ssm.types.cloud_watch_output_config.serialize_aws_json_1_1(
                value["cloud_watch_output_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CommandInvocation:
    out: CommandInvocation = {}  # type: ignore[typeddict-item]
    if data.get("CommandId") is not None:
        out["command_id"] = data["CommandId"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("InstanceName") is not None:
        out["instance_name"] = data["InstanceName"]
    if data.get("Comment") is not None:
        out["comment"] = data["Comment"]
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("RequestedDateTime") is not None:
        import capo_ssm.types.date_time

        out["requested_date_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["RequestedDateTime"]
        )
    if data.get("Status") is not None:
        import capo_ssm.types.command_invocation_status

        out["status"] = (
            capo_ssm.types.command_invocation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusDetails") is not None:
        out["status_details"] = data["StatusDetails"]
    if data.get("TraceOutput") is not None:
        out["trace_output"] = data["TraceOutput"]
    if data.get("StandardOutputUrl") is not None:
        out["standard_output_url"] = data["StandardOutputUrl"]
    if data.get("StandardErrorUrl") is not None:
        out["standard_error_url"] = data["StandardErrorUrl"]
    if data.get("CommandPlugins") is not None:
        import capo_ssm.types.command_plugin_list

        out["command_plugins"] = (
            capo_ssm.types.command_plugin_list.deserialize_aws_json_1_1(
                data["CommandPlugins"]
            )
        )
    if data.get("ServiceRole") is not None:
        out["service_role"] = data["ServiceRole"]
    if data.get("NotificationConfig") is not None:
        import capo_ssm.types.notification_config

        out["notification_config"] = (
            capo_ssm.types.notification_config.deserialize_aws_json_1_1(
                data["NotificationConfig"]
            )
        )
    if data.get("CloudWatchOutputConfig") is not None:
        import capo_ssm.types.cloud_watch_output_config

        out["cloud_watch_output_config"] = (
            capo_ssm.types.cloud_watch_output_config.deserialize_aws_json_1_1(
                data["CloudWatchOutputConfig"]
            )
        )
    return out
