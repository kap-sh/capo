"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingTypeNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

FindingTypeNames: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeNames) -> list:
    return list(value)


def deserialize_json(data: list) -> FindingTypeNames:
    return [item for item in data if item is not None]
