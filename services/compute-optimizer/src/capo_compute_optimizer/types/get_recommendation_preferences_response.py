"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRecommendationPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.recommendation_preferences_details


class GetRecommendationPreferencesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of recommendation preferences.</p> <p>This value is null when there are no more pages of recommendation preferences to return.</p>"""
    recommendation_preferences_details: NotRequired[
        "capo_compute_optimizer.types.recommendation_preferences_details.RecommendationPreferencesDetails"
    ]
    """<p>An array of objects that describe recommendation preferences.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationPreferencesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recommendation_preferences_details" in value:
        import capo_compute_optimizer.types.recommendation_preferences_details

        out["recommendationPreferencesDetails"] = (
            capo_compute_optimizer.types.recommendation_preferences_details.serialize_aws_json_1_0(
                value["recommendation_preferences_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecommendationPreferencesResponse:
    out: GetRecommendationPreferencesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("recommendationPreferencesDetails") is not None:
        import capo_compute_optimizer.types.recommendation_preferences_details

        out["recommendation_preferences_details"] = (
            capo_compute_optimizer.types.recommendation_preferences_details.deserialize_aws_json_1_0(
                data["recommendationPreferencesDetails"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRecommendationPreferencesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recommendation_preferences_details" in value:
        import capo_compute_optimizer.types.recommendation_preferences_details

        out["recommendationPreferencesDetails"] = (
            capo_compute_optimizer.types.recommendation_preferences_details.serialize_cbor(
                value["recommendation_preferences_details"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetRecommendationPreferencesResponse:
    out: GetRecommendationPreferencesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("recommendationPreferencesDetails") is not None:
        import capo_compute_optimizer.types.recommendation_preferences_details

        out["recommendation_preferences_details"] = (
            capo_compute_optimizer.types.recommendation_preferences_details.deserialize_cbor(
                data["recommendationPreferencesDetails"]
            )
        )
    return out
