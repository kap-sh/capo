"""Generated from Smithy shape ``com.amazonaws.textract#S3Object``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.s3_bucket
    import capo_textract.types.s3_object_name
    import capo_textract.types.s3_object_version


class S3Object(TypedDict, closed=True):
    bucket: NotRequired["capo_textract.types.s3_bucket.S3Bucket"]
    """<p>The name of the S3 bucket. Note that the # character is not valid in the file name.</p>"""
    name: NotRequired["capo_textract.types.s3_object_name.S3ObjectName"]
    """<p>The file name of the input document. Image files may be in PDF, TIFF, JPEG, or PNG format.</p>"""
    version: NotRequired["capo_textract.types.s3_object_version.S3ObjectVersion"]
    """<p>If the bucket has versioning enabled, you can specify the object version. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Object) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3Object) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_cbor(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
