"""Generated from Smithy shape ``com.amazonaws.ssm#Command``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.alarm_state_information_list
    import capo_ssm.types.cloud_watch_output_config
    import capo_ssm.types.command_id
    import capo_ssm.types.command_status
    import capo_ssm.types.comment
    import capo_ssm.types.completed_count
    import capo_ssm.types.date_time
    import capo_ssm.types.delivery_timed_out_count
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version
    import capo_ssm.types.error_count
    import capo_ssm.types.instance_id_list
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.notification_config
    import capo_ssm.types.parameters
    import capo_ssm.types.s3_bucket_name
    import capo_ssm.types.s3_key_prefix
    import capo_ssm.types.s3_region
    import capo_ssm.types.service_role
    import capo_ssm.types.status_details
    import capo_ssm.types.target_count
    import capo_ssm.types.targets
    import capo_ssm.types.timeout_seconds


class Command(TypedDict, closed=True):
    command_id: NotRequired["capo_ssm.types.command_id.CommandId"]
    """<p>A unique identifier for this command.</p>"""
    document_name: NotRequired["capo_ssm.types.document_name.DocumentName"]
    """<p>The name of the document requested for execution.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The Systems Manager document (SSM document) version.</p>"""
    comment: NotRequired["capo_ssm.types.comment.Comment"]
    """<p>User-specified information about the command, such as a brief description of what the command should do.</p>"""
    expires_after: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>If a command expires, it changes status to <code>DeliveryTimedOut</code> for all invocations that have the status <code>InProgress</code>, <code>Pending</code>, or <code>Delayed</code>. <code>ExpiresAfter</code> is calculated based on the total timeout for the overall command. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html?icmpid=docs_ec2_console#monitor-about-status-timeouts">Understanding command timeout values</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    parameters: NotRequired["capo_ssm.types.parameters.Parameters"]
    """<p>The parameter values to be inserted in the document when running the command.</p>"""
    instance_ids: NotRequired["capo_ssm.types.instance_id_list.InstanceIdList"]
    """<p>The managed node IDs against which this command was requested.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>An array of search criteria that targets managed nodes using a Key,Value combination that you specify. Targets is required if you don't provide one or more managed node IDs in the call.</p>"""
    requested_date_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the command was requested.</p>"""
    status: NotRequired["capo_ssm.types.command_status.CommandStatus"]
    """<p>The status of the command.</p>"""
    status_details: NotRequired["capo_ssm.types.status_details.StatusDetails"]
    """<p>A detailed status of the command execution. <code>StatusDetails</code> includes more information than <code>Status</code> because it includes states resulting from error and concurrency control parameters. <code>StatusDetails</code> can show different results than Status. For more information about these statuses, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html">Understanding command statuses</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. StatusDetails can be one of the following values:</p> <ul> <li> <p>Pending: The command hasn't been sent to any managed nodes.</p> </li> <li> <p>In Progress: The command has been sent to at least one managed node but hasn't reached a final state on all managed nodes.</p> </li> <li> <p>Success: The command successfully ran on all invocations. This is a terminal state.</p> </li> <li> <p>Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state.</p> </li> <li> <p>Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state.</p> </li> <li> <p>Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state.</p> </li> <li> <p>Incomplete: The command was attempted on all managed nodes and one or more invocations doesn't have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state.</p> </li> <li> <p>Cancelled: The command was terminated before it was completed. This is a terminal state.</p> </li> <li> <p>Rate Exceeded: The number of managed nodes targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before running it on any managed node. This is a terminal state.</p> </li> <li> <p>Delayed: The system attempted to send the command to the managed node but wasn't successful. The system retries again.</p> </li> </ul>"""
    output_s3_region: NotRequired["capo_ssm.types.s3_region.S3Region"]
    """<p>(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon Web Services Region of the S3 bucket.</p>"""
    output_s3_bucket_name: NotRequired["capo_ssm.types.s3_bucket_name.S3BucketName"]
    """<p>The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.</p>"""
    output_s3_key_prefix: NotRequired["capo_ssm.types.s3_key_prefix.S3KeyPrefix"]
    """<p>The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The maximum number of managed nodes that are allowed to run the command at the same time. You can specify a number of managed nodes, such as 10, or a percentage of nodes, such as 10%. The default value is 50. For more information about how to use <code>MaxConcurrency</code>, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html">Amazon Web Services Systems Manager Run Command</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is <code>0</code>. For more information about how to use <code>MaxErrors</code>, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html">Amazon Web Services Systems Manager Run Command</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    target_count: "capo_ssm.types.target_count.TargetCount"
    """<p>The number of targets for the command.</p>"""
    completed_count: "capo_ssm.types.completed_count.CompletedCount"
    """<p>The number of targets for which the command invocation reached a terminal state. Terminal states include the following: Success, Failed, Execution Timed Out, Delivery Timed Out, Cancelled, Terminated, or Undeliverable.</p>"""
    error_count: "capo_ssm.types.error_count.ErrorCount"
    """<p>The number of targets for which the status is Failed or Execution Timed Out.</p>"""
    delivery_timed_out_count: (
        "capo_ssm.types.delivery_timed_out_count.DeliveryTimedOutCount"
    )
    """<p>The number of targets for which the status is Delivery Timed Out.</p>"""
    service_role: NotRequired["capo_ssm.types.service_role.ServiceRole"]
    """<p>The Identity and Access Management (IAM) service role that Run Command, a tool in Amazon Web Services Systems Manager, uses to act on your behalf when sending notifications about command status changes. </p>"""
    notification_config: NotRequired[
        "capo_ssm.types.notification_config.NotificationConfig"
    ]
    """<p>Configurations for sending notifications about command status changes. </p>"""
    cloud_watch_output_config: NotRequired[
        "capo_ssm.types.cloud_watch_output_config.CloudWatchOutputConfig"
    ]
    """<p>Amazon CloudWatch Logs information where you want Amazon Web Services Systems Manager to send the command output.</p>"""
    timeout_seconds: NotRequired["capo_ssm.types.timeout_seconds.TimeoutSeconds"]
    """<p>The <code>TimeoutSeconds</code> value specified for a command.</p>"""
    alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The details for the CloudWatch alarm applied to your command.</p>"""
    triggered_alarms: NotRequired[
        "capo_ssm.types.alarm_state_information_list.AlarmStateInformationList"
    ]
    """<p>The CloudWatch alarm that was invoked by the command.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Command) -> dict:
    out: dict = {}
    if "command_id" in value:
        out["CommandId"] = value["command_id"]
    if "document_name" in value:
        out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "expires_after" in value:
        import capo_ssm.types.date_time

        out["ExpiresAfter"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["expires_after"]
        )
    if "parameters" in value:
        import capo_ssm.types.parameters

        out["Parameters"] = capo_ssm.types.parameters.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "instance_ids" in value:
        import capo_ssm.types.instance_id_list

        out["InstanceIds"] = capo_ssm.types.instance_id_list.serialize_aws_json_1_1(
            value["instance_ids"]
        )
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "requested_date_time" in value:
        import capo_ssm.types.date_time

        out["RequestedDateTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["requested_date_time"]
        )
    if "status" in value:
        import capo_ssm.types.command_status

        out["Status"] = capo_ssm.types.command_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "output_s3_region" in value:
        out["OutputS3Region"] = value["output_s3_region"]
    if "output_s3_bucket_name" in value:
        out["OutputS3BucketName"] = value["output_s3_bucket_name"]
    if "output_s3_key_prefix" in value:
        out["OutputS3KeyPrefix"] = value["output_s3_key_prefix"]
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    out["TargetCount"] = value.get("target_count", 0)
    out["CompletedCount"] = value.get("completed_count", 0)
    out["ErrorCount"] = value.get("error_count", 0)
    out["DeliveryTimedOutCount"] = value.get("delivery_timed_out_count", 0)
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
    if "timeout_seconds" in value:
        out["TimeoutSeconds"] = value["timeout_seconds"]
    if "alarm_configuration" in value:
        import capo_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            capo_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "triggered_alarms" in value:
        import capo_ssm.types.alarm_state_information_list

        out["TriggeredAlarms"] = (
            capo_ssm.types.alarm_state_information_list.serialize_aws_json_1_1(
                value["triggered_alarms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Command:
    out: Command = {}  # type: ignore[typeddict-item]
    if data.get("CommandId") is not None:
        out["command_id"] = data["CommandId"]
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("Comment") is not None:
        out["comment"] = data["Comment"]
    if data.get("ExpiresAfter") is not None:
        import capo_ssm.types.date_time

        out["expires_after"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExpiresAfter"]
        )
    if data.get("Parameters") is not None:
        import capo_ssm.types.parameters

        out["parameters"] = capo_ssm.types.parameters.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if data.get("InstanceIds") is not None:
        import capo_ssm.types.instance_id_list

        out["instance_ids"] = capo_ssm.types.instance_id_list.deserialize_aws_json_1_1(
            data["InstanceIds"]
        )
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("RequestedDateTime") is not None:
        import capo_ssm.types.date_time

        out["requested_date_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["RequestedDateTime"]
        )
    if data.get("Status") is not None:
        import capo_ssm.types.command_status

        out["status"] = capo_ssm.types.command_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("StatusDetails") is not None:
        out["status_details"] = data["StatusDetails"]
    if data.get("OutputS3Region") is not None:
        out["output_s3_region"] = data["OutputS3Region"]
    if data.get("OutputS3BucketName") is not None:
        out["output_s3_bucket_name"] = data["OutputS3BucketName"]
    if data.get("OutputS3KeyPrefix") is not None:
        out["output_s3_key_prefix"] = data["OutputS3KeyPrefix"]
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("MaxErrors") is not None:
        out["max_errors"] = data["MaxErrors"]
    if data.get("TargetCount") is not None:
        out["target_count"] = data["TargetCount"]
    else:
        out["target_count"] = 0
    if data.get("CompletedCount") is not None:
        out["completed_count"] = data["CompletedCount"]
    else:
        out["completed_count"] = 0
    if data.get("ErrorCount") is not None:
        out["error_count"] = data["ErrorCount"]
    else:
        out["error_count"] = 0
    if data.get("DeliveryTimedOutCount") is not None:
        out["delivery_timed_out_count"] = data["DeliveryTimedOutCount"]
    else:
        out["delivery_timed_out_count"] = 0
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
    if data.get("TimeoutSeconds") is not None:
        out["timeout_seconds"] = data["TimeoutSeconds"]
    if data.get("AlarmConfiguration") is not None:
        import capo_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            capo_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    if data.get("TriggeredAlarms") is not None:
        import capo_ssm.types.alarm_state_information_list

        out["triggered_alarms"] = (
            capo_ssm.types.alarm_state_information_list.deserialize_aws_json_1_1(
                data["TriggeredAlarms"]
            )
        )
    return out
