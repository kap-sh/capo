"""Generated from Smithy shape ``com.amazonaws.s3tables#SchemaField``."""

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError


class SchemaField(TypedDict, closed=True):
    id: NotRequired["int"]
    """<p>An optional unique identifier for the schema field. Field IDs are used by Apache Iceberg to track schema evolution and maintain compatibility across schema changes. If not specified, S3 Tables automatically assigns field IDs.</p>"""
    name: "str"
    """<p>The name of the field.</p>"""
    type: "str"
    """<p>The field type. S3 Tables supports all Apache Iceberg primitive types. For more information, see the <a href="https://iceberg.apache.org/spec/#primitive-types">Apache Iceberg documentation</a>.</p>"""
    required: "bool"
    """<p>A Boolean value that specifies whether values are required for each row in this field. By default, this is <code>false</code> and null values are allowed in the field. If this is <code>true</code> the field does not allow null values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaField) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["required"] = value.get("required", False)
    return out


def deserialize_json(data: dict) -> SchemaField:
    out: SchemaField = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SchemaField.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SchemaField.type required")
    if data.get("required") is not None:
        out["required"] = data["required"]
    else:
        out["required"] = False
    return out
