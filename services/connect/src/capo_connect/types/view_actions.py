"""Generated from Smithy shape ``com.amazonaws.connect#ViewActions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.view_action

ViewActions: TypeAlias = list["capo_connect.types.view_action.ViewAction"]


# --- restJson1 ser/de ---
def serialize_json(value: ViewActions) -> list:
    return list(value)


def deserialize_json(data: list) -> ViewActions:
    return [item for item in data if item is not None]


def redact_sensitive(value: ViewActions) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
