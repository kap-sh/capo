"""Generated from Smithy shape ``com.amazonaws.codestarconnections#SyncBlockerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.latest_sync_blocker_list
    import capo_codestar_connections.types.resource_name


class SyncBlockerSummary(TypedDict, closed=True):
    resource_name: "capo_codestar_connections.types.resource_name.ResourceName"
    """<p>The resource name for sync blocker summary.</p>"""
    parent_resource_name: NotRequired[
        "capo_codestar_connections.types.resource_name.ResourceName"
    ]
    """<p>The parent resource name for a sync blocker summary.</p>"""
    latest_blockers: NotRequired[
        "capo_codestar_connections.types.latest_sync_blocker_list.LatestSyncBlockerList"
    ]
    """<p>The latest events for a sync blocker summary.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlockerSummary) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    if "parent_resource_name" in value:
        out["ParentResourceName"] = value["parent_resource_name"]
    if "latest_blockers" in value:
        import capo_codestar_connections.types.latest_sync_blocker_list

        out["LatestBlockers"] = (
            capo_codestar_connections.types.latest_sync_blocker_list.serialize_aws_json_1_0(
                value["latest_blockers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlockerSummary:
    out: SyncBlockerSummary = {}  # type: ignore[typeddict-item]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    else:
        out["resource_name"] = ""
    if data.get("ParentResourceName") is not None:
        out["parent_resource_name"] = data["ParentResourceName"]
    if data.get("LatestBlockers") is not None:
        import capo_codestar_connections.types.latest_sync_blocker_list

        out["latest_blockers"] = (
            capo_codestar_connections.types.latest_sync_blocker_list.deserialize_aws_json_1_0(
                data["LatestBlockers"]
            )
        )
    return out
