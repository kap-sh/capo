"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointRegistrationState``."""

from typing import Literal, TypeAlias, cast

DestinationEndpointRegistrationState: TypeAlias = Literal[
    "REGISTERED",
    "REGISTERING",
    "DEREGISTERING",
    "REGISTRATION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointRegistrationState) -> str:
    return value


def deserialize_json(data: str) -> DestinationEndpointRegistrationState:
    return cast(DestinationEndpointRegistrationState, data)
