"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ExportDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.role_arn
    import capo_kinesis_analytics_v2.types.s3_prefix_location
    import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration
    import capo_kinesis_analytics_v2.types.storage_location_type


class ExportDestinationConfiguration(TypedDict, closed=True):
    destination_type: (
        "capo_kinesis_analytics_v2.types.storage_location_type.StorageLocationType"
    )
    """<p>The type of the destination location. The only supported value is <code>S3</code>.</p>"""
    export_role_arn: "capo_kinesis_analytics_v2.types.role_arn.RoleARN"
    """<p>The ARN of the IAM role that Managed Service for Apache Flink assumes to write the snapshot data to the destination location. For information about the permissions that this role requires, see <a href="https://docs.aws.amazon.com/managed-flink/latest/java/snapshots-import-export.html">Import and export</a>.</p>"""
    destination_encryption_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.SnapshotEncryptionConfiguration"
    ]
    """<p>The encryption configuration of the exported snapshot data. If you don't specify this parameter, Managed Service for Apache Flink uses a key of type <code>AWS_OWNED_KEY</code>. If you specify a KMS key, you must specify the key ARN.</p>"""
    destination_s3_prefix_location: (
        "capo_kinesis_analytics_v2.types.s3_prefix_location.S3PrefixLocation"
    )
    """<p>The Amazon S3 bucket and key prefix to export the snapshot data to. Managed Service for Apache Flink writes the data under a unique prefix that it appends to the key prefix that you specify. After the export completes, use <code>DescribeSnapshotOperation</code> to get the full prefix. The bucket must be owned by your account and must be in the same Region as the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportDestinationConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.storage_location_type

    out["DestinationType"] = (
        capo_kinesis_analytics_v2.types.storage_location_type.serialize_aws_json_1_1(
            value["destination_type"]
        )
    )
    out["ExportRoleArn"] = value["export_role_arn"]
    if "destination_encryption_configuration" in value:
        import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration

        out["DestinationEncryptionConfiguration"] = (
            capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.serialize_aws_json_1_1(
                value["destination_encryption_configuration"]
            )
        )
    import capo_kinesis_analytics_v2.types.s3_prefix_location

    out["DestinationS3PrefixLocation"] = (
        capo_kinesis_analytics_v2.types.s3_prefix_location.serialize_aws_json_1_1(
            value["destination_s3_prefix_location"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportDestinationConfiguration:
    out: ExportDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DestinationType") is not None:
        import capo_kinesis_analytics_v2.types.storage_location_type

        out["destination_type"] = (
            capo_kinesis_analytics_v2.types.storage_location_type.deserialize_aws_json_1_1(
                data["DestinationType"]
            )
        )
    else:
        import typing

        out["destination_type"] = typing.cast(
            "capo_kinesis_analytics_v2.types.storage_location_type.StorageLocationType",
            "",
        )
    if data.get("ExportRoleArn") is not None:
        out["export_role_arn"] = data["ExportRoleArn"]
    else:
        out["export_role_arn"] = ""
    if data.get("DestinationEncryptionConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration

        out["destination_encryption_configuration"] = (
            capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.deserialize_aws_json_1_1(
                data["DestinationEncryptionConfiguration"]
            )
        )
    if data.get("DestinationS3PrefixLocation") is not None:
        import capo_kinesis_analytics_v2.types.s3_prefix_location

        out["destination_s3_prefix_location"] = (
            capo_kinesis_analytics_v2.types.s3_prefix_location.deserialize_aws_json_1_1(
                data["DestinationS3PrefixLocation"]
            )
        )
    else:
        raise DeserializationError(
            "ExportDestinationConfiguration.destination_s3_prefix_location required"
        )
    return out
