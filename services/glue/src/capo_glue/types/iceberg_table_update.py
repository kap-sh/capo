"""Generated from Smithy shape ``com.amazonaws.glue#IcebergTableUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.encryption_key_id_string
    import capo_glue.types.iceberg_encrypted_key
    import capo_glue.types.iceberg_partition_spec
    import capo_glue.types.iceberg_schema
    import capo_glue.types.iceberg_sort_order
    import capo_glue.types.iceberg_update_action
    import capo_glue.types.location_string
    import capo_glue.types.string_to_string_map


class IcebergTableUpdate(TypedDict, closed=True):
    schema: "capo_glue.types.iceberg_schema.IcebergSchema"
    """<p>The updated schema definition for the Iceberg table, specifying any changes to field structure, data types, or schema metadata.</p>"""
    partition_spec: NotRequired[
        "capo_glue.types.iceberg_partition_spec.IcebergPartitionSpec"
    ]
    """<p>The updated partitioning specification that defines how the table data should be reorganized and partitioned.</p>"""
    sort_order: NotRequired["capo_glue.types.iceberg_sort_order.IcebergSortOrder"]
    """<p>The updated sort order specification that defines how data should be ordered within partitions for optimal query performance.</p>"""
    location: "capo_glue.types.location_string.LocationString"
    """<p>The updated S3 location where the Iceberg table data will be stored.</p>"""
    properties: NotRequired["capo_glue.types.string_to_string_map.StringToStringMap"]
    """<p>Updated key-value pairs of table properties and configuration settings for the Iceberg table.</p>"""
    action: NotRequired["capo_glue.types.iceberg_update_action.IcebergUpdateAction"]
    """<p>The type of update action to be performed on the Iceberg table. Defines the specific operation such as adding schema, setting current schema, adding partition spec, or managing encryption keys.</p>"""
    encryption_key: NotRequired[
        "capo_glue.types.iceberg_encrypted_key.IcebergEncryptedKey"
    ]
    """<p>Encryption key information associated with an Iceberg table update operation. Used when adding or removing encryption keys from the table metadata during table evolution.</p>"""
    key_id: NotRequired[
        "capo_glue.types.encryption_key_id_string.EncryptionKeyIdString"
    ]
    """<p>Identifier of the encryption key involved in an Iceberg table update operation. References the specific key being added to or removed from the table's encryption configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergTableUpdate) -> dict:
    out: dict = {}
    import capo_glue.types.iceberg_schema

    out["Schema"] = capo_glue.types.iceberg_schema.serialize_aws_json_1_1(
        value["schema"]
    )
    if "partition_spec" in value:
        import capo_glue.types.iceberg_partition_spec

        out["PartitionSpec"] = (
            capo_glue.types.iceberg_partition_spec.serialize_aws_json_1_1(
                value["partition_spec"]
            )
        )
    if "sort_order" in value:
        import capo_glue.types.iceberg_sort_order

        out["SortOrder"] = capo_glue.types.iceberg_sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    out["Location"] = value["location"]
    if "properties" in value:
        import capo_glue.types.string_to_string_map

        out["Properties"] = capo_glue.types.string_to_string_map.serialize_aws_json_1_1(
            value["properties"]
        )
    if "action" in value:
        import capo_glue.types.iceberg_update_action

        out["Action"] = capo_glue.types.iceberg_update_action.serialize_aws_json_1_1(
            value["action"]
        )
    if "encryption_key" in value:
        import capo_glue.types.iceberg_encrypted_key

        out["EncryptionKey"] = (
            capo_glue.types.iceberg_encrypted_key.serialize_aws_json_1_1(
                value["encryption_key"]
            )
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergTableUpdate:
    out: IcebergTableUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Schema") is not None:
        import capo_glue.types.iceberg_schema

        out["schema"] = capo_glue.types.iceberg_schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    else:
        raise DeserializationError("IcebergTableUpdate.schema required")
    if data.get("PartitionSpec") is not None:
        import capo_glue.types.iceberg_partition_spec

        out["partition_spec"] = (
            capo_glue.types.iceberg_partition_spec.deserialize_aws_json_1_1(
                data["PartitionSpec"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_glue.types.iceberg_sort_order

        out["sort_order"] = capo_glue.types.iceberg_sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    else:
        out["location"] = ""
    if data.get("Properties") is not None:
        import capo_glue.types.string_to_string_map

        out["properties"] = (
            capo_glue.types.string_to_string_map.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if data.get("Action") is not None:
        import capo_glue.types.iceberg_update_action

        out["action"] = capo_glue.types.iceberg_update_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if data.get("EncryptionKey") is not None:
        import capo_glue.types.iceberg_encrypted_key

        out["encryption_key"] = (
            capo_glue.types.iceberg_encrypted_key.deserialize_aws_json_1_1(
                data["EncryptionKey"]
            )
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    return out
