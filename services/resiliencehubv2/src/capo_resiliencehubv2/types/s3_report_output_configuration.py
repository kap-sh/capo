"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#S3ReportOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.aws_account_id
    import capo_resiliencehubv2.types.s3_bucket_path


class S3ReportOutputConfiguration(TypedDict, closed=True):
    bucket_path: "capo_resiliencehubv2.types.s3_bucket_path.S3BucketPath"
    """<p>S3 bucket path where reports will be written (e.g., my-bucket/ngrh-reports/).</p>"""
    bucket_owner: "capo_resiliencehubv2.types.aws_account_id.AwsAccountId"
    """<p>Account ID of the bucket owner for cross-account access verification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ReportOutputConfiguration) -> dict:
    out: dict = {}
    out["bucketPath"] = value["bucket_path"]
    out["bucketOwner"] = value["bucket_owner"]
    return out


def deserialize_json(data: dict) -> S3ReportOutputConfiguration:
    out: S3ReportOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bucketPath") is not None:
        out["bucket_path"] = data["bucketPath"]
    else:
        out["bucket_path"] = ""
    if data.get("bucketOwner") is not None:
        out["bucket_owner"] = data["bucketOwner"]
    else:
        out["bucket_owner"] = ""
    return out
