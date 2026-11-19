"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ThirdPartyTelemetryEnrichmentStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a third-party telemetry enrichment.</p>"""
ThirdPartyTelemetryEnrichmentStatus: TypeAlias = Literal[
    "Initializing",
    "Running",
    "Stopped",
    "Impaired",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThirdPartyTelemetryEnrichmentStatus) -> str:
    return value


def deserialize_json(data: str) -> ThirdPartyTelemetryEnrichmentStatus:
    return cast(ThirdPartyTelemetryEnrichmentStatus, data)
