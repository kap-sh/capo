"""Generated from Smithy shape ``com.amazonaws.panorama#OutPutS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.bucket_name
    import capo_panorama.types.object_key


class OutPutS3Location(TypedDict, closed=True):
    bucket_name: "capo_panorama.types.bucket_name.BucketName"
    """<p>The object's bucket.</p>"""
    object_key: "capo_panorama.types.object_key.ObjectKey"
    """<p>The object's key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutPutS3Location) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["ObjectKey"] = value["object_key"]
    return out


def deserialize_json(data: dict) -> OutPutS3Location:
    out: OutPutS3Location = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("ObjectKey") is not None:
        out["object_key"] = data["ObjectKey"]
    else:
        out["object_key"] = ""
    return out
