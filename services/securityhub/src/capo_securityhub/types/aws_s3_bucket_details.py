"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_account_public_access_block_details
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details
    import capo_securityhub.types.aws_s3_bucket_bucket_versioning_configuration
    import capo_securityhub.types.aws_s3_bucket_logging_configuration
    import capo_securityhub.types.aws_s3_bucket_notification_configuration
    import capo_securityhub.types.aws_s3_bucket_object_lock_configuration
    import capo_securityhub.types.aws_s3_bucket_server_side_encryption_configuration
    import capo_securityhub.types.aws_s3_bucket_website_configuration
    import capo_securityhub.types.non_empty_string


class AwsS3BucketDetails(TypedDict, closed=True):
    owner_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The canonical user ID of the owner of the S3 bucket.</p>"""
    owner_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The display name of the owner of the S3 bucket.</p>"""
    owner_account_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account identifier of the account that owns the S3 bucket.</p>"""
    created_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the S3 bucket was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_server_side_encryption_configuration.AwsS3BucketServerSideEncryptionConfiguration"
    ]
    """<p>The encryption rules that are applied to the S3 bucket.</p>"""
    bucket_lifecycle_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details.AwsS3BucketBucketLifecycleConfigurationDetails"
    ]
    """<p>The lifecycle configuration for objects in the specified bucket.</p>"""
    public_access_block_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_account_public_access_block_details.AwsS3AccountPublicAccessBlockDetails"
    ]
    """<p>Provides information about the Amazon S3 Public Access Block configuration for the S3 bucket.</p>"""
    access_control_list: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The access control list for the S3 bucket.</p>"""
    bucket_logging_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_logging_configuration.AwsS3BucketLoggingConfiguration"
    ]
    """<p>The logging configuration for the S3 bucket.</p>"""
    bucket_website_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_website_configuration.AwsS3BucketWebsiteConfiguration"
    ]
    """<p>The website configuration parameters for the S3 bucket.</p>"""
    bucket_notification_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_notification_configuration.AwsS3BucketNotificationConfiguration"
    ]
    """<p>The notification configuration for the S3 bucket.</p>"""
    bucket_versioning_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_bucket_versioning_configuration.AwsS3BucketBucketVersioningConfiguration"
    ]
    """<p>The versioning state of an S3 bucket.</p>"""
    object_lock_configuration: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_object_lock_configuration.AwsS3BucketObjectLockConfiguration"
    ]
    """<p> Specifies which rule Amazon S3 applies by default to every new object placed in the bucket. </p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the bucket. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketDetails) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "owner_name" in value:
        out["OwnerName"] = value["owner_name"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "server_side_encryption_configuration" in value:
        import capo_securityhub.types.aws_s3_bucket_server_side_encryption_configuration

        out["ServerSideEncryptionConfiguration"] = (
            capo_securityhub.types.aws_s3_bucket_server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "bucket_lifecycle_configuration" in value:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details

        out["BucketLifecycleConfiguration"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details.serialize_json(
                value["bucket_lifecycle_configuration"]
            )
        )
    if "public_access_block_configuration" in value:
        import capo_securityhub.types.aws_s3_account_public_access_block_details

        out["PublicAccessBlockConfiguration"] = (
            capo_securityhub.types.aws_s3_account_public_access_block_details.serialize_json(
                value["public_access_block_configuration"]
            )
        )
    if "access_control_list" in value:
        out["AccessControlList"] = value["access_control_list"]
    if "bucket_logging_configuration" in value:
        import capo_securityhub.types.aws_s3_bucket_logging_configuration

        out["BucketLoggingConfiguration"] = (
            capo_securityhub.types.aws_s3_bucket_logging_configuration.serialize_json(
                value["bucket_logging_configuration"]
            )
        )
    if "bucket_website_configuration" in value:
        import capo_securityhub.types.aws_s3_bucket_website_configuration

        out["BucketWebsiteConfiguration"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration.serialize_json(
                value["bucket_website_configuration"]
            )
        )
    if "bucket_notification_configuration" in value:
        import capo_securityhub.types.aws_s3_bucket_notification_configuration

        out["BucketNotificationConfiguration"] = (
            capo_securityhub.types.aws_s3_bucket_notification_configuration.serialize_json(
                value["bucket_notification_configuration"]
            )
        )
    if "bucket_versioning_configuration" in value:
        import capo_securityhub.types.aws_s3_bucket_bucket_versioning_configuration

        out["BucketVersioningConfiguration"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_versioning_configuration.serialize_json(
                value["bucket_versioning_configuration"]
            )
        )
    if "object_lock_configuration" in value:
        import capo_securityhub.types.aws_s3_bucket_object_lock_configuration

        out["ObjectLockConfiguration"] = (
            capo_securityhub.types.aws_s3_bucket_object_lock_configuration.serialize_json(
                value["object_lock_configuration"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketDetails:
    out: AwsS3BucketDetails = {}  # type: ignore[typeddict-item]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    if data.get("OwnerName") is not None:
        out["owner_name"] = data["OwnerName"]
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("CreatedAt") is not None:
        out["created_at"] = data["CreatedAt"]
    if data.get("ServerSideEncryptionConfiguration") is not None:
        import capo_securityhub.types.aws_s3_bucket_server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_securityhub.types.aws_s3_bucket_server_side_encryption_configuration.deserialize_json(
                data["ServerSideEncryptionConfiguration"]
            )
        )
    if data.get("BucketLifecycleConfiguration") is not None:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details

        out["bucket_lifecycle_configuration"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details.deserialize_json(
                data["BucketLifecycleConfiguration"]
            )
        )
    if data.get("PublicAccessBlockConfiguration") is not None:
        import capo_securityhub.types.aws_s3_account_public_access_block_details

        out["public_access_block_configuration"] = (
            capo_securityhub.types.aws_s3_account_public_access_block_details.deserialize_json(
                data["PublicAccessBlockConfiguration"]
            )
        )
    if data.get("AccessControlList") is not None:
        out["access_control_list"] = data["AccessControlList"]
    if data.get("BucketLoggingConfiguration") is not None:
        import capo_securityhub.types.aws_s3_bucket_logging_configuration

        out["bucket_logging_configuration"] = (
            capo_securityhub.types.aws_s3_bucket_logging_configuration.deserialize_json(
                data["BucketLoggingConfiguration"]
            )
        )
    if data.get("BucketWebsiteConfiguration") is not None:
        import capo_securityhub.types.aws_s3_bucket_website_configuration

        out["bucket_website_configuration"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration.deserialize_json(
                data["BucketWebsiteConfiguration"]
            )
        )
    if data.get("BucketNotificationConfiguration") is not None:
        import capo_securityhub.types.aws_s3_bucket_notification_configuration

        out["bucket_notification_configuration"] = (
            capo_securityhub.types.aws_s3_bucket_notification_configuration.deserialize_json(
                data["BucketNotificationConfiguration"]
            )
        )
    if data.get("BucketVersioningConfiguration") is not None:
        import capo_securityhub.types.aws_s3_bucket_bucket_versioning_configuration

        out["bucket_versioning_configuration"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_versioning_configuration.deserialize_json(
                data["BucketVersioningConfiguration"]
            )
        )
    if data.get("ObjectLockConfiguration") is not None:
        import capo_securityhub.types.aws_s3_bucket_object_lock_configuration

        out["object_lock_configuration"] = (
            capo_securityhub.types.aws_s3_bucket_object_lock_configuration.deserialize_json(
                data["ObjectLockConfiguration"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
