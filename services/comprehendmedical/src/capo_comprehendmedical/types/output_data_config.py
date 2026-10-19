"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#OutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.s3_bucket
    import capo_comprehendmedical.types.s3_key


class OutputDataConfig(TypedDict, closed=True):
    s3_bucket: "capo_comprehendmedical.types.s3_bucket.S3Bucket"
    """<p>When you use the <code>OutputDataConfig</code> object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.</p>"""
    s3_key: NotRequired["capo_comprehendmedical.types.s3_key.S3Key"]
    """<p>The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputDataConfig) -> dict:
    out: dict = {}
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputDataConfig:
    out: OutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("S3Key") is not None:
        out["s3_key"] = data["S3Key"]
    return out
