"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEventPredictionMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.time
    import capo_frauddetector.types.whole_number_version_string


class GetEventPredictionMetadataRequest(TypedDict, closed=True):
    event_id: "capo_frauddetector.types.identifier.identifier"
    """<p> The event ID. </p>"""
    event_type_name: "capo_frauddetector.types.identifier.identifier"
    """<p> The event type associated with the detector specified for the prediction. </p>"""
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p> The detector ID. </p>"""
    detector_version_id: (
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    )
    """<p> The detector version ID. </p>"""
    prediction_timestamp: "capo_frauddetector.types.time.time"
    """<p> The timestamp that defines when the prediction was generated. The timestamp must be specified using ISO 8601 standard in UTC.</p> <p>We recommend calling <a href="https://docs.aws.amazon.com/frauddetector/latest/api/API_ListEventPredictions.html">ListEventPredictions</a> first, and using the <code>predictionTimestamp</code> value in the response to provide an accurate prediction timestamp value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventPredictionMetadataRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["eventTypeName"] = value["event_type_name"]
    out["detectorId"] = value["detector_id"]
    out["detectorVersionId"] = value["detector_version_id"]
    out["predictionTimestamp"] = value["prediction_timestamp"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventPredictionMetadataRequest:
    out: GetEventPredictionMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError(
            "GetEventPredictionMetadataRequest.event_id required"
        )
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    else:
        raise DeserializationError(
            "GetEventPredictionMetadataRequest.event_type_name required"
        )
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError(
            "GetEventPredictionMetadataRequest.detector_id required"
        )
    if data.get("detectorVersionId") is not None:
        out["detector_version_id"] = data["detectorVersionId"]
    else:
        raise DeserializationError(
            "GetEventPredictionMetadataRequest.detector_version_id required"
        )
    if data.get("predictionTimestamp") is not None:
        out["prediction_timestamp"] = data["predictionTimestamp"]
    else:
        raise DeserializationError(
            "GetEventPredictionMetadataRequest.prediction_timestamp required"
        )
    return out
