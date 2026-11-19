"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalAccountEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_account_entry

OrganizationalAccountEntryList: TypeAlias = list[
    "capo_wellarchitected.types.organizational_account_entry.OrganizationalAccountEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalAccountEntryList) -> list:
    import capo_wellarchitected.types.organizational_account_entry

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.organizational_account_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OrganizationalAccountEntryList:
    import capo_wellarchitected.types.organizational_account_entry

    out: OrganizationalAccountEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.organizational_account_entry.deserialize_json(
                item
            )
        )
    return out
