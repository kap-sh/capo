"""Generated from Smithy shape ``com.amazonaws.athena#GetSessionEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.session_id


class GetSessionEndpointRequest(TypedDict, closed=True):
    session_id: "capo_athena.types.session_id.SessionId"
    """<p>The session ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionEndpointRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionEndpointRequest:
    out: GetSessionEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    return out
