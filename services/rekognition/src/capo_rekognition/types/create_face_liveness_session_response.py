"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateFaceLivenessSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.liveness_session_id


class CreateFaceLivenessSessionResponse(TypedDict, closed=True):
    session_id: "capo_rekognition.types.liveness_session_id.LivenessSessionId"
    """<p>A unique 128-bit UUID identifying a Face Liveness session. A new sessionID must be used for every Face Liveness check. If a given sessionID is used for subsequent Face Liveness checks, the checks will fail. Additionally, a SessionId expires 3 minutes after it's sent, making all Liveness data associated with the session (e.g., sessionID, reference image, audit images, etc.) unavailable. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFaceLivenessSessionResponse) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFaceLivenessSessionResponse:
    out: CreateFaceLivenessSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    return out
