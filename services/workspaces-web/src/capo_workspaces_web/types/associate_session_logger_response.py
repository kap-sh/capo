"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateSessionLoggerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateSessionLoggerResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the portal.</p>"""
    session_logger_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSessionLoggerResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["sessionLoggerArn"] = value["session_logger_arn"]
    return out


def deserialize_json(data: dict) -> AssociateSessionLoggerResponse:
    out: AssociateSessionLoggerResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("sessionLoggerArn") is not None:
        out["session_logger_arn"] = data["sessionLoggerArn"]
    else:
        out["session_logger_arn"] = ""
    return out
