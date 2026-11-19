"""Generated from Smithy shape ``com.amazonaws.connecthealth#PeriodontalSiteName``."""

from typing import Literal, TypeAlias, cast

PeriodontalSiteName: TypeAlias = Literal[
    "DB",
    "B",
    "MB",
    "DL",
    "L",
    "ML",
]


# --- restJson1 ser/de ---
def serialize_json(value: PeriodontalSiteName) -> str:
    return value


def deserialize_json(data: str) -> PeriodontalSiteName:
    return cast(PeriodontalSiteName, data)
