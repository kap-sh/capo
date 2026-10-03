"""Generated from Smithy shape ``com.amazonaws.ssm#SendCommandRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.cloud_watch_output_config
    import capo_ssm.types.comment
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_hash
    import capo_ssm.types.document_hash_type
    import capo_ssm.types.document_version
    import capo_ssm.types.instance_id_list
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.notification_config
    import capo_ssm.types.parameters
    import capo_ssm.types.s3_bucket_name
    import capo_ssm.types.s3_key_prefix
    import capo_ssm.types.s3_region
    import capo_ssm.types.service_role
    import capo_ssm.types.targets
    import capo_ssm.types.timeout_seconds


class SendCommandRequest(TypedDict, closed=True):
    instance_ids: NotRequired["capo_ssm.types.instance_id_list.InstanceIdList"]
    """<p>The IDs of the managed nodes where the command should run. Specifying managed node IDs is most useful when you are targeting a limited number of managed nodes, though you can specify up to 50 IDs.</p> <p>To target a larger number of managed nodes, or if you prefer not to list individual node IDs, we recommend using the <code>Targets</code> option instead. Using <code>Targets</code>, which accepts tag key-value pairs to identify the managed nodes to send commands to, you can a send command to tens, hundreds, or thousands of nodes at once.</p> <p>For more information about how to use targets, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html">Run commands at scale</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>An array of search criteria that targets managed nodes using a <code>Key,Value</code> combination that you specify. Specifying targets is most useful when you want to send a command to a large number of managed nodes at once. Using <code>Targets</code>, which accepts tag key-value pairs to identify managed nodes, you can send a command to tens, hundreds, or thousands of nodes at once.</p> <p>To send a command to a smaller number of managed nodes, you can use the <code>InstanceIds</code> option instead.</p> <p>For more information about how to use targets, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html">Run commands at scale</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    document_name: "capo_ssm.types.document_arn.DocumentARN"
    """<p>The name of the Amazon Web Services Systems Manager document (SSM document) to run. This can be a public document or a custom document. To run a shared document belonging to another account, specify the document Amazon Resource Name (ARN). For more information about how to use shared documents, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-using-shared.html">Sharing SSM documents</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <note> <p>If you specify a document name or ARN that hasn't been shared with your account, you receive an <code>InvalidDocument</code> error. </p> </note>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    r"""<p>The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you run commands by using the Command Line Interface (Amazon Web Services CLI), then you must escape the first two options by using a backslash. If you specify a version number, then you don't need to use the backslash. For example:</p> <p>--document-version "\$DEFAULT"</p> <p>--document-version "\$LATEST"</p> <p>--document-version "3"</p>"""
    document_hash: NotRequired["capo_ssm.types.document_hash.DocumentHash"]
    """<p>The Sha256 or Sha1 hash created by the system when the document was created. </p> <note> <p>Sha1 hashes have been deprecated.</p> </note>"""
    document_hash_type: NotRequired[
        "capo_ssm.types.document_hash_type.DocumentHashType"
    ]
    """<p>Sha256 or Sha1.</p> <note> <p>Sha1 hashes have been deprecated.</p> </note>"""
    timeout_seconds: NotRequired["capo_ssm.types.timeout_seconds.TimeoutSeconds"]
    """<p>If this time is reached and the command hasn't already started running, it won't run.</p>"""
    comment: NotRequired["capo_ssm.types.comment.Comment"]
    """<p>User-specified information about the command, such as a brief description of what the command should do.</p>"""
    parameters: NotRequired["capo_ssm.types.parameters.Parameters"]
    """<p>The required and optional parameters specified in the document being run.</p>"""
    output_s3_region: NotRequired["capo_ssm.types.s3_region.S3Region"]
    """<p>(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon Web Services Region of the S3 bucket.</p>"""
    output_s3_bucket_name: NotRequired["capo_ssm.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the S3 bucket where command execution responses should be stored.</p>"""
    output_s3_key_prefix: NotRequired["capo_ssm.types.s3_key_prefix.S3KeyPrefix"]
    """<p>The directory structure within the S3 bucket where the responses should be stored.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>(Optional) The maximum number of managed nodes that are allowed to run the command at the same time. You can specify a number such as 10 or a percentage such as 10%. The default value is <code>50</code>. For more information about how to use <code>MaxConcurrency</code>, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-velocity">Using concurrency controls</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The maximum number of errors allowed without the command failing. When the command fails one more time beyond the value of <code>MaxErrors</code>, the systems stops sending the command to additional targets. You can specify a number like 10 or a percentage like 10%. The default value is <code>0</code>. For more information about how to use <code>MaxErrors</code>, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-maxerrors">Using error controls</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    service_role_arn: NotRequired["capo_ssm.types.service_role.ServiceRole"]
    """<p>The ARN of the Identity and Access Management (IAM) service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for Run Command commands.</p> <p>This role must provide the <code>sns:Publish</code> permission for your notification topic. For information about creating and using this service role, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html">Monitoring Systems Manager status changes using Amazon SNS notifications</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    notification_config: NotRequired[
        "capo_ssm.types.notification_config.NotificationConfig"
    ]
    """<p>Configurations for sending notifications.</p>"""
    cloud_watch_output_config: NotRequired[
        "capo_ssm.types.cloud_watch_output_config.CloudWatchOutputConfig"
    ]
    """<p>Enables Amazon Web Services Systems Manager to send Run Command output to Amazon CloudWatch Logs. Run Command is a tool in Amazon Web Services Systems Manager.</p>"""
    alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The CloudWatch alarm you want to apply to your command.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendCommandRequest) -> dict:
    out: dict = {}
    if "instance_ids" in value:
        import capo_ssm.types.instance_id_list

        out["InstanceIds"] = capo_ssm.types.instance_id_list.serialize_aws_json_1_1(
            value["instance_ids"]
        )
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "document_hash" in value:
        out["DocumentHash"] = value["document_hash"]
    if "document_hash_type" in value:
        import capo_ssm.types.document_hash_type

        out["DocumentHashType"] = (
            capo_ssm.types.document_hash_type.serialize_aws_json_1_1(
                value["document_hash_type"]
            )
        )
    if "timeout_seconds" in value:
        out["TimeoutSeconds"] = value["timeout_seconds"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "parameters" in value:
        import capo_ssm.types.parameters

        out["Parameters"] = capo_ssm.types.parameters.serialize_aws_json_1_1(
            value["parameters"]
        )
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
    if "service_role_arn" in value:
        out["ServiceRoleArn"] = value["service_role_arn"]
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
    if "alarm_configuration" in value:
        import capo_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            capo_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SendCommandRequest:
    out: SendCommandRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    else:
        raise DeserializationError("SendCommandRequest.document_name required")
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("DocumentHash") is not None:
        out["document_hash"] = data["DocumentHash"]
    if data.get("DocumentHashType") is not None:
        import capo_ssm.types.document_hash_type

        out["document_hash_type"] = (
            capo_ssm.types.document_hash_type.deserialize_aws_json_1_1(
                data["DocumentHashType"]
            )
        )
    if data.get("TimeoutSeconds") is not None:
        out["timeout_seconds"] = data["TimeoutSeconds"]
    if data.get("Comment") is not None:
        out["comment"] = data["Comment"]
    if data.get("Parameters") is not None:
        import capo_ssm.types.parameters

        out["parameters"] = capo_ssm.types.parameters.deserialize_aws_json_1_1(
            data["Parameters"]
        )
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
    if data.get("ServiceRoleArn") is not None:
        out["service_role_arn"] = data["ServiceRoleArn"]
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
    if data.get("AlarmConfiguration") is not None:
        import capo_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            capo_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    return out
