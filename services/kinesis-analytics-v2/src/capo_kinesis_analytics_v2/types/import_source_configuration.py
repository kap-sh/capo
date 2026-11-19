"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ImportSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.role_arn
    import capo_kinesis_analytics_v2.types.s3_prefix_location
    import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration
    import capo_kinesis_analytics_v2.types.storage_location_type


class ImportSourceConfiguration(TypedDict, closed=True):
    source_type: (
        "capo_kinesis_analytics_v2.types.storage_location_type.StorageLocationType"
    )
    """<p>The type of the source location. The only supported value is <code>S3</code>.</p>"""
    import_role_arn: "capo_kinesis_analytics_v2.types.role_arn.RoleARN"
    """<p>The ARN of the IAM role that Managed Service for Apache Flink assumes to read the savepoint data from the source location. For information about the permissions that this role requires, see <a href="https://docs.aws.amazon.com/managed-flink/latest/java/snapshots-import-export.html">Import and export</a>.</p>"""
    source_encryption_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.SnapshotEncryptionConfiguration"
    ]
    """<p>The encryption configuration of the savepoint data at the source location. If you don't specify this parameter, Managed Service for Apache Flink uses a key of type <code>AWS_OWNED_KEY</code>. If you specify a KMS key, you must specify the key ARN.</p>"""
    source_s3_prefix_location: (
        "capo_kinesis_analytics_v2.types.s3_prefix_location.S3PrefixLocation"
    )
    """<p>The Amazon S3 bucket and key prefix that contain the savepoint data to import. The bucket must be owned by your account and must be in the same Region as the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportSourceConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.storage_location_type

    out["SourceType"] = (
        capo_kinesis_analytics_v2.types.storage_location_type.serialize_aws_json_1_1(
            value["source_type"]
        )
    )
    out["ImportRoleArn"] = value["import_role_arn"]
    if "source_encryption_configuration" in value:
        import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration

        out["SourceEncryptionConfiguration"] = (
            capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.serialize_aws_json_1_1(
                value["source_encryption_configuration"]
            )
        )
    import capo_kinesis_analytics_v2.types.s3_prefix_location

    out["SourceS3PrefixLocation"] = (
        capo_kinesis_analytics_v2.types.s3_prefix_location.serialize_aws_json_1_1(
            value["source_s3_prefix_location"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportSourceConfiguration:
    out: ImportSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SourceType") is not None:
        import capo_kinesis_analytics_v2.types.storage_location_type

        out["source_type"] = (
            capo_kinesis_analytics_v2.types.storage_location_type.deserialize_aws_json_1_1(
                data["SourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_kinesis_analytics_v2.types.storage_location_type.StorageLocationType",
            "",
        )
    if data.get("ImportRoleArn") is not None:
        out["import_role_arn"] = data["ImportRoleArn"]
    else:
        out["import_role_arn"] = ""
    if data.get("SourceEncryptionConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration

        out["source_encryption_configuration"] = (
            capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.deserialize_aws_json_1_1(
                data["SourceEncryptionConfiguration"]
            )
        )
    if data.get("SourceS3PrefixLocation") is not None:
        import capo_kinesis_analytics_v2.types.s3_prefix_location

        out["source_s3_prefix_location"] = (
            capo_kinesis_analytics_v2.types.s3_prefix_location.deserialize_aws_json_1_1(
                data["SourceS3PrefixLocation"]
            )
        )
    else:
        raise DeserializationError(
            "ImportSourceConfiguration.source_s3_prefix_location required"
        )
    return out
