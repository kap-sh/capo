"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#CreateStreamSessionAdminShellOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.session_id
    import capo_gameliftstreams.types.stream_url
    import capo_gameliftstreams.types.token_value


class CreateStreamSessionAdminShellOutput(TypedDict, closed=True):
    session_id: NotRequired["capo_gameliftstreams.types.session_id.SessionId"]
    """<p>An Amazon Web Services Systems Manager session identifier that uniquely identifies the requested terminal session. Use this value with the Amazon Web Services Systems Manager Session Manager plugin.</p>"""
    stream_url: NotRequired["capo_gameliftstreams.types.stream_url.StreamUrl"]
    """<p>An Amazon Web Services Systems Manager WebSocket connection endpoint for the requested terminal session.</p>"""
    token_value: NotRequired["capo_gameliftstreams.types.token_value.TokenValue"]
    """<p>An Amazon Web Services Systems Manager authentication token that authenticates your access to the session ID and WebSocket URL. This token must be treated with the same level of security as other user credentials. The token value is only valid for establishing a new connection within 60 seconds of generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamSessionAdminShellOutput) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "stream_url" in value:
        out["StreamUrl"] = value["stream_url"]
    if "token_value" in value:
        out["TokenValue"] = value["token_value"]
    return out


def deserialize_json(data: dict) -> CreateStreamSessionAdminShellOutput:
    out: CreateStreamSessionAdminShellOutput = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    if data.get("StreamUrl") is not None:
        out["stream_url"] = data["StreamUrl"]
    if data.get("TokenValue") is not None:
        out["token_value"] = data["TokenValue"]
    return out


def redact_sensitive(value: CreateStreamSessionAdminShellOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token_value" in value:
        out["token_value"] = "*** Sensitive Data Redacted ***"
    return out
