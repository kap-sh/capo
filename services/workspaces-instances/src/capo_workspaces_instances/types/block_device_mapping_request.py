"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BlockDeviceMappingRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.device_name
    import capo_workspaces_instances.types.ebs_block_device
    import capo_workspaces_instances.types.virtual_name


class BlockDeviceMappingRequest(TypedDict, closed=True):
    device_name: NotRequired["capo_workspaces_instances.types.device_name.DeviceName"]
    """<p>Name of the device for storage mapping.</p>"""
    ebs: NotRequired["capo_workspaces_instances.types.ebs_block_device.EbsBlockDevice"]
    """<p>EBS volume configuration for the device.</p>"""
    no_device: NotRequired["capo_workspaces_instances.types.device_name.DeviceName"]
    """<p>Indicates device should not be mapped.</p>"""
    virtual_name: NotRequired[
        "capo_workspaces_instances.types.virtual_name.VirtualName"
    ]
    """<p>Virtual device name for ephemeral storage.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlockDeviceMappingRequest) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "ebs" in value:
        import capo_workspaces_instances.types.ebs_block_device

        out["Ebs"] = (
            capo_workspaces_instances.types.ebs_block_device.serialize_aws_json_1_0(
                value["ebs"]
            )
        )
    if "no_device" in value:
        out["NoDevice"] = value["no_device"]
    if "virtual_name" in value:
        out["VirtualName"] = value["virtual_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BlockDeviceMappingRequest:
    out: BlockDeviceMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceName") is not None:
        out["device_name"] = data["DeviceName"]
    if data.get("Ebs") is not None:
        import capo_workspaces_instances.types.ebs_block_device

        out["ebs"] = (
            capo_workspaces_instances.types.ebs_block_device.deserialize_aws_json_1_0(
                data["Ebs"]
            )
        )
    if data.get("NoDevice") is not None:
        out["no_device"] = data["NoDevice"]
    if data.get("VirtualName") is not None:
        out["virtual_name"] = data["VirtualName"]
    return out


def redact_sensitive(value: BlockDeviceMappingRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ebs" in value:
        import capo_workspaces_instances.types.ebs_block_device

        out["ebs"] = capo_workspaces_instances.types.ebs_block_device.redact_sensitive(
            value["ebs"]
        )
    return out
