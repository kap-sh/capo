"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryFilterName``."""

from typing import Literal, TypeAlias, cast

RegistryFilterName: TypeAlias = Literal[
    "status",
    "discoveryConfiguration.authorizerType",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryFilterName) -> str:
    return value


def deserialize_json(data: str) -> RegistryFilterName:
    return cast(RegistryFilterName, data)
