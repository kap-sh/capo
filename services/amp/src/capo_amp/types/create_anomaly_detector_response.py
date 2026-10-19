"""Generated from Smithy shape ``com.amazonaws.amp#CreateAnomalyDetectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.anomaly_detector_arn
    import capo_amp.types.anomaly_detector_id
    import capo_amp.types.anomaly_detector_status
    import capo_amp.types.tag_map


class CreateAnomalyDetectorResponse(TypedDict, closed=True):
    anomaly_detector_id: "capo_amp.types.anomaly_detector_id.AnomalyDetectorId"
    """<p>The unique identifier of the created anomaly detector.</p>"""
    arn: "capo_amp.types.anomaly_detector_arn.AnomalyDetectorArn"
    """<p>The Amazon Resource Name (ARN) of the created anomaly detector.</p>"""
    status: "capo_amp.types.anomaly_detector_status.AnomalyDetectorStatus"
    """<p>The status information of the created anomaly detector.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>The tags applied to the created anomaly detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnomalyDetectorResponse) -> dict:
    out: dict = {}
    out["anomalyDetectorId"] = value["anomaly_detector_id"]
    out["arn"] = value["arn"]
    import capo_amp.types.anomaly_detector_status

    out["status"] = capo_amp.types.anomaly_detector_status.serialize_json(
        value["status"]
    )
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAnomalyDetectorResponse:
    out: CreateAnomalyDetectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("anomalyDetectorId") is not None:
        out["anomaly_detector_id"] = data["anomalyDetectorId"]
    else:
        out["anomaly_detector_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_amp.types.anomaly_detector_status

        out["status"] = capo_amp.types.anomaly_detector_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateAnomalyDetectorResponse.status required")
    if data.get("tags") is not None:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    return out
