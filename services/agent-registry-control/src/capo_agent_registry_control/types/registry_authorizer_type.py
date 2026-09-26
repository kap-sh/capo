"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryAuthorizerType``."""

from typing import Literal, TypeAlias, cast

RegistryAuthorizerType: TypeAlias = Literal[
    "CUSTOM_JWT",
    "AWS_IAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryAuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> RegistryAuthorizerType:
    return cast(RegistryAuthorizerType, data)
