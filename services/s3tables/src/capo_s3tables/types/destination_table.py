"""Generated from Smithy shape ``com.amazonaws.s3tables#DestinationTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.encryption_configuration
    import capo_s3tables.types.iceberg_schema_v2
    import capo_s3tables.types.iceberg_sort_order
    import capo_s3tables.types.migration_table_properties
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.storage_class_configuration
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_name
    import capo_s3tables.types.tags


class DestinationTable(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket to create the table in.</p>"""
    namespace: "capo_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace to create the table in.</p>"""
    name: "capo_s3tables.types.table_name.TableName"
    """<p>The name of the table to create.</p>"""
    encryption_configuration: NotRequired[
        "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for the table. If you don't specify one, the table uses the default encryption configuration of its table bucket. If you specify an encryption configuration, the migration role must have the <code>s3tables:PutTableEncryption</code> permission. If you choose SSE-KMS, the migration role must have the <code>kms:DescribeKey</code>, <code>kms:GenerateDataKey</code> and <code>kms:Decrypt</code> permissions on the KMS key, and the S3 Tables maintenance principal must have access to it. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p>"""
    storage_class_configuration: NotRequired[
        "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
    ]
    """<p>The storage class configuration for the table. If you don't specify one, the table inherits the storage class configuration of its table bucket. If you specify a storage class configuration, the migration role must have the <code>s3tables:PutTableStorageClass</code> permission.</p>"""
    tags: NotRequired["capo_s3tables.types.tags.Tags"]
    """<p>The tags to add to the table. A tag is a key-value pair that you apply to your resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>. If you specify tags, the migration role must have the <code>s3tables:TagResource</code> permission.</p>"""
    properties: NotRequired[
        "capo_s3tables.types.migration_table_properties.MigrationTableProperties"
    ]
    """<p>The properties of the destination table, such as its Iceberg format version and the format of its data files.</p>"""
    schema: NotRequired["capo_s3tables.types.iceberg_schema_v2.IcebergSchemaV2"]
    """<p>The schema of the table to create. If you don't specify a schema, the migration infers it from the source table, with every column optional. A schema that you specify must include every partition column of the source table. It can leave out other columns only if <code>unmatchedSourceFieldsPolicy</code> is <code>drop</code>. A struct column must have the same fields as the source column. Column default values aren't supported. If you mark a column as required, every source object must have a value for it: an object with a null value in a required column fails to migrate. The destination table is partitioned in the same way as the source table. To specify fields in <code>icebergSortOrder</code>, you must specify a schema.</p>"""
    iceberg_sort_order: NotRequired[
        "capo_s3tables.types.iceberg_sort_order.IcebergSortOrder"
    ]
    """<p>The sort order of the rows within each data file that the migration writes. A sort order can have up to five fields, each naming a column of the schema that you specify by its field ID, so to use a sort order you must specify a schema. <code>StartTableMigration</code> rejects a field that names no column of the schema, or whose transform doesn't fit the column's type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationTable) -> dict:
    out: dict = {}
    out["tableBucketARN"] = value["table_bucket_arn"]
    out["namespace"] = value["namespace"]
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
    if "properties" in value:
        import capo_s3tables.types.migration_table_properties

        out["properties"] = (
            capo_s3tables.types.migration_table_properties.serialize_json(
                value["properties"]
            )
        )
    if "schema" in value:
        import capo_s3tables.types.iceberg_schema_v2

        out["schema"] = capo_s3tables.types.iceberg_schema_v2.serialize_json(
            value["schema"]
        )
    if "iceberg_sort_order" in value:
        import capo_s3tables.types.iceberg_sort_order

        out["icebergSortOrder"] = capo_s3tables.types.iceberg_sort_order.serialize_json(
            value["iceberg_sort_order"]
        )
    return out


def deserialize_json(data: dict) -> DestinationTable:
    out: DestinationTable = {}  # type: ignore[typeddict-item]
    if data.get("tableBucketARN") is not None:
        out["table_bucket_arn"] = data["tableBucketARN"]
    else:
        out["table_bucket_arn"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        out["namespace"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
    if data.get("properties") is not None:
        import capo_s3tables.types.migration_table_properties

        out["properties"] = (
            capo_s3tables.types.migration_table_properties.deserialize_json(
                data["properties"]
            )
        )
    if data.get("schema") is not None:
        import capo_s3tables.types.iceberg_schema_v2

        out["schema"] = capo_s3tables.types.iceberg_schema_v2.deserialize_json(
            data["schema"]
        )
    if data.get("icebergSortOrder") is not None:
        import capo_s3tables.types.iceberg_sort_order

        out["iceberg_sort_order"] = (
            capo_s3tables.types.iceberg_sort_order.deserialize_json(
                data["icebergSortOrder"]
            )
        )
    return out
