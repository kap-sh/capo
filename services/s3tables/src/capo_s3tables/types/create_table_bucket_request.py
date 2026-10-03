"""Generated from Smithy shape ``com.amazonaws.s3tables#CreateTableBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.encryption_configuration
    import capo_s3tables.types.storage_class_configuration
    import capo_s3tables.types.table_bucket_name
    import capo_s3tables.types.tags


class CreateTableBucketRequest(TypedDict, closed=True):
    name: "capo_s3tables.types.table_bucket_name.TableBucketName"
    """<p>The name for the table bucket.</p>"""
    encryption_configuration: NotRequired[
        "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration to use for the table bucket. This configuration specifies the default encryption settings that will be applied to all tables created in this bucket unless overridden at the table level. The configuration includes the encryption algorithm and, if using SSE-KMS, the KMS key to use.</p>"""
    storage_class_configuration: NotRequired[
        "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
    ]
    """<p>The default storage class configuration for the table bucket. This configuration will be applied to all new tables created in this bucket unless overridden at the table level. If not specified, the service default storage class will be used.</p>"""
    tags: NotRequired["capo_s3tables.types.tags.Tags"]
    """<p>A map of user-defined tags that you would like to apply to the table bucket that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTableBucket</code> permisson to create a table bucket with tags.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTableBucketRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "encryption_configuration" in value:
        import capo_s3tables.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_s3tables.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "storage_class_configuration" in value:
        import capo_s3tables.types.storage_class_configuration

        out["storageClassConfiguration"] = (
            capo_s3tables.types.storage_class_configuration.serialize_json(
                value["storage_class_configuration"]
            )
        )
    if "tags" in value:
        import capo_s3tables.types.tags

        out["tags"] = capo_s3tables.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTableBucketRequest:
    out: CreateTableBucketRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateTableBucketRequest.name required")
    if data.get("encryptionConfiguration") is not None:
        import capo_s3tables.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_s3tables.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("storageClassConfiguration") is not None:
        import capo_s3tables.types.storage_class_configuration

        out["storage_class_configuration"] = (
            capo_s3tables.types.storage_class_configuration.deserialize_json(
                data["storageClassConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_s3tables.types.tags

        out["tags"] = capo_s3tables.types.tags.deserialize_json(data["tags"])
    return out
