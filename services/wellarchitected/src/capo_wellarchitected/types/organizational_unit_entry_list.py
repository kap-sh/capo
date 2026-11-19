"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalUnitEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_unit_entry

OrganizationalUnitEntryList: TypeAlias = list[
    "capo_wellarchitected.types.organizational_unit_entry.OrganizationalUnitEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitEntryList) -> list:
    import capo_wellarchitected.types.organizational_unit_entry

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.organizational_unit_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OrganizationalUnitEntryList:
    import capo_wellarchitected.types.organizational_unit_entry

    out: OrganizationalUnitEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.organizational_unit_entry.deserialize_json(item)
        )
    return out
