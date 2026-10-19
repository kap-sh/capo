"""Generated from Smithy shape ``com.amazonaws.qconnect#RecommendationData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.data_summary
    import capo_qconnect.types.document
    import capo_qconnect.types.recommendation_id
    import capo_qconnect.types.recommendation_type
    import capo_qconnect.types.relevance_level
    import capo_qconnect.types.relevance_score


class RecommendationData(TypedDict, closed=True):
    recommendation_id: "capo_qconnect.types.recommendation_id.RecommendationId"
    """<p>The identifier of the recommendation.</p>"""
    document: NotRequired["capo_qconnect.types.document.Document"]
    """<p>The recommended document.</p>"""
    relevance_score: "capo_qconnect.types.relevance_score.RelevanceScore"
    """<p>The relevance score of the recommendation.</p>"""
    relevance_level: NotRequired["capo_qconnect.types.relevance_level.RelevanceLevel"]
    """<p>The relevance level of the recommendation.</p>"""
    type: NotRequired["capo_qconnect.types.recommendation_type.RecommendationType"]
    """<p>The type of recommendation.</p>"""
    data: NotRequired["capo_qconnect.types.data_summary.DataSummary"]
    """<p> Summary of the recommended content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationData) -> dict:
    out: dict = {}
    out["recommendationId"] = value["recommendation_id"]
    if "document" in value:
        import capo_qconnect.types.document

        out["document"] = capo_qconnect.types.document.serialize_json(value["document"])
    out["relevanceScore"] = (
        "NaN"
        if value.get("relevance_score", 0) != value.get("relevance_score", 0)
        else "Infinity"
        if value.get("relevance_score", 0) == float("inf")
        else "-Infinity"
        if value.get("relevance_score", 0) == float("-inf")
        else value.get("relevance_score", 0)
    )
    if "relevance_level" in value:
        out["relevanceLevel"] = value["relevance_level"]
    if "type" in value:
        out["type"] = value["type"]
    if "data" in value:
        import capo_qconnect.types.data_summary

        out["data"] = capo_qconnect.types.data_summary.serialize_json(value["data"])
    return out


def deserialize_json(data: dict) -> RecommendationData:
    out: RecommendationData = {}  # type: ignore[typeddict-item]
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    else:
        out["recommendation_id"] = ""
    if data.get("document") is not None:
        import capo_qconnect.types.document

        out["document"] = capo_qconnect.types.document.deserialize_json(
            data["document"]
        )
    if data.get("relevanceScore") is not None:
        out["relevance_score"] = float(data["relevanceScore"])
    else:
        out["relevance_score"] = 0
    if data.get("relevanceLevel") is not None:
        out["relevance_level"] = data["relevanceLevel"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("data") is not None:
        import capo_qconnect.types.data_summary

        out["data"] = capo_qconnect.types.data_summary.deserialize_json(data["data"])
    return out


def redact_sensitive(value: RecommendationData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document" in value:
        import capo_qconnect.types.document

        out["document"] = capo_qconnect.types.document.redact_sensitive(
            value["document"]
        )
    if "data" in value:
        import capo_qconnect.types.data_summary

        out["data"] = capo_qconnect.types.data_summary.redact_sensitive(value["data"])
    return out
