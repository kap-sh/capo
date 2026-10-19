"""Generated from Smithy shape ``com.amazonaws.customerprofiles#S3ExportingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.s3_bucket_name
    import capo_customer_profiles.types.s3_key_name_customer_output_config


class S3ExportingConfig(TypedDict, closed=True):
    s3_bucket_name: "capo_customer_profiles.types.s3_bucket_name.s3BucketName"
    """<p>The name of the S3 bucket where Identity Resolution Jobs write result files.</p>"""
    s3_key_name: NotRequired[
        "capo_customer_profiles.types.s3_key_name_customer_output_config.s3KeyNameCustomerOutputConfig"
    ]
    """<p>The S3 key name of the location where Identity Resolution Jobs write result files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ExportingConfig) -> dict:
    out: dict = {}
    out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key_name" in value:
        out["S3KeyName"] = value["s3_key_name"]
    return out


def deserialize_json(data: dict) -> S3ExportingConfig:
    out: S3ExportingConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        out["s3_bucket_name"] = ""
    if data.get("S3KeyName") is not None:
        out["s3_key_name"] = data["S3KeyName"]
    return out
