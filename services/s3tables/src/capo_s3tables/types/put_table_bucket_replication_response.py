"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableBucketReplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.version_token


class PutTableBucketReplicationResponse(TypedDict, closed=True):
    version_token: "capo_s3tables.types.version_token.VersionToken"
    """<p>A new version token representing the updated replication configuration.</p>"""
    status: "str"
    """<p>The status of the replication configuration operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableBucketReplicationResponse) -> dict:
    out: dict = {}
    out["versionToken"] = value["version_token"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> PutTableBucketReplicationResponse:
    out: PutTableBucketReplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("versionToken") is not None:
        out["version_token"] = data["versionToken"]
    else:
        out["version_token"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
