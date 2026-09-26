"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordCredentialProviderType``."""

from typing import Literal, TypeAlias, cast

RegistryRecordCredentialProviderType: TypeAlias = Literal[
    "OAUTH",
    "IAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordCredentialProviderType) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordCredentialProviderType:
    return cast(RegistryRecordCredentialProviderType, data)
