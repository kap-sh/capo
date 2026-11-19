"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PreferenceEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.preference_entry

PreferenceEntries: TypeAlias = list[
    "capo_wellarchitected.types.preference_entry.PreferenceEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: PreferenceEntries) -> list:
    import capo_wellarchitected.types.preference_entry

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.preference_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> PreferenceEntries:
    import capo_wellarchitected.types.preference_entry

    out: PreferenceEntries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.preference_entry.deserialize_json(item))
    return out
