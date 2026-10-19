"""Generated from Smithy shape ``com.amazonaws.rekognition#GetFaceLivenessSessionResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.liveness_session_id


class GetFaceLivenessSessionResultsRequest(TypedDict, closed=True):
    session_id: "capo_rekognition.types.liveness_session_id.LivenessSessionId"
    """<p>A unique 128-bit UUID. This is used to uniquely identify the session and also acts as an idempotency token for all operations associated with the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFaceLivenessSessionResultsRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFaceLivenessSessionResultsRequest:
    out: GetFaceLivenessSessionResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    return out
