"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetAutoScalingGroupRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.auto_scaling_group_recommendations
    import capo_compute_optimizer.types.get_recommendation_errors
    import capo_compute_optimizer.types.next_token


class GetAutoScalingGroupRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of Auto Scaling group recommendations.</p> <p>This value is null when there are no more pages of Auto Scaling group recommendations to return.</p>"""
    auto_scaling_group_recommendations: NotRequired[
        "capo_compute_optimizer.types.auto_scaling_group_recommendations.AutoScalingGroupRecommendations"
    ]
    """<p>An array of objects that describe Auto Scaling group recommendations.</p>"""
    errors: NotRequired[
        "capo_compute_optimizer.types.get_recommendation_errors.GetRecommendationErrors"
    ]
    """<p>An array of objects that describe errors of the request.</p> <p>For example, an error is returned if you request recommendations for an unsupported Auto Scaling group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutoScalingGroupRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "auto_scaling_group_recommendations" in value:
        import capo_compute_optimizer.types.auto_scaling_group_recommendations

        out["autoScalingGroupRecommendations"] = (
            capo_compute_optimizer.types.auto_scaling_group_recommendations.serialize_aws_json_1_0(
                value["auto_scaling_group_recommendations"]
            )
        )
    if "errors" in value:
        import capo_compute_optimizer.types.get_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.get_recommendation_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutoScalingGroupRecommendationsResponse:
    out: GetAutoScalingGroupRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("autoScalingGroupRecommendations") is not None:
        import capo_compute_optimizer.types.auto_scaling_group_recommendations

        out["auto_scaling_group_recommendations"] = (
            capo_compute_optimizer.types.auto_scaling_group_recommendations.deserialize_aws_json_1_0(
                data["autoScalingGroupRecommendations"]
            )
        )
    if data.get("errors") is not None:
        import capo_compute_optimizer.types.get_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.get_recommendation_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAutoScalingGroupRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "auto_scaling_group_recommendations" in value:
        import capo_compute_optimizer.types.auto_scaling_group_recommendations

        out["autoScalingGroupRecommendations"] = (
            capo_compute_optimizer.types.auto_scaling_group_recommendations.serialize_cbor(
                value["auto_scaling_group_recommendations"]
            )
        )
    if "errors" in value:
        import capo_compute_optimizer.types.get_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.get_recommendation_errors.serialize_cbor(
                value["errors"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetAutoScalingGroupRecommendationsResponse:
    out: GetAutoScalingGroupRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("autoScalingGroupRecommendations") is not None:
        import capo_compute_optimizer.types.auto_scaling_group_recommendations

        out["auto_scaling_group_recommendations"] = (
            capo_compute_optimizer.types.auto_scaling_group_recommendations.deserialize_cbor(
                data["autoScalingGroupRecommendations"]
            )
        )
    if data.get("errors") is not None:
        import capo_compute_optimizer.types.get_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.get_recommendation_errors.deserialize_cbor(
                data["errors"]
            )
        )
    return out
