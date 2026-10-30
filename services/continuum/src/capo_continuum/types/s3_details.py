"""Generated from Smithy shape ``com.amazonaws.continuum#S3Details``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_s3_bucket_name
    import capo_continuum.types.integration_s3_role_arn


class S3Details(TypedDict, closed=True):
    bucket: "capo_continuum.types.integration_s3_bucket_name.IntegrationS3BucketName"
    role_arn: "capo_continuum.types.integration_s3_role_arn.IntegrationS3RoleArn"


# --- restJson1 ser/de ---
def serialize_json(value: S3Details) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> S3Details:
    out: S3Details = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
