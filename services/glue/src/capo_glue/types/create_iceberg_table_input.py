"""Generated from Smithy shape ``com.amazonaws.glue#CreateIcebergTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.iceberg_partition_spec
    import capo_glue.types.iceberg_schema
    import capo_glue.types.iceberg_sort_order
    import capo_glue.types.location_string
    import capo_glue.types.string_to_string_map


class CreateIcebergTableInput(TypedDict, closed=True):
    location: "capo_glue.types.location_string.LocationString"
    """<p>The S3 location where the Iceberg table data will be stored.</p>"""
    schema: "capo_glue.types.iceberg_schema.IcebergSchema"
    """<p>The schema definition that specifies the structure, field types, and metadata for the Iceberg table.</p>"""
    partition_spec: NotRequired[
        "capo_glue.types.iceberg_partition_spec.IcebergPartitionSpec"
    ]
    """<p>The partitioning specification that defines how the Iceberg table data will be organized and partitioned for optimal query performance.</p>"""
    write_order: NotRequired["capo_glue.types.iceberg_sort_order.IcebergSortOrder"]
    """<p>The sort order specification that defines how data should be ordered within each partition to optimize query performance.</p>"""
    properties: NotRequired["capo_glue.types.string_to_string_map.StringToStringMap"]
    """<p>Key-value pairs of additional table properties and configuration settings for the Iceberg table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIcebergTableInput) -> dict:
    out: dict = {}
    out["Location"] = value["location"]
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
    if "write_order" in value:
        import capo_glue.types.iceberg_sort_order

        out["WriteOrder"] = capo_glue.types.iceberg_sort_order.serialize_aws_json_1_1(
            value["write_order"]
        )
    if "properties" in value:
        import capo_glue.types.string_to_string_map

        out["Properties"] = capo_glue.types.string_to_string_map.serialize_aws_json_1_1(
            value["properties"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIcebergTableInput:
    out: CreateIcebergTableInput = {}  # type: ignore[typeddict-item]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    else:
        out["location"] = ""
    if data.get("Schema") is not None:
        import capo_glue.types.iceberg_schema

        out["schema"] = capo_glue.types.iceberg_schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    else:
        raise DeserializationError("CreateIcebergTableInput.schema required")
    if data.get("PartitionSpec") is not None:
        import capo_glue.types.iceberg_partition_spec

        out["partition_spec"] = (
            capo_glue.types.iceberg_partition_spec.deserialize_aws_json_1_1(
                data["PartitionSpec"]
            )
        )
    if data.get("WriteOrder") is not None:
        import capo_glue.types.iceberg_sort_order

        out["write_order"] = (
            capo_glue.types.iceberg_sort_order.deserialize_aws_json_1_1(
                data["WriteOrder"]
            )
        )
    if data.get("Properties") is not None:
        import capo_glue.types.string_to_string_map

        out["properties"] = (
            capo_glue.types.string_to_string_map.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
