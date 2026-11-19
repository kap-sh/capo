"""Generated from Smithy shape ``com.amazonaws.wellarchitected#FailedOrganizationalUnitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.failed_organizational_unit

FailedOrganizationalUnitList: TypeAlias = list[
    "capo_wellarchitected.types.failed_organizational_unit.FailedOrganizationalUnit"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedOrganizationalUnitList) -> list:
    import capo_wellarchitected.types.failed_organizational_unit

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.failed_organizational_unit.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailedOrganizationalUnitList:
    import capo_wellarchitected.types.failed_organizational_unit

    out: FailedOrganizationalUnitList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.failed_organizational_unit.deserialize_json(item)
        )
    return out
