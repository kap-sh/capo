"""Generated from Smithy shape ``com.amazonaws.workspaces#CapacityStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.active_user_sessions
    import capo_workspaces.types.actual_user_sessions
    import capo_workspaces.types.available_user_sessions
    import capo_workspaces.types.desired_user_sessions


class CapacityStatus(TypedDict, closed=True):
    available_user_sessions: (
        "capo_workspaces.types.available_user_sessions.AvailableUserSessions"
    )
    """<p>The number of user sessions currently available for streaming from your pool.</p> <p>AvailableUserSessions = ActualUserSessions - ActiveUserSessions</p>"""
    desired_user_sessions: (
        "capo_workspaces.types.desired_user_sessions.DesiredUserSessions"
    )
    """<p>The total number of sessions slots that are either running or pending. This represents the total number of concurrent streaming sessions your pool can support in a steady state.</p>"""
    actual_user_sessions: (
        "capo_workspaces.types.actual_user_sessions.ActualUserSessions"
    )
    """<p>The total number of user sessions that are available for streaming or are currently streaming in your pool.</p> <p>ActualUserSessions = AvailableUserSessions + ActiveUserSessions</p>"""
    active_user_sessions: (
        "capo_workspaces.types.active_user_sessions.ActiveUserSessions"
    )
    """<p>The number of user sessions currently being used for your pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityStatus) -> dict:
    out: dict = {}
    out["AvailableUserSessions"] = value["available_user_sessions"]
    out["DesiredUserSessions"] = value["desired_user_sessions"]
    out["ActualUserSessions"] = value["actual_user_sessions"]
    out["ActiveUserSessions"] = value["active_user_sessions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityStatus:
    out: CapacityStatus = {}  # type: ignore[typeddict-item]
    if data.get("AvailableUserSessions") is not None:
        out["available_user_sessions"] = data["AvailableUserSessions"]
    else:
        out["available_user_sessions"] = 0
    if data.get("DesiredUserSessions") is not None:
        out["desired_user_sessions"] = data["DesiredUserSessions"]
    else:
        out["desired_user_sessions"] = 0
    if data.get("ActualUserSessions") is not None:
        out["actual_user_sessions"] = data["ActualUserSessions"]
    else:
        out["actual_user_sessions"] = 0
    if data.get("ActiveUserSessions") is not None:
        out["active_user_sessions"] = data["ActiveUserSessions"]
    else:
        out["active_user_sessions"] = 0
    return out
