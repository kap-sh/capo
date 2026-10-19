"""Generated from Smithy shape ``com.amazonaws.cloudtrail#S3ImportSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.string


class S3ImportSource(TypedDict, closed=True):
    s3_location_uri: "capo_cloudtrail.types.string.String"
    """<p> The URI for the source S3 bucket. </p>"""
    s3_bucket_region: "capo_cloudtrail.types.string.String"
    """<p> The Region associated with the source S3 bucket. </p>"""
    s3_bucket_access_role_arn: "capo_cloudtrail.types.string.String"
    """<p> The IAM ARN role used to access the source S3 bucket. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ImportSource) -> dict:
    out: dict = {}
    out["S3LocationUri"] = value["s3_location_uri"]
    out["S3BucketRegion"] = value["s3_bucket_region"]
    out["S3BucketAccessRoleArn"] = value["s3_bucket_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ImportSource:
    out: S3ImportSource = {}  # type: ignore[typeddict-item]
    if data.get("S3LocationUri") is not None:
        out["s3_location_uri"] = data["S3LocationUri"]
    else:
        out["s3_location_uri"] = ""
    if data.get("S3BucketRegion") is not None:
        out["s3_bucket_region"] = data["S3BucketRegion"]
    else:
        out["s3_bucket_region"] = ""
    if data.get("S3BucketAccessRoleArn") is not None:
        out["s3_bucket_access_role_arn"] = data["S3BucketAccessRoleArn"]
    else:
        out["s3_bucket_access_role_arn"] = ""
    return out
