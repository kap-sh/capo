"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

"""The operational status of an environment."""
EnvironmentStatus: TypeAlias = Literal["ACTIVE",]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentStatus) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentStatus:
    return cast(EnvironmentStatus, data)
