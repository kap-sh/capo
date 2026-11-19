"""Generated from Smithy shape ``com.amazonaws.codebuild#SSMSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.string


class SSMSession(TypedDict, closed=True):
    session_id: NotRequired["capo_codebuild.types.string.String"]
    """<p>The ID of the session.</p>"""
    token_value: NotRequired["capo_codebuild.types.string.String"]
    """<p>An encrypted token value containing session and caller information.</p>"""
    stream_url: NotRequired["capo_codebuild.types.string.String"]
    """<p>A URL back to SSM Agent on the managed node that the Session Manager client uses to send commands and receive output from the node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SSMSession) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "token_value" in value:
        out["tokenValue"] = value["token_value"]
    if "stream_url" in value:
        out["streamUrl"] = value["stream_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SSMSession:
    out: SSMSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("tokenValue") is not None:
        out["token_value"] = data["tokenValue"]
    if data.get("streamUrl") is not None:
        out["stream_url"] = data["streamUrl"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SSMSession) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "token_value" in value:
        out["tokenValue"] = value["token_value"]
    if "stream_url" in value:
        out["streamUrl"] = value["stream_url"]
    return out


def deserialize_cbor(data: dict) -> SSMSession:
    out: SSMSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("tokenValue") is not None:
        out["token_value"] = data["tokenValue"]
    if data.get("streamUrl") is not None:
        out["stream_url"] = data["streamUrl"]
    return out
