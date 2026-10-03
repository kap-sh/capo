"""Generated from Smithy shape ``com.amazonaws.s3tables#CreateTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.encryption_configuration
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.open_table_format
    import capo_s3tables.types.storage_class_configuration
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_metadata
    import capo_s3tables.types.table_name
    import capo_s3tables.types.tags


class CreateTableRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket to create the table in.</p>"""
    namespace: "capo_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace to associated with the table.</p>"""
    name: "capo_s3tables.types.table_name.TableName"
    """<p>The name for the table.</p>"""
    format: "capo_s3tables.types.open_table_format.OpenTableFormat"
    """<p>The format for the table.</p>"""
    metadata: NotRequired["capo_s3tables.types.table_metadata.TableMetadata"]
    """<p>The metadata for the table.</p>"""
    encryption_configuration: NotRequired[
        "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration to use for the table. This configuration specifies the encryption algorithm and, if using SSE-KMS, the KMS key to use for encrypting the table. </p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p> </note>"""
    storage_class_configuration: NotRequired[
        "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
    ]
    """<p>The storage class configuration for the table. If not specified, the table inherits the storage class configuration from its table bucket. Specify this parameter to override the bucket's default storage class for this table.</p>"""
    tags: NotRequired["capo_s3tables.types.tags.Tags"]
    """<p>A map of user-defined tags that you would like to apply to the table that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs for, and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission to create a table with tags.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTableRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_s3tables.types.open_table_format

    out["format"] = capo_s3tables.types.open_table_format.serialize_json(
        value["format"]
    )
    if "metadata" in value:
        import capo_s3tables.types.table_metadata

        out["metadata"] = capo_s3tables.types.table_metadata.serialize_json(
            value["metadata"]
        )
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


def deserialize_json(data: dict) -> CreateTableRequest:
    out: CreateTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateTableRequest.name required")
    if data.get("format") is not None:
        import capo_s3tables.types.open_table_format

        out["format"] = capo_s3tables.types.open_table_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("CreateTableRequest.format required")
    if data.get("metadata") is not None:
        import capo_s3tables.types.table_metadata

        out["metadata"] = capo_s3tables.types.table_metadata.deserialize_json(
            data["metadata"]
        )
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
