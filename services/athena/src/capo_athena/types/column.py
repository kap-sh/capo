"""Generated from Smithy shape ``com.amazonaws.athena#Column``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.comment_string
    import capo_athena.types.name_string
    import capo_athena.types.type_string


class Column(TypedDict, closed=True):
    name: "capo_athena.types.name_string.NameString"
    """<p>The name of the column.</p>"""
    type: NotRequired["capo_athena.types.type_string.TypeString"]
    """<p>The data type of the column.</p>"""
    comment: NotRequired["capo_athena.types.comment_string.CommentString"]
    """<p>Optional information about the column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Column) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "comment" in value:
        out["Comment"] = value["comment"]
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
    return out
