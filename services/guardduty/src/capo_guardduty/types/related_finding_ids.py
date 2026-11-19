"""Generated from Smithy shape ``com.amazonaws.guardduty#RelatedFindingIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.finding_id

RelatedFindingIds: TypeAlias = list["capo_guardduty.types.finding_id.FindingId"]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedFindingIds) -> list:
    return list(value)


def deserialize_json(data: list) -> RelatedFindingIds:
    return [item for item in data if item is not None]
