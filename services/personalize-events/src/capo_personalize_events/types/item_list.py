"""Generated from Smithy shape ``com.amazonaws.personalizeevents#ItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_events.types.item

ItemList: TypeAlias = list["capo_personalize_events.types.item.Item"]


# --- restJson1 ser/de ---
def serialize_json(value: ItemList) -> list:
    import capo_personalize_events.types.item

    out: list = []
    for item in value:
        out.append(capo_personalize_events.types.item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ItemList:
    import capo_personalize_events.types.item

    out: ItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_personalize_events.types.item.deserialize_json(item))
    return out


def redact_sensitive(value: ItemList) -> list[Any]:
    import capo_personalize_events.types.item

    return [capo_personalize_events.types.item.redact_sensitive(item) for item in value]
