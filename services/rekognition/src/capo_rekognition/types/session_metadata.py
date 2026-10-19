"""Generated from Smithy shape ``com.amazonaws.rekognition#SessionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.sdk_type_string


class SessionMetadata(TypedDict, closed=True):
    sdk_type: "capo_rekognition.types.sdk_type_string.SDKTypeString"
    """<p>The type of SDK that was used to stream the video for the Face Liveness session.</p> <note> <p>This value is self-reported by the client that streamed the session, and Amazon Rekognition doesn't verify it. Don't rely on it for authentication, authorization, or any other security decision.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionMetadata) -> dict:
    out: dict = {}
    out["SDKType"] = value["sdk_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionMetadata:
    out: SessionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("SDKType") is not None:
        out["sdk_type"] = data["SDKType"]
    else:
        out["sdk_type"] = ""
    return out
