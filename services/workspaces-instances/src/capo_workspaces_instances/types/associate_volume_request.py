"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#AssociateVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.device_name
    import capo_workspaces_instances.types.volume_id
    import capo_workspaces_instances.types.workspace_instance_id


class AssociateVolumeRequest(TypedDict, closed=True):
    workspace_instance_id: (
        "capo_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>WorkSpace Instance to attach volume to.</p>"""
    volume_id: "capo_workspaces_instances.types.volume_id.VolumeId"
    """<p>Volume to be attached.</p>"""
    device: "capo_workspaces_instances.types.device_name.DeviceName"
    """<p>Device path for volume attachment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateVolumeRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    out["VolumeId"] = value["volume_id"]
    out["Device"] = value["device"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateVolumeRequest:
    out: AssociateVolumeRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceInstanceId") is not None:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        out["workspace_instance_id"] = ""
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    else:
        out["volume_id"] = ""
    if data.get("Device") is not None:
        out["device"] = data["Device"]
    else:
        out["device"] = ""
    return out
