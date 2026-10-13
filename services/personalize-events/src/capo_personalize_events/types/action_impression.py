"""Generated from Smithy shape ``com.amazonaws.personalizeevents#ActionImpression``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_events.types.action_id

ActionImpression: TypeAlias = list["capo_personalize_events.types.action_id.ActionId"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionImpression) -> list:
    return list(value)


def deserialize_json(data: list) -> ActionImpression:
    return [item for item in data if item is not None]


def redact_sensitive(value: ActionImpression) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
