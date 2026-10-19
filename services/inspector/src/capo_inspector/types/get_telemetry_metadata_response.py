"""Generated from Smithy shape ``com.amazonaws.inspector#GetTelemetryMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.telemetry_metadata_list


class GetTelemetryMetadataResponse(TypedDict, closed=True):
    telemetry_metadata: (
        "capo_inspector.types.telemetry_metadata_list.TelemetryMetadataList"
    )
    """<p>Telemetry details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTelemetryMetadataResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.telemetry_metadata_list

    out["telemetryMetadata"] = (
        capo_inspector.types.telemetry_metadata_list.serialize_aws_json_1_1(
            value["telemetry_metadata"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTelemetryMetadataResponse:
    out: GetTelemetryMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("telemetryMetadata") is not None:
        import capo_inspector.types.telemetry_metadata_list

        out["telemetry_metadata"] = (
            capo_inspector.types.telemetry_metadata_list.deserialize_aws_json_1_1(
                data["telemetryMetadata"]
            )
        )
    else:
        out["telemetry_metadata"] = []
    return out
