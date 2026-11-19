"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ThirdPartyTelemetrySource``."""

from typing import Literal, TypeAlias, cast

"""<p>A third-party telemetry source that can provide resource metadata.</p>"""
ThirdPartyTelemetrySource: TypeAlias = Literal["Azure",]


# --- restJson1 ser/de ---
def serialize_json(value: ThirdPartyTelemetrySource) -> str:
    return value


def deserialize_json(data: str) -> ThirdPartyTelemetrySource:
    return cast(ThirdPartyTelemetrySource, data)
