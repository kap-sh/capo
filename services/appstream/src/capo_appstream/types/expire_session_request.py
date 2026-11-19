"""Generated from Smithy shape ``com.amazonaws.appstream#ExpireSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string


class ExpireSessionRequest(TypedDict, closed=True):
    session_id: NotRequired["capo_appstream.types.string.String"]
    """<p>The identifier of the streaming session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpireSessionRequest) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpireSessionRequest:
    out: ExpireSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpireSessionRequest) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    return out


def deserialize_cbor(data: dict) -> ExpireSessionRequest:
    out: ExpireSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    return out
