"""Generated from Smithy shape ``com.amazonaws.datazone#S3File``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.s3_object_key


class S3File(TypedDict, closed=True):
    key: "capo_datazone.types.s3_object_key.S3ObjectKey"
    """<p>The key of the Amazon Simple Storage Service object to import.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3File) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3File:
    out: S3File = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3File.key required")
    return out
