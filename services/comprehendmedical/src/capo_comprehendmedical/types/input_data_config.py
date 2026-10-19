"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#InputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.s3_bucket
    import capo_comprehendmedical.types.s3_key


class InputDataConfig(TypedDict, closed=True):
    s3_bucket: "capo_comprehendmedical.types.s3_bucket.S3Bucket"
    """<p>The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.</p>"""
    s3_key: NotRequired["capo_comprehendmedical.types.s3_key.S3Key"]
    """<p>The path to the input data files in the S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDataConfig) -> dict:
    out: dict = {}
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputDataConfig:
    out: InputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("S3Key") is not None:
        out["s3_key"] = data["S3Key"]
    return out
