"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#S3BucketMountConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.mount_path


class S3BucketMountConfiguration(TypedDict, closed=True):
    bucket: "str"
    """<p>The name of the S3 bucket to mount. You can specify a general purpose bucket or a directory bucket.</p>"""
    mount_path: "capo_bedrock_agentcore_control.types.mount_path.MountPath"
    """<p>The mount path for the S3 bucket inside the AgentCore Runtime. The path must be under <code>/mnt</code> with exactly one subdirectory level (for example, <code>/mnt/data</code>).</p>"""
    prefix: NotRequired["str"]
    """<p>The key prefix to mount. Only objects under this prefix are visible at the mount path. To give each session its own prefix, include <code>{runtimeSessionId}</code> (for example, <code>data/{runtimeSessionId}/</code>). If you omit the prefix, the whole bucket is mounted.</p>"""
    s3_bucket_owner: NotRequired["str"]
    """<p>The AWS account ID that must own the bucket. If you omit it, the bucket must be owned by the account that owns the AgentCore Runtime.</p>"""
    s3_bucket_region: NotRequired["str"]
    """<p>The AWS Region of the S3 bucket. If you omit it, the bucket must be in the same Region as the AgentCore Runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketMountConfiguration) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["mountPath"] = value["mount_path"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    if "s3_bucket_region" in value:
        out["s3BucketRegion"] = value["s3_bucket_region"]
    return out


def deserialize_json(data: dict) -> S3BucketMountConfiguration:
    out: S3BucketMountConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("mountPath") is not None:
        out["mount_path"] = data["mountPath"]
    else:
        out["mount_path"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    if data.get("s3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    if data.get("s3BucketRegion") is not None:
        out["s3_bucket_region"] = data["s3BucketRegion"]
    return out
