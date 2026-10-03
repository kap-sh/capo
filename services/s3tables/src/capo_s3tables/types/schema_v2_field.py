"""Generated from Smithy shape ``com.amazonaws.s3tables#SchemaV2Field``."""

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError


class SchemaV2Field(TypedDict, closed=True):
    id: "int"
    """<p>The unique identifier for the schema field. Field IDs are used by Apache Iceberg to track schema evolution and maintain compatibility across schema changes.</p>"""
    name: "str"
    """<p>The name of the field.</p>"""
    type: "object"
    """<p>The data type of the field. This can be a primitive type string such as <code>boolean</code>, <code>int</code>, <code>long</code>, <code>float</code>, <code>double</code>, <code>string</code>, <code>binary</code>, <code>date</code>, <code>timestamp</code>, or <code>timestamptz</code>, or a complex type represented as a JSON object for nested types such as <code>struct</code>, <code>list</code>, or <code>map</code>. For more information, see the <a href="https://iceberg.apache.org/spec/#schemas-and-data-types">Apache Iceberg schemas and data types documentation</a>.</p>"""
    required: "bool"
    """<p>A Boolean value that specifies whether values are required for each row in this field. If this is <code>true</code>, the field does not allow null values.</p>"""
    doc: NotRequired["str"]
    """<p>An optional description of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaV2Field) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["required"] = value["required"]
    if "doc" in value:
        out["doc"] = value["doc"]
    return out


def deserialize_json(data: dict) -> SchemaV2Field:
    out: SchemaV2Field = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SchemaV2Field.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SchemaV2Field.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SchemaV2Field.type required")
    if data.get("required") is not None:
        out["required"] = data["required"]
    else:
        raise DeserializationError("SchemaV2Field.required required")
    if data.get("doc") is not None:
        out["doc"] = data["doc"]
    return out
