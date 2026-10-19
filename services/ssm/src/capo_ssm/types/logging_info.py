"""Generated from Smithy shape ``com.amazonaws.ssm#LoggingInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.s3_bucket_name
    import capo_ssm.types.s3_key_prefix
    import capo_ssm.types.s3_region


class LoggingInfo(TypedDict, closed=True):
    s3_bucket_name: "capo_ssm.types.s3_bucket_name.S3BucketName"
    """<p>The name of an S3 bucket where execution logs are stored.</p>"""
    s3_key_prefix: NotRequired["capo_ssm.types.s3_key_prefix.S3KeyPrefix"]
    """<p>(Optional) The S3 bucket subfolder. </p>"""
    s3_region: "capo_ssm.types.s3_region.S3Region"
    """<p>The Amazon Web Services Region where the S3 bucket is located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoggingInfo) -> dict:
    out: dict = {}
    out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    out["S3Region"] = value["s3_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LoggingInfo:
    out: LoggingInfo = {}  # type: ignore[typeddict-item]
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        out["s3_bucket_name"] = ""
    if data.get("S3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    if data.get("S3Region") is not None:
        out["s3_region"] = data["S3Region"]
    else:
        out["s3_region"] = ""
    return out
