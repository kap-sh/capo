"""Generated from Smithy shape ``com.amazonaws.codepipeline#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.s3_bucket
    import capo_codepipeline.types.s3_key


class S3Location(TypedDict, closed=True):
    bucket: NotRequired["capo_codepipeline.types.s3_bucket.S3Bucket"]
    """<p>The Amazon S3 artifact bucket for an action's artifacts.</p>"""
    key: NotRequired["capo_codepipeline.types.s3_key.S3Key"]
    """<p>The artifact name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("key") is not None:
        out["key"] = data["key"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    return out


def deserialize_cbor(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("key") is not None:
        out["key"] = data["key"]
    return out
