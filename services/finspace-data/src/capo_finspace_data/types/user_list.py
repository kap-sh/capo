"""Generated from Smithy shape ``com.amazonaws.finspacedata#UserList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_finspace_data.types.user

UserList: TypeAlias = list["capo_finspace_data.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: UserList) -> list:
    import capo_finspace_data.types.user

    out: list = []
    for item in value:
        out.append(capo_finspace_data.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserList:
    import capo_finspace_data.types.user

    out: UserList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_finspace_data.types.user.deserialize_json(item))
    return out


def redact_sensitive(value: UserList) -> list[Any]:
    import capo_finspace_data.types.user

    return [capo_finspace_data.types.user.redact_sensitive(item) for item in value]
