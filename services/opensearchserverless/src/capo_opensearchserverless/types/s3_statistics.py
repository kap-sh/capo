"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#S3Statistics``."""

from typing_extensions import NotRequired, TypedDict


class S3Statistics(TypedDict, closed=True):
    objects_discovered: NotRequired["int"]
    """<p>The number of Amazon S3 objects discovered for ingestion.</p>"""
    objects_ingested: NotRequired["int"]
    """<p>The number of Amazon S3 objects successfully ingested.</p>"""
    objects_failed: NotRequired["int"]
    """<p>The number of Amazon S3 objects that failed to be ingested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Statistics) -> dict:
    out: dict = {}
    if "objects_discovered" in value:
        out["objectsDiscovered"] = value["objects_discovered"]
    if "objects_ingested" in value:
        out["objectsIngested"] = value["objects_ingested"]
    if "objects_failed" in value:
        out["objectsFailed"] = value["objects_failed"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Statistics:
    out: S3Statistics = {}  # type: ignore[typeddict-item]
    if data.get("objectsDiscovered") is not None:
        out["objects_discovered"] = data["objectsDiscovered"]
    if data.get("objectsIngested") is not None:
        out["objects_ingested"] = data["objectsIngested"]
    if data.get("objectsFailed") is not None:
        out["objects_failed"] = data["objectsFailed"]
    return out
