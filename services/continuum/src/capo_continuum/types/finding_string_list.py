"""Generated from Smithy shape ``com.amazonaws.continuum#FindingStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.finding_list_entry

FindingStringList: TypeAlias = list[
    "capo_continuum.types.finding_list_entry.FindingListEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> FindingStringList:
    return [item for item in data if item is not None]
