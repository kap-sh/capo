"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEC2InstanceRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.get_recommendation_errors
    import capo_compute_optimizer.types.instance_recommendations
    import capo_compute_optimizer.types.next_token


class GetEC2InstanceRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of instance recommendations.</p> <p>This value is null when there are no more pages of instance recommendations to return.</p>"""
    instance_recommendations: NotRequired[
        "capo_compute_optimizer.types.instance_recommendations.InstanceRecommendations"
    ]
    """<p>An array of objects that describe instance recommendations.</p>"""
    errors: NotRequired[
        "capo_compute_optimizer.types.get_recommendation_errors.GetRecommendationErrors"
    ]
    """<p>An array of objects that describe errors of the request.</p> <p>For example, an error is returned if you request recommendations for an instance of an unsupported instance family.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEC2InstanceRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "instance_recommendations" in value:
        import capo_compute_optimizer.types.instance_recommendations

        out["instanceRecommendations"] = (
            capo_compute_optimizer.types.instance_recommendations.serialize_aws_json_1_0(
                value["instance_recommendations"]
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


def deserialize_aws_json_1_0(data: dict) -> GetEC2InstanceRecommendationsResponse:
    out: GetEC2InstanceRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("instanceRecommendations") is not None:
        import capo_compute_optimizer.types.instance_recommendations

        out["instance_recommendations"] = (
            capo_compute_optimizer.types.instance_recommendations.deserialize_aws_json_1_0(
                data["instanceRecommendations"]
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
def serialize_cbor(value: GetEC2InstanceRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "instance_recommendations" in value:
        import capo_compute_optimizer.types.instance_recommendations

        out["instanceRecommendations"] = (
            capo_compute_optimizer.types.instance_recommendations.serialize_cbor(
                value["instance_recommendations"]
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


def deserialize_cbor(data: dict) -> GetEC2InstanceRecommendationsResponse:
    out: GetEC2InstanceRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("instanceRecommendations") is not None:
        import capo_compute_optimizer.types.instance_recommendations

        out["instance_recommendations"] = (
            capo_compute_optimizer.types.instance_recommendations.deserialize_cbor(
                data["instanceRecommendations"]
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
