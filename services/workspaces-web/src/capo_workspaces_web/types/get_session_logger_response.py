"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetSessionLoggerResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.session_logger


class GetSessionLoggerResponse(TypedDict, closed=True):
    session_logger: NotRequired[
        "capo_workspaces_web.types.session_logger.SessionLogger"
    ]
    """<p>The session logger details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionLoggerResponse) -> dict:
    out: dict = {}
    if "session_logger" in value:
        import capo_workspaces_web.types.session_logger

        out["sessionLogger"] = capo_workspaces_web.types.session_logger.serialize_json(
            value["session_logger"]
        )
    return out


def deserialize_json(data: dict) -> GetSessionLoggerResponse:
    out: GetSessionLoggerResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionLogger") is not None:
        import capo_workspaces_web.types.session_logger

        out["session_logger"] = (
            capo_workspaces_web.types.session_logger.deserialize_json(
                data["sessionLogger"]
            )
        )
    return out


def redact_sensitive(value: GetSessionLoggerResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "session_logger" in value:
        import capo_workspaces_web.types.session_logger

        out["session_logger"] = (
            capo_workspaces_web.types.session_logger.redact_sensitive(
                value["session_logger"]
            )
        )
    return out
