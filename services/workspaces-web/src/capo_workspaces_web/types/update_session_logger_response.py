"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateSessionLoggerResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.session_logger


class UpdateSessionLoggerResponse(TypedDict, closed=True):
    session_logger: "capo_workspaces_web.types.session_logger.SessionLogger"
    """<p>The updated details of the session logger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionLoggerResponse) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.session_logger

    out["sessionLogger"] = capo_workspaces_web.types.session_logger.serialize_json(
        value["session_logger"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSessionLoggerResponse:
    out: UpdateSessionLoggerResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionLogger") is not None:
        import capo_workspaces_web.types.session_logger

        out["session_logger"] = (
            capo_workspaces_web.types.session_logger.deserialize_json(
                data["sessionLogger"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSessionLoggerResponse.session_logger required"
        )
    return out


def redact_sensitive(value: UpdateSessionLoggerResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "session_logger" in value:
        import capo_workspaces_web.types.session_logger

        out["session_logger"] = (
            capo_workspaces_web.types.session_logger.redact_sensitive(
                value["session_logger"]
            )
        )
    return out
