"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#StartTelemetryPipelineRefreshInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_pipeline_identifier


class StartTelemetryPipelineRefreshInput(TypedDict, closed=True):
    pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier"
    """<p>The Amazon Resource Name (ARN) of the telemetry pipeline to refresh.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTelemetryPipelineRefreshInput) -> dict:
    out: dict = {}
    out["PipelineIdentifier"] = value["pipeline_identifier"]
    return out


def deserialize_json(data: dict) -> StartTelemetryPipelineRefreshInput:
    out: StartTelemetryPipelineRefreshInput = {}  # type: ignore[typeddict-item]
    if data.get("PipelineIdentifier") is not None:
        out["pipeline_identifier"] = data["PipelineIdentifier"]
    else:
        out["pipeline_identifier"] = ""
    return out
