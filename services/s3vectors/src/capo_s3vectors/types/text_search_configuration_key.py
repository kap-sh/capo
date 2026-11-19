"""Generated from Smithy shape ``com.amazonaws.s3vectors#TextSearchConfigurationKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.metadata_key


class TextSearchConfigurationKey(TypedDict, closed=True):
    metadata_key: "capo_s3vectors.types.metadata_key.MetadataKey"
    """<p>The searchable metadata key whose text search configuration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextSearchConfigurationKey) -> dict:
    out: dict = {}
    out["metadataKey"] = value["metadata_key"]
    return out


def deserialize_json(data: dict) -> TextSearchConfigurationKey:
    out: TextSearchConfigurationKey = {}  # type: ignore[typeddict-item]
    if data.get("metadataKey") is not None:
        out["metadata_key"] = data["metadataKey"]
    else:
        out["metadata_key"] = ""
    return out
