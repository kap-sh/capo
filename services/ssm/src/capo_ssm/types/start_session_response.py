"""Generated from Smithy shape ``com.amazonaws.ssm#StartSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.session_id
    import capo_ssm.types.stream_url
    import capo_ssm.types.token_value


class StartSessionResponse(TypedDict, closed=True):
    session_id: NotRequired["capo_ssm.types.session_id.SessionId"]
    """<p>The ID of the session.</p>"""
    token_value: NotRequired["capo_ssm.types.token_value.TokenValue"]
    """<p>An encrypted token value containing session and caller information. This token is used to authenticate the connection to the managed node, and is valid only long enough to ensure the connection is successful. Never share your session's token.</p>"""
    stream_url: NotRequired["capo_ssm.types.stream_url.StreamUrl"]
    """<p>A URL back to SSM Agent on the managed node that the Session Manager client uses to send commands and receive output from the node. Format: <code>wss://ssmmessages.<b>region</b>.amazonaws.com/v1/data-channel/<b>session-id</b>?stream=(input|output)</code> </p> <p> <b>region</b> represents the Region identifier for an Amazon Web Services Region supported by Amazon Web Services Systems Manager, such as <code>us-east-2</code> for the US East (Ohio) Region. For a list of supported <b>region</b> values, see the <b>Region</b> column in <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#ssm_region">Systems Manager service endpoints</a> in the <i>Amazon Web Services General Reference</i>.</p> <p> <b>session-id</b> represents the ID of a Session Manager session, such as <code>1a2b3c4dEXAMPLE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSessionResponse) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "token_value" in value:
        out["TokenValue"] = value["token_value"]
    if "stream_url" in value:
        out["StreamUrl"] = value["stream_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSessionResponse:
    out: StartSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    if data.get("TokenValue") is not None:
        out["token_value"] = data["TokenValue"]
    if data.get("StreamUrl") is not None:
        out["stream_url"] = data["StreamUrl"]
    return out
