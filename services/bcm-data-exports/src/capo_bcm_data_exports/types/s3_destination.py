"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#S3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.account_id
    import capo_bcm_data_exports.types.generic_string
    import capo_bcm_data_exports.types.s3_output_configurations


class S3Destination(TypedDict, closed=True):
    s3_bucket: "capo_bcm_data_exports.types.generic_string.GenericString"
    """<p>The name of the Amazon S3 bucket used as the destination of a data export file.</p>"""
    s3_bucket_owner: NotRequired["capo_bcm_data_exports.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the S3 bucket used as the destination for the data export.</p>"""
    s3_prefix: "capo_bcm_data_exports.types.generic_string.GenericString"
    """<p>The S3 path prefix you want prepended to the name of your data export.</p>"""
    s3_region: "capo_bcm_data_exports.types.generic_string.GenericString"
    """<p>The S3 bucket Region.</p>"""
    s3_output_configurations: (
        "capo_bcm_data_exports.types.s3_output_configurations.S3OutputConfigurations"
    )
    """<p>The output configuration for the data export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Destination) -> dict:
    out: dict = {}
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_bucket_owner" in value:
        out["S3BucketOwner"] = value["s3_bucket_owner"]
    out["S3Prefix"] = value["s3_prefix"]
    out["S3Region"] = value["s3_region"]
    import capo_bcm_data_exports.types.s3_output_configurations

    out["S3OutputConfigurations"] = (
        capo_bcm_data_exports.types.s3_output_configurations.serialize_aws_json_1_1(
            value["s3_output_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("S3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["S3BucketOwner"]
    if data.get("S3Prefix") is not None:
        out["s3_prefix"] = data["S3Prefix"]
    else:
        out["s3_prefix"] = ""
    if data.get("S3Region") is not None:
        out["s3_region"] = data["S3Region"]
    else:
        out["s3_region"] = ""
    if data.get("S3OutputConfigurations") is not None:
        import capo_bcm_data_exports.types.s3_output_configurations

        out["s3_output_configurations"] = (
            capo_bcm_data_exports.types.s3_output_configurations.deserialize_aws_json_1_1(
                data["S3OutputConfigurations"]
            )
        )
    else:
        raise DeserializationError("S3Destination.s3_output_configurations required")
    return out
