"""Generated from Smithy shape ``com.amazonaws.novaact#WorkflowExportConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.s3_bucket_name
    import capo_nova_act.types.s3_key_prefix


class WorkflowExportConfig(TypedDict, closed=True):
    s3_bucket_name: "capo_nova_act.types.s3_bucket_name.S3BucketName"
    """<p>The name of your Amazon S3 bucket, that Nova Act uses to export your workflow data. Note that the IAM role used to access Nova Act must also have write permissions to this bucket.</p>"""
    s3_key_prefix: NotRequired["capo_nova_act.types.s3_key_prefix.S3KeyPrefix"]
    """<p>An optional prefix for Amazon S3 object keys to organize exported data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowExportConfig) -> dict:
    out: dict = {}
    out["s3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["s3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_json(data: dict) -> WorkflowExportConfig:
    out: WorkflowExportConfig = {}  # type: ignore[typeddict-item]
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    else:
        out["s3_bucket_name"] = ""
    if data.get("s3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["s3KeyPrefix"]
    return out
