"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowRunCommandParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_watch_output_config
    import capo_ssm.types.comment
    import capo_ssm.types.document_hash
    import capo_ssm.types.document_hash_type
    import capo_ssm.types.document_version
    import capo_ssm.types.notification_config
    import capo_ssm.types.parameters
    import capo_ssm.types.s3_bucket_name
    import capo_ssm.types.s3_key_prefix
    import capo_ssm.types.service_role
    import capo_ssm.types.timeout_seconds


class MaintenanceWindowRunCommandParameters(TypedDict, closed=True):
    comment: NotRequired["capo_ssm.types.comment.Comment"]
    """<p>Information about the commands to run.</p>"""
    cloud_watch_output_config: NotRequired[
        "capo_ssm.types.cloud_watch_output_config.CloudWatchOutputConfig"
    ]
    document_hash: NotRequired["capo_ssm.types.document_hash.DocumentHash"]
    """<p>The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.</p>"""
    document_hash_type: NotRequired[
        "capo_ssm.types.document_hash_type.DocumentHashType"
    ]
    """<p>SHA-256 or SHA-1. SHA-1 hashes have been deprecated.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    r"""<p>The Amazon Web Services Systems Manager document (SSM document) version to use in the request. You can specify <code>$DEFAULT</code>, <code>$LATEST</code>, or a specific version number. If you run commands by using the Amazon Web Services CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don't need to use the backslash. For example:</p> <p> <code>--document-version "\$DEFAULT"</code> </p> <p> <code>--document-version "\$LATEST"</code> </p> <p> <code>--document-version "3"</code> </p>"""
    notification_config: NotRequired[
        "capo_ssm.types.notification_config.NotificationConfig"
    ]
    """<p>Configurations for sending notifications about command status changes on a per-managed node basis.</p>"""
    output_s3_bucket_name: NotRequired["capo_ssm.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the Amazon Simple Storage Service (Amazon S3) bucket.</p>"""
    output_s3_key_prefix: NotRequired["capo_ssm.types.s3_key_prefix.S3KeyPrefix"]
    """<p>The S3 bucket subfolder.</p>"""
    parameters: NotRequired["capo_ssm.types.parameters.Parameters"]
    """<p>The parameters for the <code>RUN_COMMAND</code> task execution.</p>"""
    service_role_arn: NotRequired["capo_ssm.types.service_role.ServiceRole"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role for Amazon Web Services Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run <code>RegisterTaskWithMaintenanceWindow</code>.</p> <p>However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html">Setting up Maintenance Windows</a> in the in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    timeout_seconds: NotRequired["capo_ssm.types.timeout_seconds.TimeoutSeconds"]
    """<p>If this time is reached and the command hasn't already started running, it doesn't run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowRunCommandParameters) -> dict:
    out: dict = {}
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "cloud_watch_output_config" in value:
        import capo_ssm.types.cloud_watch_output_config

        out["CloudWatchOutputConfig"] = (
            capo_ssm.types.cloud_watch_output_config.serialize_aws_json_1_1(
                value["cloud_watch_output_config"]
            )
        )
    if "document_hash" in value:
        out["DocumentHash"] = value["document_hash"]
    if "document_hash_type" in value:
        import capo_ssm.types.document_hash_type

        out["DocumentHashType"] = (
            capo_ssm.types.document_hash_type.serialize_aws_json_1_1(
                value["document_hash_type"]
            )
        )
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "notification_config" in value:
        import capo_ssm.types.notification_config

        out["NotificationConfig"] = (
            capo_ssm.types.notification_config.serialize_aws_json_1_1(
                value["notification_config"]
            )
        )
    if "output_s3_bucket_name" in value:
        out["OutputS3BucketName"] = value["output_s3_bucket_name"]
    if "output_s3_key_prefix" in value:
        out["OutputS3KeyPrefix"] = value["output_s3_key_prefix"]
    if "parameters" in value:
        import capo_ssm.types.parameters

        out["Parameters"] = capo_ssm.types.parameters.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "service_role_arn" in value:
        out["ServiceRoleArn"] = value["service_role_arn"]
    if "timeout_seconds" in value:
        out["TimeoutSeconds"] = value["timeout_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowRunCommandParameters:
    out: MaintenanceWindowRunCommandParameters = {}  # type: ignore[typeddict-item]
    if data.get("Comment") is not None:
        out["comment"] = data["Comment"]
    if data.get("CloudWatchOutputConfig") is not None:
        import capo_ssm.types.cloud_watch_output_config

        out["cloud_watch_output_config"] = (
            capo_ssm.types.cloud_watch_output_config.deserialize_aws_json_1_1(
                data["CloudWatchOutputConfig"]
            )
        )
    if data.get("DocumentHash") is not None:
        out["document_hash"] = data["DocumentHash"]
    if data.get("DocumentHashType") is not None:
        import capo_ssm.types.document_hash_type

        out["document_hash_type"] = (
            capo_ssm.types.document_hash_type.deserialize_aws_json_1_1(
                data["DocumentHashType"]
            )
        )
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("NotificationConfig") is not None:
        import capo_ssm.types.notification_config

        out["notification_config"] = (
            capo_ssm.types.notification_config.deserialize_aws_json_1_1(
                data["NotificationConfig"]
            )
        )
    if data.get("OutputS3BucketName") is not None:
        out["output_s3_bucket_name"] = data["OutputS3BucketName"]
    if data.get("OutputS3KeyPrefix") is not None:
        out["output_s3_key_prefix"] = data["OutputS3KeyPrefix"]
    if data.get("Parameters") is not None:
        import capo_ssm.types.parameters

        out["parameters"] = capo_ssm.types.parameters.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if data.get("ServiceRoleArn") is not None:
        out["service_role_arn"] = data["ServiceRoleArn"]
    if data.get("TimeoutSeconds") is not None:
        out["timeout_seconds"] = data["TimeoutSeconds"]
    return out
