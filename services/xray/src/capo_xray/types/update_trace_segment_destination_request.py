"""Generated from Smithy shape ``com.amazonaws.xray#UpdateTraceSegmentDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.cloud_watch_logs_configuration
    import capo_xray.types.trace_segment_destination


class UpdateTraceSegmentDestinationRequest(TypedDict, closed=True):
    destination: NotRequired[
        "capo_xray.types.trace_segment_destination.TraceSegmentDestination"
    ]
    """<p> The configured destination of trace segments. </p>"""
    cloud_watch_logs_configuration: NotRequired[
        "capo_xray.types.cloud_watch_logs_configuration.CloudWatchLogsConfiguration"
    ]
    """<p> Specifies settings for the CloudWatch Logs log groups that X-Ray creates for Transaction Search. Specify this only when <code>Destination</code> is <code>CloudWatchLogs</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTraceSegmentDestinationRequest) -> dict:
    out: dict = {}
    if "destination" in value:
        import capo_xray.types.trace_segment_destination

        out["Destination"] = capo_xray.types.trace_segment_destination.serialize_json(
            value["destination"]
        )
    if "cloud_watch_logs_configuration" in value:
        import capo_xray.types.cloud_watch_logs_configuration

        out["CloudWatchLogsConfiguration"] = (
            capo_xray.types.cloud_watch_logs_configuration.serialize_json(
                value["cloud_watch_logs_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTraceSegmentDestinationRequest:
    out: UpdateTraceSegmentDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        import capo_xray.types.trace_segment_destination

        out["destination"] = capo_xray.types.trace_segment_destination.deserialize_json(
            data["Destination"]
        )
    if data.get("CloudWatchLogsConfiguration") is not None:
        import capo_xray.types.cloud_watch_logs_configuration

        out["cloud_watch_logs_configuration"] = (
            capo_xray.types.cloud_watch_logs_configuration.deserialize_json(
                data["CloudWatchLogsConfiguration"]
            )
        )
    return out
