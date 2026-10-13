"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionLogger``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.arn_list
    import capo_workspaces_web.types.display_name_safe
    import capo_workspaces_web.types.encryption_context_map
    import capo_workspaces_web.types.event_filter
    import capo_workspaces_web.types.key_arn
    import capo_workspaces_web.types.log_configuration
    import capo_workspaces_web.types.timestamp


class SessionLogger(TypedDict, closed=True):
    session_logger_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger resource.</p>"""
    event_filter: NotRequired["capo_workspaces_web.types.event_filter.EventFilter"]
    """<p>The filter that specifies which events to monitor.</p>"""
    log_configuration: NotRequired[
        "capo_workspaces_web.types.log_configuration.LogConfiguration"
    ]
    """<p>The configuration that specifies where logs are fowarded.</p>"""
    customer_managed_key: NotRequired["capo_workspaces_web.types.key_arn.keyArn"]
    """<p>The custom managed key of the session logger.</p>"""
    additional_encryption_context: NotRequired[
        "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
    ]
    """<p>The additional encryption context of the session logger.</p>"""
    associated_portal_arns: NotRequired["capo_workspaces_web.types.arn_list.ArnList"]
    """<p>The associated portal ARN.</p>"""
    display_name: NotRequired[
        "capo_workspaces_web.types.display_name_safe.DisplayNameSafe"
    ]
    """<p>The human-readable display name.</p>"""
    creation_date: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The date the session logger resource was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionLogger) -> dict:
    out: dict = {}
    out["sessionLoggerArn"] = value["session_logger_arn"]
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
    if "customer_managed_key" in value:
        out["customerManagedKey"] = value["customer_managed_key"]
    if "additional_encryption_context" in value:
        import capo_workspaces_web.types.encryption_context_map

        out["additionalEncryptionContext"] = (
            capo_workspaces_web.types.encryption_context_map.serialize_json(
                value["additional_encryption_context"]
            )
        )
    if "associated_portal_arns" in value:
        import capo_workspaces_web.types.arn_list

        out["associatedPortalArns"] = capo_workspaces_web.types.arn_list.serialize_json(
            value["associated_portal_arns"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "creation_date" in value:
        import capo_workspaces_web.types.timestamp

        out["creationDate"] = capo_workspaces_web.types.timestamp.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> SessionLogger:
    out: SessionLogger = {}  # type: ignore[typeddict-item]
    if data.get("sessionLoggerArn") is not None:
        out["session_logger_arn"] = data["sessionLoggerArn"]
    else:
        raise DeserializationError("SessionLogger.session_logger_arn required")
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
    if data.get("customerManagedKey") is not None:
        out["customer_managed_key"] = data["customerManagedKey"]
    if data.get("additionalEncryptionContext") is not None:
        import capo_workspaces_web.types.encryption_context_map

        out["additional_encryption_context"] = (
            capo_workspaces_web.types.encryption_context_map.deserialize_json(
                data["additionalEncryptionContext"]
            )
        )
    if data.get("associatedPortalArns") is not None:
        import capo_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            capo_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
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


def redact_sensitive(value: SessionLogger) -> dict[str, Any]:
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
