"""Generated from Smithy shape ``com.amazonaws.appstream#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.s3_bucket
    import capo_appstream.types.s3_key


class S3Location(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_appstream.types.s3_bucket.S3Bucket"]
    """<p>The S3 bucket of the S3 object.</p>"""
    s3_key: NotRequired["capo_appstream.types.s3_key.S3Key"]
    """<p>The S3 key of the S3 object.</p> <p>This is required when used for the following:</p> <ul> <li> <p>IconS3Location (Actions: CreateApplication and UpdateApplication)</p> </li> <li> <p>SessionScriptS3Location (Actions: CreateFleet and UpdateFleet)</p> </li> <li> <p>ScriptDetails (Actions: CreateAppBlock)</p> </li> <li> <p>SourceS3Location when creating an app block with <code>CUSTOM</code> PackagingType (Actions: CreateAppBlock)</p> </li> <li> <p>SourceS3Location when creating an app block with <code>APPSTREAM2</code> PackagingType, and using an existing application package (VHD file). In this case, <code>S3Key</code> refers to the VHD file. If a new application package is required, then <code>S3Key</code> is not required. (Actions: CreateAppBlock)</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Location) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    if data.get("S3Key") is not None:
        out["s3_key"] = data["S3Key"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3Location) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    return out


def deserialize_cbor(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    if data.get("S3Key") is not None:
        out["s3_key"] = data["S3Key"]
    return out
