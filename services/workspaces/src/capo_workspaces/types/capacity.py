"""Generated from Smithy shape ``com.amazonaws.workspaces#Capacity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.desired_user_sessions


class Capacity(TypedDict, closed=True):
    desired_user_sessions: (
        "capo_workspaces.types.desired_user_sessions.DesiredUserSessions"
    )
    """<p>The desired number of user sessions for the WorkSpaces in the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Capacity) -> dict:
    out: dict = {}
    out["DesiredUserSessions"] = value["desired_user_sessions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Capacity:
    out: Capacity = {}  # type: ignore[typeddict-item]
    if data.get("DesiredUserSessions") is not None:
        out["desired_user_sessions"] = data["DesiredUserSessions"]
    else:
        out["desired_user_sessions"] = 0
    return out
