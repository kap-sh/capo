"""Generated from Smithy shape ``com.amazonaws.personalizeevents#EventList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_events.types.event

EventList: TypeAlias = list["capo_personalize_events.types.event.Event"]


# --- restJson1 ser/de ---
def serialize_json(value: EventList) -> list:
    import capo_personalize_events.types.event

    out: list = []
    for item in value:
        out.append(capo_personalize_events.types.event.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventList:
    import capo_personalize_events.types.event

    out: EventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_personalize_events.types.event.deserialize_json(item))
    return out


def redact_sensitive(value: EventList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
