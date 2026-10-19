"""Generated from Smithy shape ``com.amazonaws.glue#IcebergStructField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean
    import capo_glue.types.column_name_string
    import capo_glue.types.comment_string
    import capo_glue.types.iceberg_document
    import capo_glue.types.integer


class IcebergStructField(TypedDict, closed=True):
    id: "capo_glue.types.integer.Integer"
    """<p>The unique identifier assigned to this field within the Iceberg table schema, used for schema evolution and field tracking.</p>"""
    name: "capo_glue.types.column_name_string.ColumnNameString"
    """<p>The name of the field as it appears in the table schema and query operations.</p>"""
    type: "capo_glue.types.iceberg_document.IcebergDocument"
    """<p>The data type definition for this field, specifying the structure and format of the data it contains.</p>"""
    required: "capo_glue.types.boolean.Boolean"
    """<p>Indicates whether this field is required (non-nullable) or optional (nullable) in the table schema.</p>"""
    doc: NotRequired["capo_glue.types.comment_string.CommentString"]
    """<p>Optional documentation or description text that provides additional context about the purpose and usage of this field.</p>"""
    initial_default: NotRequired["capo_glue.types.iceberg_document.IcebergDocument"]
    """<p>Default value used to populate the field's value for all records that were written before the field was added to the schema. This enables backward compatibility when adding new fields to existing Iceberg tables.</p>"""
    write_default: NotRequired["capo_glue.types.iceberg_document.IcebergDocument"]
    """<p>Default value used to populate the field's value for any records written after the field was added to the schema, if the writer does not supply the field's value. This can be changed through schema evolution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergStructField) -> dict:
    out: dict = {}
    out["Id"] = value.get("id", 0)
    out["Name"] = value["name"]
    out["Type"] = value["type"]
    out["Required"] = value.get("required", False)
    if "doc" in value:
        out["Doc"] = value["doc"]
    if "initial_default" in value:
        out["InitialDefault"] = value["initial_default"]
    if "write_default" in value:
        out["WriteDefault"] = value["write_default"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergStructField:
    out: IcebergStructField = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = 0
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = None
    if data.get("Required") is not None:
        out["required"] = data["Required"]
    else:
        out["required"] = False
    if data.get("Doc") is not None:
        out["doc"] = data["Doc"]
    if data.get("InitialDefault") is not None:
        out["initial_default"] = data["InitialDefault"]
    if data.get("WriteDefault") is not None:
        out["write_default"] = data["WriteDefault"]
    return out
