"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEBSVolumeRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.get_recommendation_errors
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.volume_recommendations


class GetEBSVolumeRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of volume recommendations.</p> <p>This value is null when there are no more pages of volume recommendations to return.</p>"""
    volume_recommendations: NotRequired[
        "capo_compute_optimizer.types.volume_recommendations.VolumeRecommendations"
    ]
    """<p>An array of objects that describe volume recommendations.</p>"""
    errors: NotRequired[
        "capo_compute_optimizer.types.get_recommendation_errors.GetRecommendationErrors"
    ]
    """<p>An array of objects that describe errors of the request.</p> <p>For example, an error is returned if you request recommendations for an unsupported volume.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEBSVolumeRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "volume_recommendations" in value:
        import capo_compute_optimizer.types.volume_recommendations

        out["volumeRecommendations"] = (
            capo_compute_optimizer.types.volume_recommendations.serialize_aws_json_1_0(
                value["volume_recommendations"]
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


def deserialize_aws_json_1_0(data: dict) -> GetEBSVolumeRecommendationsResponse:
    out: GetEBSVolumeRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("volumeRecommendations") is not None:
        import capo_compute_optimizer.types.volume_recommendations

        out["volume_recommendations"] = (
            capo_compute_optimizer.types.volume_recommendations.deserialize_aws_json_1_0(
                data["volumeRecommendations"]
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
def serialize_cbor(value: GetEBSVolumeRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "volume_recommendations" in value:
        import capo_compute_optimizer.types.volume_recommendations

        out["volumeRecommendations"] = (
            capo_compute_optimizer.types.volume_recommendations.serialize_cbor(
                value["volume_recommendations"]
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


def deserialize_cbor(data: dict) -> GetEBSVolumeRecommendationsResponse:
    out: GetEBSVolumeRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("volumeRecommendations") is not None:
        import capo_compute_optimizer.types.volume_recommendations

        out["volume_recommendations"] = (
            capo_compute_optimizer.types.volume_recommendations.deserialize_cbor(
                data["volumeRecommendations"]
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
