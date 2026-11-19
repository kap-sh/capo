"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRecommendationSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.recommendation_summaries


class GetRecommendationSummariesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of recommendation summaries.</p> <p>This value is null when there are no more pages of recommendation summaries to return.</p>"""
    recommendation_summaries: NotRequired[
        "capo_compute_optimizer.types.recommendation_summaries.RecommendationSummaries"
    ]
    """<p>An array of objects that summarize a recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationSummariesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recommendation_summaries" in value:
        import capo_compute_optimizer.types.recommendation_summaries

        out["recommendationSummaries"] = (
            capo_compute_optimizer.types.recommendation_summaries.serialize_aws_json_1_0(
                value["recommendation_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecommendationSummariesResponse:
    out: GetRecommendationSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("recommendationSummaries") is not None:
        import capo_compute_optimizer.types.recommendation_summaries

        out["recommendation_summaries"] = (
            capo_compute_optimizer.types.recommendation_summaries.deserialize_aws_json_1_0(
                data["recommendationSummaries"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRecommendationSummariesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recommendation_summaries" in value:
        import capo_compute_optimizer.types.recommendation_summaries

        out["recommendationSummaries"] = (
            capo_compute_optimizer.types.recommendation_summaries.serialize_cbor(
                value["recommendation_summaries"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetRecommendationSummariesResponse:
    out: GetRecommendationSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("recommendationSummaries") is not None:
        import capo_compute_optimizer.types.recommendation_summaries

        out["recommendation_summaries"] = (
            capo_compute_optimizer.types.recommendation_summaries.deserialize_cbor(
                data["recommendationSummaries"]
            )
        )
    return out
