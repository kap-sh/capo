"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryText``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.metadata_key
    import capo_s3vectors.types.query_text_string


class QueryText(TypedDict, closed=True):
    text: "capo_s3vectors.types.query_text_string.QueryTextString"
    """<p>The full-text query string.</p>"""
    metadata_key: "capo_s3vectors.types.metadata_key.MetadataKey"
    """<p>The searchable metadata key to query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryText) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    out["metadataKey"] = value["metadata_key"]
    return out


def deserialize_json(data: dict) -> QueryText:
    out: QueryText = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("metadataKey") is not None:
        out["metadata_key"] = data["metadataKey"]
    else:
        out["metadata_key"] = ""
    return out
