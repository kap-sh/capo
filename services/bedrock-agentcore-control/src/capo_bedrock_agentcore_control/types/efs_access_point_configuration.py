"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EfsAccessPointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.efs_access_point_arn
    import capo_bedrock_agentcore_control.types.mount_path


class EfsAccessPointConfiguration(TypedDict, closed=True):
    access_point_arn: (
        "capo_bedrock_agentcore_control.types.efs_access_point_arn.EfsAccessPointArn"
    )
    """<p>The ARN of the EFS access point to mount into the AgentCore Runtime.</p>"""
    mount_path: "capo_bedrock_agentcore_control.types.mount_path.MountPath"
    """<p>The mount path for the EFS access point inside the AgentCore Runtime. The path must be under <code>/mnt</code> with exactly one subdirectory level (for example, <code>/mnt/data</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EfsAccessPointConfiguration) -> dict:
    out: dict = {}
    out["accessPointArn"] = value["access_point_arn"]
    out["mountPath"] = value["mount_path"]
    return out


def deserialize_json(data: dict) -> EfsAccessPointConfiguration:
    out: EfsAccessPointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accessPointArn") is not None:
        out["access_point_arn"] = data["accessPointArn"]
    else:
        out["access_point_arn"] = ""
    if data.get("mountPath") is not None:
        out["mount_path"] = data["mountPath"]
    else:
        out["mount_path"] = ""
    return out
