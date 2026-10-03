"""Generated from Smithy shape ``com.amazonaws.datasync#ReportDestinationS3``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.iam_role_arn
    import capo_datasync.types.s3_bucket_arn
    import capo_datasync.types.s3_subdirectory


class ReportDestinationS3(TypedDict, closed=True):
    subdirectory: NotRequired["capo_datasync.types.s3_subdirectory.S3Subdirectory"]
    """<p>Specifies a bucket prefix for your report.</p>"""
    s3_bucket_arn: "capo_datasync.types.s3_bucket_arn.S3BucketArn"
    """<p>Specifies the ARN of the S3 bucket where DataSync uploads your report.</p>"""
    bucket_access_role_arn: "capo_datasync.types.iam_role_arn.IamRoleArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the IAM policy that allows DataSync to upload a task report to your S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html">Allowing DataSync to upload a task report to an Amazon S3 bucket</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportDestinationS3) -> dict:
    out: dict = {}
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    out["S3BucketArn"] = value["s3_bucket_arn"]
    out["BucketAccessRoleArn"] = value["bucket_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportDestinationS3:
    out: ReportDestinationS3 = {}  # type: ignore[typeddict-item]
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("S3BucketArn") is not None:
        out["s3_bucket_arn"] = data["S3BucketArn"]
    else:
        raise DeserializationError("ReportDestinationS3.s3_bucket_arn required")
    if data.get("BucketAccessRoleArn") is not None:
        out["bucket_access_role_arn"] = data["BucketAccessRoleArn"]
    else:
        raise DeserializationError(
            "ReportDestinationS3.bucket_access_role_arn required"
        )
    return out
