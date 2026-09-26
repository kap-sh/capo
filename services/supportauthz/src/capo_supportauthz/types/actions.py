"""Generated from Smithy shape ``com.amazonaws.supportauthz#Actions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supportauthz.types.action

Actions: TypeAlias = list["capo_supportauthz.types.action.Action"]


# --- restJson1 ser/de ---
def serialize_json(value: Actions) -> list:
    return list(value)


def deserialize_json(data: list) -> Actions:
    return [item for item in data if item is not None]
