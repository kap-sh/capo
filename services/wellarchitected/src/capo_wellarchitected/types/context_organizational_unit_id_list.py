"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextOrganizationalUnitIdList``."""

from typing import TypeAlias

ContextOrganizationalUnitIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ContextOrganizationalUnitIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ContextOrganizationalUnitIdList:
    return [item for item in data if item is not None]
