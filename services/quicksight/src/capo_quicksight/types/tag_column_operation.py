"""Generated from Smithy shape ``com.amazonaws.quicksight#TagColumnOperation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name
    import capo_quicksight.types.column_tag_list


class TagColumnOperation(TypedDict, closed=True):
    column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The column that this operation acts on.</p>"""
    tags: "capo_quicksight.types.column_tag_list.ColumnTagList"
    """<p>The dataset column tag, currently only used for geospatial type tagging.</p> <note> <p>This is not tags for the Amazon Web Services tagging feature.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagColumnOperation) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    import capo_quicksight.types.column_tag_list

    out["Tags"] = capo_quicksight.types.column_tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagColumnOperation:
    out: TagColumnOperation = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    if data.get("Tags") is not None:
        import capo_quicksight.types.column_tag_list

        out["tags"] = capo_quicksight.types.column_tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out


def redact_sensitive(value: TagColumnOperation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_quicksight.types.column_tag_list

        out["tags"] = capo_quicksight.types.column_tag_list.redact_sensitive(
            value["tags"]
        )
    return out
