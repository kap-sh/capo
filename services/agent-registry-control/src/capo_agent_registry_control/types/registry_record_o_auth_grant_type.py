"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordOAuthGrantType``."""

from typing import Literal, TypeAlias, cast

RegistryRecordOAuthGrantType: TypeAlias = Literal["CLIENT_CREDENTIALS",]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordOAuthGrantType) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordOAuthGrantType:
    return cast(RegistryRecordOAuthGrantType, data)
