"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#S3ReportOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.account_id


class S3ReportOutputConfiguration(TypedDict, closed=True):
    bucket_path: NotRequired["str"]
    """<p>The S3 bucket name and optional prefix where reports are stored. Format: bucket-name or bucket-name/prefix.</p>"""
    bucket_owner: NotRequired["capo_arc_region_switch.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the S3 bucket. Required to ensure the bucket is still owned by the same expected owner at generation time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3ReportOutputConfiguration) -> dict:
    out: dict = {}
    if "bucket_path" in value:
        out["bucketPath"] = value["bucket_path"]
    if "bucket_owner" in value:
        out["bucketOwner"] = value["bucket_owner"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3ReportOutputConfiguration:
    out: S3ReportOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bucketPath") is not None:
        out["bucket_path"] = data["bucketPath"]
    if data.get("bucketOwner") is not None:
        out["bucket_owner"] = data["bucketOwner"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3ReportOutputConfiguration) -> dict:
    out: dict = {}
    if "bucket_path" in value:
        out["bucketPath"] = value["bucket_path"]
    if "bucket_owner" in value:
        out["bucketOwner"] = value["bucket_owner"]
    return out


def deserialize_cbor(data: dict) -> S3ReportOutputConfiguration:
    out: S3ReportOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bucketPath") is not None:
        out["bucket_path"] = data["bucketPath"]
    if data.get("bucketOwner") is not None:
        out["bucket_owner"] = data["bucketOwner"]
    return out
