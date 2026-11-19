"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PreferenceUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.preference_update

PreferenceUpdates: TypeAlias = list[
    "capo_wellarchitected.types.preference_update.PreferenceUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: PreferenceUpdates) -> list:
    import capo_wellarchitected.types.preference_update

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.preference_update.serialize_json(item))
    return out


def deserialize_json(data: list) -> PreferenceUpdates:
    import capo_wellarchitected.types.preference_update

    out: PreferenceUpdates = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.preference_update.deserialize_json(item))
    return out
