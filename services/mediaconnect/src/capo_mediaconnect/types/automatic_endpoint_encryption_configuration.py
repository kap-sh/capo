"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AutomaticEndpointEncryptionConfiguration``."""

from typing_extensions import TypedDict


class AutomaticEndpointEncryptionConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AutomaticEndpointEncryptionConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AutomaticEndpointEncryptionConfiguration:
    out: AutomaticEndpointEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    return out
