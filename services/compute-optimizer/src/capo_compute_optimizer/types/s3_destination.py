"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#S3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.destination_bucket
    import capo_compute_optimizer.types.destination_key
    import capo_compute_optimizer.types.metadata_key


class S3Destination(TypedDict, closed=True):
    bucket: NotRequired[
        "capo_compute_optimizer.types.destination_bucket.DestinationBucket"
    ]
    """<p>The name of the Amazon S3 bucket used as the destination of an export file.</p>"""
    key: NotRequired["capo_compute_optimizer.types.destination_key.DestinationKey"]
    """<p>The Amazon S3 bucket key of an export file.</p> <p>The key uniquely identifies the object, or export file, in the S3 bucket.</p>"""
    metadata_key: NotRequired["capo_compute_optimizer.types.metadata_key.MetadataKey"]
    """<p>The Amazon S3 bucket key of a metadata file.</p> <p>The key uniquely identifies the object, or metadata file, in the S3 bucket.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Destination) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    if "metadata_key" in value:
        out["metadataKey"] = value["metadata_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("metadataKey") is not None:
        out["metadata_key"] = data["metadataKey"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3Destination) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    if "metadata_key" in value:
        out["metadataKey"] = value["metadata_key"]
    return out


def deserialize_cbor(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("metadataKey") is not None:
        out["metadata_key"] = data["metadataKey"]
    return out
