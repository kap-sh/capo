"""Generated from Smithy shape ``com.amazonaws.continuum#IssueFindingIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.finding_id

IssueFindingIds: TypeAlias = list["capo_continuum.types.finding_id.FindingId"]


# --- restJson1 ser/de ---
def serialize_json(value: IssueFindingIds) -> list:
    return list(value)


def deserialize_json(data: list) -> IssueFindingIds:
    return [item for item in data if item is not None]
