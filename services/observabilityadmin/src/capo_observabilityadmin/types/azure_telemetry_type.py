"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureTelemetryType``."""

from typing import Literal, TypeAlias, cast

AzureTelemetryType: TypeAlias = Literal[
    "ResourceLogs",
    "Metrics",
    "FlowLogs",
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureTelemetryType) -> str:
    return value


def deserialize_json(data: str) -> AzureTelemetryType:
    return cast(AzureTelemetryType, data)
