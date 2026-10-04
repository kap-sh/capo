"""Generated from Smithy shape ``com.amazonaws.opensearch#AcceptedWarningsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.string

AcceptedWarningsList: TypeAlias = list["capo_opensearch.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: AcceptedWarningsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AcceptedWarningsList:
    return [item for item in data if item is not None]
