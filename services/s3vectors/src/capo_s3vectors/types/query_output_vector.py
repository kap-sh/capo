"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryOutputVector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.query_scores
    import capo_s3vectors.types.vector_key
    import capo_s3vectors.types.vector_metadata


class QueryOutputVector(TypedDict, closed=True):
    distance: NotRequired["float"]
    """<p>The measure of similarity between the vector in the response and the query vector.</p>"""
    scores: NotRequired["capo_s3vectors.types.query_scores.QueryScores"]
    """<p>The relevance scores for a full-text-only or hybrid result, when requested through <code>returnScores</code>.</p>"""
    key: "capo_s3vectors.types.vector_key.VectorKey"
    """<p>The key of the matching vector.</p>"""
    metadata: NotRequired["capo_s3vectors.types.vector_metadata.VectorMetadata"]
    """<p>The metadata associated with the vector, if requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryOutputVector) -> dict:
    out: dict = {}
    if "distance" in value:
        out["distance"] = (
            "NaN"
            if value["distance"] != value["distance"]
            else "Infinity"
            if value["distance"] == float("inf")
            else "-Infinity"
            if value["distance"] == float("-inf")
            else value["distance"]
        )
    if "scores" in value:
        import capo_s3vectors.types.query_scores

        out["scores"] = capo_s3vectors.types.query_scores.serialize_json(
            value["scores"]
        )
    out["key"] = value["key"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> QueryOutputVector:
    out: QueryOutputVector = {}  # type: ignore[typeddict-item]
    if data.get("distance") is not None:
        out["distance"] = float(data["distance"])
    if data.get("scores") is not None:
        import capo_s3vectors.types.query_scores

        out["scores"] = capo_s3vectors.types.query_scores.deserialize_json(
            data["scores"]
        )
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    return out
