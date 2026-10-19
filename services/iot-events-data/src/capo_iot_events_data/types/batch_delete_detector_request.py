"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchDeleteDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.delete_detector_requests


class BatchDeleteDetectorRequest(TypedDict, closed=True):
    detectors: (
        "capo_iot_events_data.types.delete_detector_requests.DeleteDetectorRequests"
    )
    """<p>The list of one or more detectors to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDetectorRequest) -> dict:
    out: dict = {}
    import capo_iot_events_data.types.delete_detector_requests

    out["detectors"] = (
        capo_iot_events_data.types.delete_detector_requests.serialize_json(
            value["detectors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDetectorRequest:
    out: BatchDeleteDetectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("detectors") is not None:
        import capo_iot_events_data.types.delete_detector_requests

        out["detectors"] = (
            capo_iot_events_data.types.delete_detector_requests.deserialize_json(
                data["detectors"]
            )
        )
    else:
        out["detectors"] = []
    return out
