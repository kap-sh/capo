"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#PermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.permission

PermissionList: TypeAlias = list["capo_observabilityadmin.types.permission.Permission"]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionList) -> list:
    return list(value)


def deserialize_json(data: list) -> PermissionList:
    return [item for item in data if item is not None]
