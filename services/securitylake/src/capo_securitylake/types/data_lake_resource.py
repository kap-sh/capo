"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securitylake.types.amazon_resource_name
    import capo_securitylake.types.data_lake_encryption_configuration
    import capo_securitylake.types.data_lake_lifecycle_configuration
    import capo_securitylake.types.data_lake_replication_configuration
    import capo_securitylake.types.data_lake_status
    import capo_securitylake.types.data_lake_update_status
    import capo_securitylake.types.region
    import capo_securitylake.types.s3_bucket_arn


class DataLakeResource(TypedDict, closed=True):
    data_lake_arn: "capo_securitylake.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) created by you to provide to the subscriber. For more information about ARNs and how to use them in policies, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html">Amazon Security Lake User Guide</a>.</p>"""
    region: "capo_securitylake.types.region.Region"
    """<p>The Amazon Web Services Regions where Security Lake is enabled.</p>"""
    s3_bucket_arn: NotRequired["capo_securitylake.types.s3_bucket_arn.S3BucketArn"]
    """<p>The ARN for the Amazon Security Lake Amazon S3 bucket.</p>"""
    encryption_configuration: NotRequired[
        "capo_securitylake.types.data_lake_encryption_configuration.DataLakeEncryptionConfiguration"
    ]
    """<p>Provides encryption details of Amazon Security Lake object.</p>"""
    lifecycle_configuration: NotRequired[
        "capo_securitylake.types.data_lake_lifecycle_configuration.DataLakeLifecycleConfiguration"
    ]
    """<p>Provides lifecycle details of Amazon Security Lake object.</p>"""
    replication_configuration: NotRequired[
        "capo_securitylake.types.data_lake_replication_configuration.DataLakeReplicationConfiguration"
    ]
    """<p>Provides replication details of Amazon Security Lake object.</p>"""
    create_status: NotRequired[
        "capo_securitylake.types.data_lake_status.DataLakeStatus"
    ]
    """<p>Retrieves the status of the <code>CreateDatalake</code> API call for an account in Amazon Security Lake.</p>"""
    update_status: NotRequired[
        "capo_securitylake.types.data_lake_update_status.DataLakeUpdateStatus"
    ]
    """<p>The status of the last <code>UpdateDataLake </code>or <code>DeleteDataLake</code> API request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeResource) -> dict:
    out: dict = {}
    out["dataLakeArn"] = value["data_lake_arn"]
    out["region"] = value["region"]
    if "s3_bucket_arn" in value:
        out["s3BucketArn"] = value["s3_bucket_arn"]
    if "encryption_configuration" in value:
        import capo_securitylake.types.data_lake_encryption_configuration

        out["encryptionConfiguration"] = (
            capo_securitylake.types.data_lake_encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "lifecycle_configuration" in value:
        import capo_securitylake.types.data_lake_lifecycle_configuration

        out["lifecycleConfiguration"] = (
            capo_securitylake.types.data_lake_lifecycle_configuration.serialize_json(
                value["lifecycle_configuration"]
            )
        )
    if "replication_configuration" in value:
        import capo_securitylake.types.data_lake_replication_configuration

        out["replicationConfiguration"] = (
            capo_securitylake.types.data_lake_replication_configuration.serialize_json(
                value["replication_configuration"]
            )
        )
    if "create_status" in value:
        import capo_securitylake.types.data_lake_status

        out["createStatus"] = capo_securitylake.types.data_lake_status.serialize_json(
            value["create_status"]
        )
    if "update_status" in value:
        import capo_securitylake.types.data_lake_update_status

        out["updateStatus"] = (
            capo_securitylake.types.data_lake_update_status.serialize_json(
                value["update_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeResource:
    out: DataLakeResource = {}  # type: ignore[typeddict-item]
    if data.get("dataLakeArn") is not None:
        out["data_lake_arn"] = data["dataLakeArn"]
    else:
        raise DeserializationError("DataLakeResource.data_lake_arn required")
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        raise DeserializationError("DataLakeResource.region required")
    if data.get("s3BucketArn") is not None:
        out["s3_bucket_arn"] = data["s3BucketArn"]
    if data.get("encryptionConfiguration") is not None:
        import capo_securitylake.types.data_lake_encryption_configuration

        out["encryption_configuration"] = (
            capo_securitylake.types.data_lake_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("lifecycleConfiguration") is not None:
        import capo_securitylake.types.data_lake_lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_securitylake.types.data_lake_lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    if data.get("replicationConfiguration") is not None:
        import capo_securitylake.types.data_lake_replication_configuration

        out["replication_configuration"] = (
            capo_securitylake.types.data_lake_replication_configuration.deserialize_json(
                data["replicationConfiguration"]
            )
        )
    if data.get("createStatus") is not None:
        import capo_securitylake.types.data_lake_status

        out["create_status"] = (
            capo_securitylake.types.data_lake_status.deserialize_json(
                data["createStatus"]
            )
        )
    if data.get("updateStatus") is not None:
        import capo_securitylake.types.data_lake_update_status

        out["update_status"] = (
            capo_securitylake.types.data_lake_update_status.deserialize_json(
                data["updateStatus"]
            )
        )
    return out
