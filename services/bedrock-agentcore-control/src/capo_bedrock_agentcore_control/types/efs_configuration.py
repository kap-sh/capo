"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EfsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.efs_access_point_arn
    import capo_bedrock_agentcore_control.types.efs_file_system_arn
    import capo_bedrock_agentcore_control.types.mount_path


class EfsConfiguration(TypedDict, closed=True):
    access_point_arn: (
        "capo_bedrock_agentcore_control.types.efs_access_point_arn.EfsAccessPointArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon Elastic File System (Amazon EFS) access point to mount.</p>"""
    mount_path: "capo_bedrock_agentcore_control.types.mount_path.MountPath"
    """<p>The absolute path within the session at which the access point is mounted, for example <code>/mnt/efs</code>. Each mount path must be unique across all file system configurations in the session.</p>"""
    file_system_arn: (
        "capo_bedrock_agentcore_control.types.efs_file_system_arn.EfsFileSystemArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon Elastic File System (Amazon EFS) file system that owns the access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EfsConfiguration) -> dict:
    out: dict = {}
    out["accessPointArn"] = value["access_point_arn"]
    out["mountPath"] = value["mount_path"]
    out["fileSystemArn"] = value["file_system_arn"]
    return out


def deserialize_json(data: dict) -> EfsConfiguration:
    out: EfsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accessPointArn") is not None:
        out["access_point_arn"] = data["accessPointArn"]
    else:
        out["access_point_arn"] = ""
    if data.get("mountPath") is not None:
        out["mount_path"] = data["mountPath"]
    else:
        out["mount_path"] = ""
    if data.get("fileSystemArn") is not None:
        out["file_system_arn"] = data["fileSystemArn"]
    else:
        out["file_system_arn"] = ""
    return out
