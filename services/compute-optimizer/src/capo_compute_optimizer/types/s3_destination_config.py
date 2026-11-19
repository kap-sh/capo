"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#S3DestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.destination_bucket
    import capo_compute_optimizer.types.destination_key_prefix


class S3DestinationConfig(TypedDict, closed=True):
    bucket: NotRequired[
        "capo_compute_optimizer.types.destination_bucket.DestinationBucket"
    ]
    """<p>The name of the Amazon S3 bucket to use as the destination for an export job.</p>"""
    key_prefix: NotRequired[
        "capo_compute_optimizer.types.destination_key_prefix.DestinationKeyPrefix"
    ]
    """<p>The Amazon S3 bucket prefix for an export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3DestinationConfig) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3DestinationConfig:
    out: S3DestinationConfig = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("keyPrefix") is not None:
        out["key_prefix"] = data["keyPrefix"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3DestinationConfig) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    return out


def deserialize_cbor(data: dict) -> S3DestinationConfig:
    out: S3DestinationConfig = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("keyPrefix") is not None:
        out["key_prefix"] = data["keyPrefix"]
    return out
