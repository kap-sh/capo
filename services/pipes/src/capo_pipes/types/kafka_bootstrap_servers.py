"""Generated from Smithy shape ``com.amazonaws.pipes#KafkaBootstrapServers``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.endpoint_string

KafkaBootstrapServers: TypeAlias = list[
    "capo_pipes.types.endpoint_string.EndpointString"
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaBootstrapServers) -> list:
    return list(value)


def deserialize_json(data: list) -> KafkaBootstrapServers:
    return [item for item in data if item is not None]


def redact_sensitive(value: KafkaBootstrapServers) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
