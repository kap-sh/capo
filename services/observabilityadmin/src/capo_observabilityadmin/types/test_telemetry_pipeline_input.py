"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TestTelemetryPipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.records
    import capo_observabilityadmin.types.signal_type
    import capo_observabilityadmin.types.telemetry_pipeline_configuration


class TestTelemetryPipelineInput(TypedDict, closed=True):
    records: "capo_observabilityadmin.types.records.Records"
    """<p>The sample records to process through the pipeline configuration for testing purposes.</p>"""
    configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration"
    """<p>The pipeline configuration to test with the provided sample records.</p>"""
    signal_type: NotRequired["capo_observabilityadmin.types.signal_type.SignalType"]
    """<p>The type of telemetry signal to test. If not specified, defaults to log processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestTelemetryPipelineInput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.records

    out["Records"] = capo_observabilityadmin.types.records.serialize_json(
        value["records"]
    )
    import capo_observabilityadmin.types.telemetry_pipeline_configuration

    out["Configuration"] = (
        capo_observabilityadmin.types.telemetry_pipeline_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "signal_type" in value:
        import capo_observabilityadmin.types.signal_type

        out["SignalType"] = capo_observabilityadmin.types.signal_type.serialize_json(
            value["signal_type"]
        )
    return out


def deserialize_json(data: dict) -> TestTelemetryPipelineInput:
    out: TestTelemetryPipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("Records") is not None:
        import capo_observabilityadmin.types.records

        out["records"] = capo_observabilityadmin.types.records.deserialize_json(
            data["Records"]
        )
    else:
        raise DeserializationError("TestTelemetryPipelineInput.records required")
    if data.get("Configuration") is not None:
        import capo_observabilityadmin.types.telemetry_pipeline_configuration

        out["configuration"] = (
            capo_observabilityadmin.types.telemetry_pipeline_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("TestTelemetryPipelineInput.configuration required")
    if data.get("SignalType") is not None:
        import capo_observabilityadmin.types.signal_type

        out["signal_type"] = capo_observabilityadmin.types.signal_type.deserialize_json(
            data["SignalType"]
        )
    return out
