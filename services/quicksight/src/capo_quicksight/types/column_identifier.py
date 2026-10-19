"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name
    import capo_quicksight.types.data_set_identifier
    import capo_quicksight.types.topic_identifier


class ColumnIdentifier(TypedDict, closed=True):
    data_set_identifier: "capo_quicksight.types.data_set_identifier.DataSetIdentifier"
    """<p>The data set that the column belongs to.</p>"""
    topic_identifier: NotRequired[
        "capo_quicksight.types.topic_identifier.TopicIdentifier"
    ]
    """<p>The topic that the column belongs to.</p>"""
    column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The name of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnIdentifier) -> dict:
    out: dict = {}
    out["DataSetIdentifier"] = value.get("data_set_identifier", "")
    if "topic_identifier" in value:
        out["TopicIdentifier"] = value["topic_identifier"]
    out["ColumnName"] = value["column_name"]
    return out


def deserialize_json(data: dict) -> ColumnIdentifier:
    out: ColumnIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("DataSetIdentifier") is not None:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        out["data_set_identifier"] = ""
    if data.get("TopicIdentifier") is not None:
        out["topic_identifier"] = data["TopicIdentifier"]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    return out
