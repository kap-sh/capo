"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.session_status
    import capo_workspaces_web.types.string_type
    import capo_workspaces_web.types.timestamp
    import capo_workspaces_web.types.username


class SessionSummary(TypedDict, closed=True):
    portal_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the web portal.</p>"""
    session_id: NotRequired["capo_workspaces_web.types.string_type.StringType"]
    """<p>The ID of the session.</p>"""
    username: NotRequired["capo_workspaces_web.types.username.Username"]
    """<p>The username of the session.</p>"""
    status: NotRequired["capo_workspaces_web.types.session_status.SessionStatus"]
    """<p>The status of the session.</p>"""
    start_time: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The start time of the session.</p>"""
    end_time: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The end time of the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    if "portal_arn" in value:
        out["portalArn"] = value["portal_arn"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "username" in value:
        out["username"] = value["username"]
    if "status" in value:
        import capo_workspaces_web.types.session_status

        out["status"] = capo_workspaces_web.types.session_status.serialize_json(
            value["status"]
        )
    if "start_time" in value:
        import capo_workspaces_web.types.timestamp

        out["startTime"] = capo_workspaces_web.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_workspaces_web.types.timestamp

        out["endTime"] = capo_workspaces_web.types.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("status") is not None:
        import capo_workspaces_web.types.session_status

        out["status"] = capo_workspaces_web.types.session_status.deserialize_json(
            data["status"]
        )
    if data.get("startTime") is not None:
        import capo_workspaces_web.types.timestamp

        out["start_time"] = capo_workspaces_web.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_workspaces_web.types.timestamp

        out["end_time"] = capo_workspaces_web.types.timestamp.deserialize_json(
            data["endTime"]
        )
    return out


def redact_sensitive(value: SessionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
