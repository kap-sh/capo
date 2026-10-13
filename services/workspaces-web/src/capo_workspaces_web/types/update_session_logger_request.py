"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateSessionLoggerRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.display_name_safe
    import capo_workspaces_web.types.event_filter
    import capo_workspaces_web.types.log_configuration


class UpdateSessionLoggerRequest(TypedDict, closed=True):
    session_logger_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger to update.</p>"""
    event_filter: NotRequired["capo_workspaces_web.types.event_filter.EventFilter"]
    """<p>The updated eventFilter.</p>"""
    log_configuration: NotRequired[
        "capo_workspaces_web.types.log_configuration.LogConfiguration"
    ]
    """<p>The updated logConfiguration.</p>"""
    display_name: NotRequired[
        "capo_workspaces_web.types.display_name_safe.DisplayNameSafe"
    ]
    """<p>The updated display name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionLoggerRequest) -> dict:
    out: dict = {}
    if "event_filter" in value:
        import capo_workspaces_web.types.event_filter

        out["eventFilter"] = capo_workspaces_web.types.event_filter.serialize_json(
            value["event_filter"]
        )
    if "log_configuration" in value:
        import capo_workspaces_web.types.log_configuration

        out["logConfiguration"] = (
            capo_workspaces_web.types.log_configuration.serialize_json(
                value["log_configuration"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> UpdateSessionLoggerRequest:
    out: UpdateSessionLoggerRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventFilter") is not None:
        import capo_workspaces_web.types.event_filter

        out["event_filter"] = capo_workspaces_web.types.event_filter.deserialize_json(
            data["eventFilter"]
        )
    if data.get("logConfiguration") is not None:
        import capo_workspaces_web.types.log_configuration

        out["log_configuration"] = (
            capo_workspaces_web.types.log_configuration.deserialize_json(
                data["logConfiguration"]
            )
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    return out


def redact_sensitive(value: UpdateSessionLoggerRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "log_configuration" in value:
        import capo_workspaces_web.types.log_configuration

        out["log_configuration"] = (
            capo_workspaces_web.types.log_configuration.redact_sensitive(
                value["log_configuration"]
            )
        )
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    return out
