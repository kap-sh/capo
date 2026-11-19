"""Generated from Smithy shape ``com.amazonaws.networkmanager#MultipathResilienceMode``."""

from typing import Literal, TypeAlias, cast

MultipathResilienceMode: TypeAlias = Literal[
    "best-effort",
    "disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultipathResilienceMode) -> str:
    return value


def deserialize_json(data: str) -> MultipathResilienceMode:
    return cast(MultipathResilienceMode, data)
