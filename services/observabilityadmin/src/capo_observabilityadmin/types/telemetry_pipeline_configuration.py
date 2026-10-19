"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryPipelineConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_pipeline_configuration_body


class TelemetryPipelineConfiguration(TypedDict, closed=True):
    body: "capo_observabilityadmin.types.telemetry_pipeline_configuration_body.TelemetryPipelineConfigurationBody"
    """<p>The pipeline configuration body that defines the data processing rules and transformations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryPipelineConfiguration) -> dict:
    out: dict = {}
    out["Body"] = value["body"]
    return out


def deserialize_json(data: dict) -> TelemetryPipelineConfiguration:
    out: TelemetryPipelineConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    else:
        out["body"] = ""
    return out
