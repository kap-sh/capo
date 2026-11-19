"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryScores``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.bm25_score_list


class QueryScores(TypedDict, closed=True):
    fused: NotRequired["float"]
    """<p>The Reciprocal Rank Fusion (RRF) score that combines the vector and full-text rankings. This field is returned only for hybrid requests.</p>"""
    bm25_scores: NotRequired["capo_s3vectors.types.bm25_score_list.Bm25ScoreList"]
    """<p>The BM25 scores for the searchable metadata keys that the result matched.</p>"""
    vector_distance: NotRequired["float"]
    """<p>The distance from the query vector. This field is returned when a hybrid result matches the vector search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryScores) -> dict:
    out: dict = {}
    if "fused" in value:
        out["fused"] = (
            "NaN"
            if value["fused"] != value["fused"]
            else "Infinity"
            if value["fused"] == float("inf")
            else "-Infinity"
            if value["fused"] == float("-inf")
            else value["fused"]
        )
    if "bm25_scores" in value:
        import capo_s3vectors.types.bm25_score_list

        out["bm25Scores"] = capo_s3vectors.types.bm25_score_list.serialize_json(
            value["bm25_scores"]
        )
    if "vector_distance" in value:
        out["vectorDistance"] = (
            "NaN"
            if value["vector_distance"] != value["vector_distance"]
            else "Infinity"
            if value["vector_distance"] == float("inf")
            else "-Infinity"
            if value["vector_distance"] == float("-inf")
            else value["vector_distance"]
        )
    return out


def deserialize_json(data: dict) -> QueryScores:
    out: QueryScores = {}  # type: ignore[typeddict-item]
    if data.get("fused") is not None:
        out["fused"] = float(data["fused"])
    if data.get("bm25Scores") is not None:
        import capo_s3vectors.types.bm25_score_list

        out["bm25_scores"] = capo_s3vectors.types.bm25_score_list.deserialize_json(
            data["bm25Scores"]
        )
    if data.get("vectorDistance") is not None:
        out["vector_distance"] = float(data["vectorDistance"])
    return out
