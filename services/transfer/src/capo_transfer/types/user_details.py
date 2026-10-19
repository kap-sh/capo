"""Generated from Smithy shape ``com.amazonaws.transfer#UserDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.server_id
    import capo_transfer.types.session_id
    import capo_transfer.types.user_name


class UserDetails(TypedDict, closed=True):
    user_name: "capo_transfer.types.user_name.UserName"
    """<p>A unique string that identifies a Transfer Family user associated with a server.</p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The system-assigned unique identifier for a Transfer server instance. </p>"""
    session_id: NotRequired["capo_transfer.types.session_id.SessionId"]
    """<p>The system-assigned unique identifier for a session that corresponds to the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserDetails) -> dict:
    out: dict = {}
    out["UserName"] = value["user_name"]
    out["ServerId"] = value["server_id"]
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserDetails:
    out: UserDetails = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        out["user_name"] = ""
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    return out
