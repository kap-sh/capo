"""Generated from Smithy shape ``com.amazonaws.personalizeevents#ActionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_events.types.action

ActionList: TypeAlias = list["capo_personalize_events.types.action.Action"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionList) -> list:
    import capo_personalize_events.types.action

    out: list = []
    for item in value:
        out.append(capo_personalize_events.types.action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionList:
    import capo_personalize_events.types.action

    out: ActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_personalize_events.types.action.deserialize_json(item))
    return out


def redact_sensitive(value: ActionList) -> list[Any]:
    import capo_personalize_events.types.action

    return [
        capo_personalize_events.types.action.redact_sensitive(item) for item in value
    ]
