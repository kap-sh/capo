"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionLoggerSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.display_name_safe
    import capo_workspaces_web.types.log_configuration
    import capo_workspaces_web.types.timestamp


class SessionLoggerSummary(TypedDict, closed=True):
    session_logger_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger resource.</p>"""
    log_configuration: NotRequired[
        "capo_workspaces_web.types.log_configuration.LogConfiguration"
    ]
    """<p>The configuration that specifies where the logs are fowarded.</p>"""
    display_name: NotRequired[
        "capo_workspaces_web.types.display_name_safe.DisplayNameSafe"
    ]
    """<p>The human-readable display name.</p>"""
    creation_date: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The date the session logger resource was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionLoggerSummary) -> dict:
    out: dict = {}
    out["sessionLoggerArn"] = value["session_logger_arn"]
    if "log_configuration" in value:
        import capo_workspaces_web.types.log_configuration

        out["logConfiguration"] = (
            capo_workspaces_web.types.log_configuration.serialize_json(
                value["log_configuration"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "creation_date" in value:
        import capo_workspaces_web.types.timestamp

        out["creationDate"] = capo_workspaces_web.types.timestamp.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> SessionLoggerSummary:
    out: SessionLoggerSummary = {}  # type: ignore[typeddict-item]
    if data.get("sessionLoggerArn") is not None:
        out["session_logger_arn"] = data["sessionLoggerArn"]
    else:
        out["session_logger_arn"] = ""
    if data.get("logConfiguration") is not None:
        import capo_workspaces_web.types.log_configuration

        out["log_configuration"] = (
            capo_workspaces_web.types.log_configuration.deserialize_json(
                data["logConfiguration"]
            )
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("creationDate") is not None:
        import capo_workspaces_web.types.timestamp

        out["creation_date"] = capo_workspaces_web.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    return out


def redact_sensitive(value: SessionLoggerSummary) -> dict[str, Any]:
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
