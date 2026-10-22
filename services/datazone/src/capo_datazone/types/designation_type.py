"""Generated from Smithy shape ``com.amazonaws.datazone#DesignationType``."""

from typing import Literal, TypeAlias, cast

"""The classification of a designation."""
DesignationType: TypeAlias = Literal[
    "MANAGED",
    "USER_CREATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DesignationType) -> str:
    return value


def deserialize_json(data: str) -> DesignationType:
    return cast(DesignationType, data)
