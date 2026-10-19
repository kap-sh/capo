"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3PublicAccessBlockConfiguration``."""

from typing_extensions import TypedDict


class S3PublicAccessBlockConfiguration(TypedDict, closed=True):
    ignore_public_acls: "bool"
    """<p> Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. </p>"""
    restrict_public_buckets: "bool"
    """<p> Specifies whether Amazon S3 should restrict public bucket policies for this bucket. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3PublicAccessBlockConfiguration) -> dict:
    out: dict = {}
    out["ignorePublicAcls"] = value["ignore_public_acls"]
    out["restrictPublicBuckets"] = value["restrict_public_buckets"]
    return out


def deserialize_json(data: dict) -> S3PublicAccessBlockConfiguration:
    out: S3PublicAccessBlockConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ignorePublicAcls") is not None:
        out["ignore_public_acls"] = data["ignorePublicAcls"]
    else:
        out["ignore_public_acls"] = False
    if data.get("restrictPublicBuckets") is not None:
        out["restrict_public_buckets"] = data["restrictPublicBuckets"]
    else:
        out["restrict_public_buckets"] = False
    return out
