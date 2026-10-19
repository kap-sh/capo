"""Generated from Smithy shape ``com.amazonaws.glue#IcebergPartitionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.column_name_string
    import capo_glue.types.iceberg_transform_string
    import capo_glue.types.integer


class IcebergPartitionField(TypedDict, closed=True):
    source_id: "capo_glue.types.integer.Integer"
    """<p>The identifier of the source field from the table schema that this partition field is based on.</p>"""
    transform: "capo_glue.types.iceberg_transform_string.IcebergTransformString"
    """<p>The transformation function applied to the source field to create the partition, such as identity, bucket, truncate, year, month, day, or hour.</p>"""
    name: "capo_glue.types.column_name_string.ColumnNameString"
    """<p>The name of the partition field as it will appear in the partitioned table structure.</p>"""
    field_id: "capo_glue.types.integer.Integer"
    """<p>The unique identifier assigned to this partition field within the Iceberg table's partition specification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergPartitionField) -> dict:
    out: dict = {}
    out["SourceId"] = value.get("source_id", 0)
    out["Transform"] = value["transform"]
    out["Name"] = value["name"]
    out["FieldId"] = value.get("field_id", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergPartitionField:
    out: IcebergPartitionField = {}  # type: ignore[typeddict-item]
    if data.get("SourceId") is not None:
        out["source_id"] = data["SourceId"]
    else:
        out["source_id"] = 0
    if data.get("Transform") is not None:
        out["transform"] = data["Transform"]
    else:
        out["transform"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = 0
    return out
