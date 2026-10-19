"""Generated from Smithy shape ``com.amazonaws.datasync#S3Config``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.iam_role_arn


class S3Config(TypedDict, closed=True):
    bucket_access_role_arn: "capo_datasync.types.iam_role_arn.IamRoleArn"
    """<p>Specifies the ARN of the IAM role that DataSync uses to access your S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Config) -> dict:
    out: dict = {}
    out["BucketAccessRoleArn"] = value["bucket_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Config:
    out: S3Config = {}  # type: ignore[typeddict-item]
    if data.get("BucketAccessRoleArn") is not None:
        out["bucket_access_role_arn"] = data["BucketAccessRoleArn"]
    else:
        out["bucket_access_role_arn"] = ""
    return out
