"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateSessionLoggerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class CreateSessionLoggerResponse(TypedDict, closed=True):
    session_logger_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSessionLoggerResponse) -> dict:
    out: dict = {}
    out["sessionLoggerArn"] = value["session_logger_arn"]
    return out


def deserialize_json(data: dict) -> CreateSessionLoggerResponse:
    out: CreateSessionLoggerResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionLoggerArn") is not None:
        out["session_logger_arn"] = data["sessionLoggerArn"]
    else:
        out["session_logger_arn"] = ""
    return out
