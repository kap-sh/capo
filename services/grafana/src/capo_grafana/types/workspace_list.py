"""Generated from Smithy shape ``com.amazonaws.grafana#WorkspaceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.workspace_summary

WorkspaceList: TypeAlias = list["capo_grafana.types.workspace_summary.WorkspaceSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceList) -> list:
    import capo_grafana.types.workspace_summary

    out: list = []
    for item in value:
        out.append(capo_grafana.types.workspace_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkspaceList:
    import capo_grafana.types.workspace_summary

    out: WorkspaceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_grafana.types.workspace_summary.deserialize_json(item))
    return out


def redact_sensitive(value: WorkspaceList) -> list[Any]:
    import capo_grafana.types.workspace_summary

    return [
        capo_grafana.types.workspace_summary.redact_sensitive(item) for item in value
    ]
