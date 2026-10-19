"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CapacityProviderVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_volume_name
    import capo_bedrock_agentcore_control.types.mount_path


class CapacityProviderVolumeConfiguration(TypedDict, closed=True):
    volume_name: "capo_bedrock_agentcore_control.types.capacity_provider_volume_name.CapacityProviderVolumeName"
    """<p>The logical name of the capacity provider volume to mount. This name must match a volume that is defined in the capacity provider's list of volumes.</p>"""
    mount_path: "capo_bedrock_agentcore_control.types.mount_path.MountPath"
    """<p>The mount path for the capacity provider volume inside the AgentCore Runtime. The path must be under <code>/mnt</code> with exactly one subdirectory level (for example, <code>/mnt/data</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderVolumeConfiguration) -> dict:
    out: dict = {}
    out["volumeName"] = value["volume_name"]
    out["mountPath"] = value["mount_path"]
    return out


def deserialize_json(data: dict) -> CapacityProviderVolumeConfiguration:
    out: CapacityProviderVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("volumeName") is not None:
        out["volume_name"] = data["volumeName"]
    else:
        out["volume_name"] = ""
    if data.get("mountPath") is not None:
        out["mount_path"] = data["mountPath"]
    else:
        out["mount_path"] = ""
    return out
