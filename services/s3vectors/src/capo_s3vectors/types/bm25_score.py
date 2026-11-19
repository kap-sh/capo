"""Generated from Smithy shape ``com.amazonaws.s3vectors#Bm25Score``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.metadata_key


class Bm25Score(TypedDict, closed=True):
    metadata_key: "capo_s3vectors.types.metadata_key.MetadataKey"
    """<p>The searchable metadata key that the score applies to.</p>"""
    score: "float"
    """<p>The BM25 relevance score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bm25Score) -> dict:
    out: dict = {}
    out["metadataKey"] = value["metadata_key"]
    out["score"] = (
        "NaN"
        if value["score"] != value["score"]
        else "Infinity"
        if value["score"] == float("inf")
        else "-Infinity"
        if value["score"] == float("-inf")
        else value["score"]
    )
    return out


def deserialize_json(data: dict) -> Bm25Score:
    out: Bm25Score = {}  # type: ignore[typeddict-item]
    if data.get("metadataKey") is not None:
        out["metadata_key"] = data["metadataKey"]
    else:
        out["metadata_key"] = ""
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    else:
        out["score"] = 0.0
    return out
