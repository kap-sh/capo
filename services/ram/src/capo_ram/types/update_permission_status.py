"""Generated from Smithy shape ``com.amazonaws.ram#UpdatePermissionStatus``."""

from typing import Literal, TypeAlias, cast

UpdatePermissionStatus: TypeAlias = Literal[
    "ATTACHABLE",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePermissionStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdatePermissionStatus:
    return cast(UpdatePermissionStatus, data)
