"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedEntitySort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.topic_sort_direction


class NamedEntitySort(TypedDict, closed=True):
    field_name: "capo_quicksight.types.limited_string.LimitedString"
    """<p>The name of the field that is used for the sort.</p>"""
    direction: "capo_quicksight.types.topic_sort_direction.TopicSortDirection"
    """<p>The direction of the sort. Valid values are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamedEntitySort) -> dict:
    out: dict = {}
    out["FieldName"] = value["field_name"]
    import capo_quicksight.types.topic_sort_direction

    out["Direction"] = capo_quicksight.types.topic_sort_direction.serialize_json(
        value["direction"]
    )
    return out


def deserialize_json(data: dict) -> NamedEntitySort:
    out: NamedEntitySort = {}  # type: ignore[typeddict-item]
    if data.get("FieldName") is not None:
        out["field_name"] = data["FieldName"]
    else:
        out["field_name"] = ""
    if data.get("Direction") is not None:
        import capo_quicksight.types.topic_sort_direction

        out["direction"] = capo_quicksight.types.topic_sort_direction.deserialize_json(
            data["Direction"]
        )
    else:
        import typing

        out["direction"] = typing.cast(
            "capo_quicksight.types.topic_sort_direction.TopicSortDirection", ""
        )
    return out
