"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceQualityMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.relevance_metrics


class AudienceQualityMetrics(TypedDict, closed=True):
    relevance_metrics: "capo_cleanroomsml.types.relevance_metrics.RelevanceMetrics"
    """<p>The relevance scores of the generated audience.</p>"""
    recall_metric: NotRequired["float"]
    """<p>The recall score of the generated audience. Recall is the percentage of the most similar users (by default, the most similar 20%) from a sample of the training data that are included in the seed audience by the audience generation job. Values range from 0-1, larger values indicate a better audience. A recall value approximately equal to the maximum bin size indicates that the audience model is equivalent to random selection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceQualityMetrics) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.relevance_metrics

    out["relevanceMetrics"] = capo_cleanroomsml.types.relevance_metrics.serialize_json(
        value["relevance_metrics"]
    )
    if "recall_metric" in value:
        out["recallMetric"] = (
            "NaN"
            if value["recall_metric"] != value["recall_metric"]
            else "Infinity"
            if value["recall_metric"] == float("inf")
            else "-Infinity"
            if value["recall_metric"] == float("-inf")
            else value["recall_metric"]
        )
    return out


def deserialize_json(data: dict) -> AudienceQualityMetrics:
    out: AudienceQualityMetrics = {}  # type: ignore[typeddict-item]
    if data.get("relevanceMetrics") is not None:
        import capo_cleanroomsml.types.relevance_metrics

        out["relevance_metrics"] = (
            capo_cleanroomsml.types.relevance_metrics.deserialize_json(
                data["relevanceMetrics"]
            )
        )
    else:
        out["relevance_metrics"] = []
    if data.get("recallMetric") is not None:
        out["recall_metric"] = float(data["recallMetric"])
    return out
