"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetTelemetryPipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_pipeline_identifier


class GetTelemetryPipelineInput(TypedDict, closed=True):
    pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier"
    """<p>The identifier (name or ARN) of the telemetry pipeline to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTelemetryPipelineInput) -> dict:
    out: dict = {}
    out["PipelineIdentifier"] = value["pipeline_identifier"]
    return out


def deserialize_json(data: dict) -> GetTelemetryPipelineInput:
    out: GetTelemetryPipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("PipelineIdentifier") is not None:
        out["pipeline_identifier"] = data["PipelineIdentifier"]
    else:
        out["pipeline_identifier"] = ""
    return out
