"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergPartitionField``."""

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError


class IcebergPartitionField(TypedDict, closed=True):
    source_id: "int"
    """<p>The ID of the source schema field to partition by. This must reference a valid field ID from the table schema.</p>"""
    transform: "str"
    """<p>The partition transform to apply to the source field. Supported transforms include <code>identity</code>, <code>year</code>, <code>month</code>, <code>day</code>, <code>hour</code>, <code>bucket</code>, and <code>truncate</code>. For more information, see the <a href="https://iceberg.apache.org/spec/#partition-transforms">Apache Iceberg partition transforms documentation</a>.</p>"""
    name: "str"
    """<p>The name for this partition field. This name is used in the partitioned file paths.</p>"""
    field_id: NotRequired["int"]
    """<p>An optional unique identifier for this partition field. If not specified, S3 Tables automatically assigns a field ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergPartitionField) -> dict:
    out: dict = {}
    out["source-id"] = value["source_id"]
    out["transform"] = value["transform"]
    out["name"] = value["name"]
    if "field_id" in value:
        out["field-id"] = value["field_id"]
    return out


def deserialize_json(data: dict) -> IcebergPartitionField:
    out: IcebergPartitionField = {}  # type: ignore[typeddict-item]
    if data.get("source-id") is not None:
        out["source_id"] = data["source-id"]
    else:
        raise DeserializationError("IcebergPartitionField.source_id required")
    if data.get("transform") is not None:
        out["transform"] = data["transform"]
    else:
        raise DeserializationError("IcebergPartitionField.transform required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("IcebergPartitionField.name required")
    if data.get("field-id") is not None:
        out["field_id"] = data["field-id"]
    return out
