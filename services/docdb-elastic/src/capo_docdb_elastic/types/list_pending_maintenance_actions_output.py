"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ListPendingMaintenanceActionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.pagination_token
    import capo_docdb_elastic.types.resource_pending_maintenance_action_list


class ListPendingMaintenanceActionsOutput(TypedDict, closed=True):
    resource_pending_maintenance_actions: "capo_docdb_elastic.types.resource_pending_maintenance_action_list.ResourcePendingMaintenanceActionList"
    """<p>Provides information about a pending maintenance action for a resource.</p>"""
    next_token: NotRequired["capo_docdb_elastic.types.pagination_token.PaginationToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is displayed, the responses will include only records beyond the marker, up to the value specified by <code>maxResults</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPendingMaintenanceActionsOutput) -> dict:
    out: dict = {}
    import capo_docdb_elastic.types.resource_pending_maintenance_action_list

    out["resourcePendingMaintenanceActions"] = (
        capo_docdb_elastic.types.resource_pending_maintenance_action_list.serialize_json(
            value["resource_pending_maintenance_actions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPendingMaintenanceActionsOutput:
    out: ListPendingMaintenanceActionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("resourcePendingMaintenanceActions") is not None:
        import capo_docdb_elastic.types.resource_pending_maintenance_action_list

        out["resource_pending_maintenance_actions"] = (
            capo_docdb_elastic.types.resource_pending_maintenance_action_list.deserialize_json(
                data["resourcePendingMaintenanceActions"]
            )
        )
    else:
        out["resource_pending_maintenance_actions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
