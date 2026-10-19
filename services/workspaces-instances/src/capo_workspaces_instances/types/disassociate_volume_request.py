"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#DisassociateVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.device_name
    import capo_workspaces_instances.types.disassociate_mode_enum
    import capo_workspaces_instances.types.volume_id
    import capo_workspaces_instances.types.workspace_instance_id


class DisassociateVolumeRequest(TypedDict, closed=True):
    workspace_instance_id: (
        "capo_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>WorkSpace Instance to detach volume from.</p>"""
    volume_id: "capo_workspaces_instances.types.volume_id.VolumeId"
    """<p>Volume to be detached.</p>"""
    device: NotRequired["capo_workspaces_instances.types.device_name.DeviceName"]
    """<p>Device path of volume to detach.</p>"""
    disassociate_mode: NotRequired[
        "capo_workspaces_instances.types.disassociate_mode_enum.DisassociateModeEnum"
    ]
    """<p>Mode for volume detachment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateVolumeRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    out["VolumeId"] = value["volume_id"]
    if "device" in value:
        out["Device"] = value["device"]
    if "disassociate_mode" in value:
        import capo_workspaces_instances.types.disassociate_mode_enum

        out["DisassociateMode"] = (
            capo_workspaces_instances.types.disassociate_mode_enum.serialize_aws_json_1_0(
                value["disassociate_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateVolumeRequest:
    out: DisassociateVolumeRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("DisassociateMode") is not None:
        import capo_workspaces_instances.types.disassociate_mode_enum

        out["disassociate_mode"] = (
            capo_workspaces_instances.types.disassociate_mode_enum.deserialize_aws_json_1_0(
                data["DisassociateMode"]
            )
        )
    return out
