"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EndpointLifecycle``."""

from typing import Literal, TypeAlias, cast

EndpointLifecycle: TypeAlias = Literal[
    "MANAGED",
    "UNMANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointLifecycle) -> str:
    return value


def deserialize_json(data: str) -> EndpointLifecycle:
    return cast(EndpointLifecycle, data)
