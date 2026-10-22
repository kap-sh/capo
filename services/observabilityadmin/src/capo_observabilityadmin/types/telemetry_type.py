"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryType``."""

from typing import Literal, TypeAlias, cast

TelemetryType: TypeAlias = Literal[
    "Logs",
    "Metrics",
    "Traces",
    "Insights",
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryType) -> str:
    return value


def deserialize_json(data: str) -> TelemetryType:
    return cast(TelemetryType, data)
