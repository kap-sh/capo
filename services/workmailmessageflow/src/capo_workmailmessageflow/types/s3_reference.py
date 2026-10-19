"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#S3Reference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmailmessageflow.types.s3_bucket_id_type
    import capo_workmailmessageflow.types.s3_key_id_type
    import capo_workmailmessageflow.types.s3_version_type


class S3Reference(TypedDict, closed=True):
    bucket: "capo_workmailmessageflow.types.s3_bucket_id_type.s3BucketIdType"
    """<p>The S3 bucket name.</p>"""
    key: "capo_workmailmessageflow.types.s3_key_id_type.s3KeyIdType"
    """<p>The S3 key object name.</p>"""
    object_version: NotRequired[
        "capo_workmailmessageflow.types.s3_version_type.s3VersionType"
    ]
    """<p>If you enable versioning for the bucket, you can specify the object version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Reference) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    if "object_version" in value:
        out["objectVersion"] = value["object_version"]
    return out


def deserialize_json(data: dict) -> S3Reference:
    out: S3Reference = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("objectVersion") is not None:
        out["object_version"] = data["objectVersion"]
    return out
