"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#PutConnectorTelemetryManifestOutput``."""

from typing_extensions import TypedDict


class PutConnectorTelemetryManifestOutput(TypedDict, closed=True):
    version: "int"
    """<p>The version of the telemetry manifest after this update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConnectorTelemetryManifestOutput) -> dict:
    out: dict = {}
    out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> PutConnectorTelemetryManifestOutput:
    out: PutConnectorTelemetryManifestOutput = {}  # type: ignore[typeddict-item]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    return out
