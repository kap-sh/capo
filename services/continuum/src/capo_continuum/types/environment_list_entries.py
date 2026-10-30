"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentListEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.environment_list_entry

EnvironmentListEntries: TypeAlias = list[
    "capo_continuum.types.environment_list_entry.EnvironmentListEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentListEntries) -> list:
    import capo_continuum.types.environment_list_entry

    out: list = []
    for item in value:
        out.append(capo_continuum.types.environment_list_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentListEntries:
    import capo_continuum.types.environment_list_entry

    out: EnvironmentListEntries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.environment_list_entry.deserialize_json(item))
    return out
