"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationObservations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

InvestigationObservations: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationObservations) -> list:
    return list(value)


def deserialize_json(data: list) -> InvestigationObservations:
    return [item for item in data if item is not None]
