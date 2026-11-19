"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetIdleRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.idle_recommendation_errors
    import capo_compute_optimizer.types.idle_recommendations
    import capo_compute_optimizer.types.next_token


class GetIdleRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of idle resource recommendations.</p>"""
    idle_recommendations: NotRequired[
        "capo_compute_optimizer.types.idle_recommendations.IdleRecommendations"
    ]
    """<p>An array of objects that describe the idle resource recommendations.</p>"""
    errors: NotRequired[
        "capo_compute_optimizer.types.idle_recommendation_errors.IdleRecommendationErrors"
    ]
    """<p>An array of objects that describe errors of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIdleRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "idle_recommendations" in value:
        import capo_compute_optimizer.types.idle_recommendations

        out["idleRecommendations"] = (
            capo_compute_optimizer.types.idle_recommendations.serialize_aws_json_1_0(
                value["idle_recommendations"]
            )
        )
    if "errors" in value:
        import capo_compute_optimizer.types.idle_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.idle_recommendation_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIdleRecommendationsResponse:
    out: GetIdleRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("idleRecommendations") is not None:
        import capo_compute_optimizer.types.idle_recommendations

        out["idle_recommendations"] = (
            capo_compute_optimizer.types.idle_recommendations.deserialize_aws_json_1_0(
                data["idleRecommendations"]
            )
        )
    if data.get("errors") is not None:
        import capo_compute_optimizer.types.idle_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.idle_recommendation_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetIdleRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "idle_recommendations" in value:
        import capo_compute_optimizer.types.idle_recommendations

        out["idleRecommendations"] = (
            capo_compute_optimizer.types.idle_recommendations.serialize_cbor(
                value["idle_recommendations"]
            )
        )
    if "errors" in value:
        import capo_compute_optimizer.types.idle_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.idle_recommendation_errors.serialize_cbor(
                value["errors"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetIdleRecommendationsResponse:
    out: GetIdleRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("idleRecommendations") is not None:
        import capo_compute_optimizer.types.idle_recommendations

        out["idle_recommendations"] = (
            capo_compute_optimizer.types.idle_recommendations.deserialize_cbor(
                data["idleRecommendations"]
            )
        )
    if data.get("errors") is not None:
        import capo_compute_optimizer.types.idle_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.idle_recommendation_errors.deserialize_cbor(
                data["errors"]
            )
        )
    return out
