"""Generated from Smithy shape ``com.amazonaws.finspacedata#PermissionGroupByUserList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_finspace_data.types.permission_group_by_user

PermissionGroupByUserList: TypeAlias = list[
    "capo_finspace_data.types.permission_group_by_user.PermissionGroupByUser"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionGroupByUserList) -> list:
    import capo_finspace_data.types.permission_group_by_user

    out: list = []
    for item in value:
        out.append(
            capo_finspace_data.types.permission_group_by_user.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PermissionGroupByUserList:
    import capo_finspace_data.types.permission_group_by_user

    out: PermissionGroupByUserList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_finspace_data.types.permission_group_by_user.deserialize_json(item)
        )
    return out


def redact_sensitive(value: PermissionGroupByUserList) -> list[Any]:
    import capo_finspace_data.types.permission_group_by_user

    return [
        capo_finspace_data.types.permission_group_by_user.redact_sensitive(item)
        for item in value
    ]
