"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointRegistrationState``."""

from typing import Literal, TypeAlias, cast

SourceEndpointRegistrationState: TypeAlias = Literal[
    "REGISTERED",
    "REGISTERING",
    "DEREGISTERING",
    "REGISTRATION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointRegistrationState) -> str:
    return value


def deserialize_json(data: str) -> SourceEndpointRegistrationState:
    return cast(SourceEndpointRegistrationState, data)
