"""Generated from Smithy shape ``com.amazonaws.gamelift#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string


class S3Location(TypedDict, closed=True):
    bucket: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>An Amazon S3 bucket identifier. The name of the S3 bucket.</p> <note> <p>Amazon GameLift Servers doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).</p> </note>"""
    key: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>The name of the zip file that contains the build files or script files. </p>"""
    role_arn: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) for an IAM role that allows Amazon GameLift Servers to access the S3 bucket.</p>"""
    object_version: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>The version of the file, if object versioning is turned on for the bucket. Amazon GameLift Servers uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "key" in value:
        out["Key"] = value["key"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "object_version" in value:
        out["ObjectVersion"] = value["object_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ObjectVersion") is not None:
        out["object_version"] = data["ObjectVersion"]
    return out
