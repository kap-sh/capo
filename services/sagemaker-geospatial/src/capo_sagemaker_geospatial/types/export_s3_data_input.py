"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportS3DataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.s3_uri


class ExportS3DataInput(TypedDict, closed=True):
    s3_uri: "capo_sagemaker_geospatial.types.s3_uri.S3Uri"
    """<p>The URL to the Amazon S3 data input.</p>"""
    kms_key_id: NotRequired["capo_sagemaker_geospatial.types.kms_key.KmsKey"]
    """<p>The Key Management Service key ID for server-side encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportS3DataInput) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> ExportS3DataInput:
    out: ExportS3DataInput = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
