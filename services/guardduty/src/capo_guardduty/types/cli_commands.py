"""Generated from Smithy shape ``com.amazonaws.guardduty#CliCommands``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

CliCommands: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: CliCommands) -> list:
    return list(value)


def deserialize_json(data: list) -> CliCommands:
    return [item for item in data if item is not None]
