"""Generated from Smithy shape ``com.amazonaws.signer#S3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signer.types.bucket_name
    import capo_signer.types.key
    import capo_signer.types.version


class S3Source(TypedDict, closed=True):
    bucket_name: "capo_signer.types.bucket_name.BucketName"
    """<p>Name of the S3 bucket.</p>"""
    key: "capo_signer.types.key.Key"
    """<p>Key name of the bucket object that contains your unsigned code.</p>"""
    version: "capo_signer.types.version.Version"
    """<p>Version of your source image in your version enabled S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Source) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["key"] = value["key"]
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> S3Source:
    out: S3Source = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    return out
