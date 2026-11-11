"""Generated from Smithy shape ``com.amazonaws.ram#PermissionStatus``."""

from typing import Literal, TypeAlias, cast

PermissionStatus: TypeAlias = Literal[
    "ATTACHABLE",
    "UNATTACHABLE",
    "DELETING",
    "DELETED",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionStatus) -> str:
    return value


def deserialize_json(data: str) -> PermissionStatus:
    return cast(PermissionStatus, data)
