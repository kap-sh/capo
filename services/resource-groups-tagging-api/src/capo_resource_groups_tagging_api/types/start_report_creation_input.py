"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#StartReportCreationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.s3_bucket


class StartReportCreationInput(TypedDict, closed=True):
    s3_bucket: "capo_resource_groups_tagging_api.types.s3_bucket.S3Bucket"
    """<p>The name of the Amazon S3 bucket where the report will be stored; for example:</p> <p> <code>amzn-s3-demo-bucket</code> </p> <p>For more information on S3 bucket requirements, including an example bucket policy, see the example Amazon S3 bucket policy on this page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReportCreationInput) -> dict:
    out: dict = {}
    out["S3Bucket"] = value["s3_bucket"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReportCreationInput:
    out: StartReportCreationInput = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    return out
