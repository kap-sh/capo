"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#S3FilesAccessPointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.mount_path
    import capo_bedrock_agentcore_control.types.s3_files_access_point_arn


class S3FilesAccessPointConfiguration(TypedDict, closed=True):
    access_point_arn: "capo_bedrock_agentcore_control.types.s3_files_access_point_arn.S3FilesAccessPointArn"
    """<p>The ARN of the S3 Files access point to mount into the AgentCore Runtime.</p>"""
    mount_path: "capo_bedrock_agentcore_control.types.mount_path.MountPath"
    """<p>The mount path for the S3 Files access point inside the AgentCore Runtime. The path must be under <code>/mnt</code> with exactly one subdirectory level (for example, <code>/mnt/data</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3FilesAccessPointConfiguration) -> dict:
    out: dict = {}
    out["accessPointArn"] = value["access_point_arn"]
    out["mountPath"] = value["mount_path"]
    return out


def deserialize_json(data: dict) -> S3FilesAccessPointConfiguration:
    out: S3FilesAccessPointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accessPointArn") is not None:
        out["access_point_arn"] = data["accessPointArn"]
    else:
        out["access_point_arn"] = ""
    if data.get("mountPath") is not None:
        out["mount_path"] = data["mountPath"]
    else:
        out["mount_path"] = ""
    return out
