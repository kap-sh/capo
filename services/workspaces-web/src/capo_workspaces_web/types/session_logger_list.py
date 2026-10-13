"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionLoggerList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.session_logger_summary

SessionLoggerList: TypeAlias = list[
    "capo_workspaces_web.types.session_logger_summary.SessionLoggerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionLoggerList) -> list:
    import capo_workspaces_web.types.session_logger_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_web.types.session_logger_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SessionLoggerList:
    import capo_workspaces_web.types.session_logger_summary

    out: SessionLoggerList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_web.types.session_logger_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SessionLoggerList) -> list[Any]:
    import capo_workspaces_web.types.session_logger_summary

    return [
        capo_workspaces_web.types.session_logger_summary.redact_sensitive(item)
        for item in value
    ]
