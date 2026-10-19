"""Generated from Smithy shape ``com.amazonaws.codestarconnections#UpdateSyncBlockerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_connections.types.resource_name
    import capo_codestar_connections.types.sync_blocker


class UpdateSyncBlockerOutput(TypedDict, closed=True):
    resource_name: "capo_codestar_connections.types.resource_name.ResourceName"
    """<p>The resource name for the sync blocker.</p>"""
    parent_resource_name: NotRequired[
        "capo_codestar_connections.types.resource_name.ResourceName"
    ]
    """<p>The parent resource name for the sync blocker.</p>"""
    sync_blocker: "capo_codestar_connections.types.sync_blocker.SyncBlocker"
    """<p>Information about the sync blocker to be updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSyncBlockerOutput) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    if "parent_resource_name" in value:
        out["ParentResourceName"] = value["parent_resource_name"]
    import capo_codestar_connections.types.sync_blocker

    out["SyncBlocker"] = (
        capo_codestar_connections.types.sync_blocker.serialize_aws_json_1_0(
            value["sync_blocker"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSyncBlockerOutput:
    out: UpdateSyncBlockerOutput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    else:
        out["resource_name"] = ""
    if data.get("ParentResourceName") is not None:
        out["parent_resource_name"] = data["ParentResourceName"]
    if data.get("SyncBlocker") is not None:
        import capo_codestar_connections.types.sync_blocker

        out["sync_blocker"] = (
            capo_codestar_connections.types.sync_blocker.deserialize_aws_json_1_0(
                data["SyncBlocker"]
            )
        )
    else:
        raise DeserializationError("UpdateSyncBlockerOutput.sync_blocker required")
    return out
