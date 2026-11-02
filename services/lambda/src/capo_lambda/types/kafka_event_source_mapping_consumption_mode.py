"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaEventSourceMappingConsumptionMode``."""

from typing import Literal, TypeAlias, cast

KafkaEventSourceMappingConsumptionMode: TypeAlias = Literal[
    "Stream",
    "Queue",
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaEventSourceMappingConsumptionMode) -> str:
    return value


def deserialize_json(data: str) -> KafkaEventSourceMappingConsumptionMode:
    return cast(KafkaEventSourceMappingConsumptionMode, data)
