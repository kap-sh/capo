"""Generated from Smithy shape ``com.amazonaws.workspacesweb#PortalList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.portal_summary

PortalList: TypeAlias = list["capo_workspaces_web.types.portal_summary.PortalSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: PortalList) -> list:
    import capo_workspaces_web.types.portal_summary

    out: list = []
    for item in value:
        out.append(capo_workspaces_web.types.portal_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PortalList:
    import capo_workspaces_web.types.portal_summary

    out: PortalList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces_web.types.portal_summary.deserialize_json(item))
    return out


def redact_sensitive(value: PortalList) -> list[Any]:
    import capo_workspaces_web.types.portal_summary

    return [
        capo_workspaces_web.types.portal_summary.redact_sensitive(item)
        for item in value
    ]
