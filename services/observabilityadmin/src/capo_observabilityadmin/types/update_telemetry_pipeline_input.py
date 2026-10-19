"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#UpdateTelemetryPipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_pipeline_configuration
    import capo_observabilityadmin.types.telemetry_pipeline_identifier


class UpdateTelemetryPipelineInput(TypedDict, closed=True):
    pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier"
    """<p>The ARN of the telemetry pipeline to update.</p>"""
    configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration"
    """<p>The new configuration for the telemetry pipeline, including updated sources, processors, and destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTelemetryPipelineInput) -> dict:
    out: dict = {}
    out["PipelineIdentifier"] = value["pipeline_identifier"]
    import capo_observabilityadmin.types.telemetry_pipeline_configuration

    out["Configuration"] = (
        capo_observabilityadmin.types.telemetry_pipeline_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTelemetryPipelineInput:
    out: UpdateTelemetryPipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("PipelineIdentifier") is not None:
        out["pipeline_identifier"] = data["PipelineIdentifier"]
    else:
        out["pipeline_identifier"] = ""
    if data.get("Configuration") is not None:
        import capo_observabilityadmin.types.telemetry_pipeline_configuration

        out["configuration"] = (
            capo_observabilityadmin.types.telemetry_pipeline_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTelemetryPipelineInput.configuration required"
        )
    return out
