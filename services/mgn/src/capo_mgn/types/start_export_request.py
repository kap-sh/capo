"""Generated from Smithy shape ``com.amazonaws.mgn#StartExportRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.s3_bucket_name
    import capo_mgn.types.s3_key
    import capo_mgn.types.tags_map


class StartExportRequest(TypedDict, closed=True):
    s3_bucket: "capo_mgn.types.s3_bucket_name.S3BucketName"
    """<p>Start export request s3 bucket.</p>"""
    s3_key: "capo_mgn.types.s3_key.S3Key"
    """<p>Start export request s3key.</p>"""
    s3_bucket_owner: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Start export request s3 bucket owner.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Start export request tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExportRequest) -> dict:
    out: dict = {}
    out["s3Bucket"] = value["s3_bucket"]
    out["s3Key"] = value["s3_key"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartExportRequest:
    out: StartExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("s3Bucket") is not None:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        raise DeserializationError("StartExportRequest.s3_bucket required")
    if data.get("s3Key") is not None:
        out["s3_key"] = data["s3Key"]
    else:
        raise DeserializationError("StartExportRequest.s3_key required")
    if data.get("s3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: StartExportRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
