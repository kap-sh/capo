"""Generated from Smithy shape ``com.amazonaws.personalizeevents#Impression``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_events.types.item_id

Impression: TypeAlias = list["capo_personalize_events.types.item_id.ItemId"]


# --- restJson1 ser/de ---
def serialize_json(value: Impression) -> list:
    return list(value)


def deserialize_json(data: list) -> Impression:
    return [item for item in data if item is not None]


def redact_sensitive(value: Impression) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
