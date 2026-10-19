"""Generated from Smithy shape ``com.amazonaws.glue#Column``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.column_type_string
    import capo_glue.types.comment_string
    import capo_glue.types.name_string
    import capo_glue.types.parameters_map


class Column(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the <code>Column</code>.</p>"""
    type: NotRequired["capo_glue.types.column_type_string.ColumnTypeString"]
    """<p>The data type of the <code>Column</code>.</p>"""
    comment: NotRequired["capo_glue.types.comment_string.CommentString"]
    """<p>A free-form text comment.</p>"""
    parameters: NotRequired["capo_glue.types.parameters_map.ParametersMap"]
    """<p>These key-value pairs define properties associated with the column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Column) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "parameters" in value:
        import capo_glue.types.parameters_map

        out["Parameters"] = capo_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Column:
    out: Column = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Comment") is not None:
        out["comment"] = data["Comment"]
    if data.get("Parameters") is not None:
        import capo_glue.types.parameters_map

        out["parameters"] = capo_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
