"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.session_summary

SessionSummaryList: TypeAlias = list[
    "capo_workspaces_web.types.session_summary.SessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummaryList) -> list:
    import capo_workspaces_web.types.session_summary

    out: list = []
    for item in value:
        out.append(capo_workspaces_web.types.session_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionSummaryList:
    import capo_workspaces_web.types.session_summary

    out: SessionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces_web.types.session_summary.deserialize_json(item))
    return out


def redact_sensitive(value: SessionSummaryList) -> list[Any]:
    import capo_workspaces_web.types.session_summary

    return [
        capo_workspaces_web.types.session_summary.redact_sensitive(item)
        for item in value
    ]
