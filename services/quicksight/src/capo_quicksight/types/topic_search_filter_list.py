"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSearchFilterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_search_filter

TopicSearchFilterList: TypeAlias = list[
    "capo_quicksight.types.topic_search_filter.TopicSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicSearchFilterList) -> list:
    import capo_quicksight.types.topic_search_filter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicSearchFilterList:
    import capo_quicksight.types.topic_search_filter

    out: TopicSearchFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_search_filter.deserialize_json(item))
    return out


def redact_sensitive(value: TopicSearchFilterList) -> list[Any]:
    import capo_quicksight.types.topic_search_filter

    return [
        capo_quicksight.types.topic_search_filter.redact_sensitive(item)
        for item in value
    ]
