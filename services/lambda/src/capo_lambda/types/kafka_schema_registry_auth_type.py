"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaRegistryAuthType``."""

from typing import Literal, TypeAlias, cast

KafkaSchemaRegistryAuthType: TypeAlias = Literal[
    "BASIC_AUTH",
    "CLIENT_CERTIFICATE_TLS_AUTH",
    "SERVER_ROOT_CA_CERTIFICATE",
    "OAUTHBEARER_AUTH",
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaSchemaRegistryAuthType) -> str:
    return value


def deserialize_json(data: str) -> KafkaSchemaRegistryAuthType:
    return cast(KafkaSchemaRegistryAuthType, data)
