"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetLicenseRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.get_recommendation_errors
    import capo_compute_optimizer.types.license_recommendations
    import capo_compute_optimizer.types.next_token


class GetLicenseRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p> The token to use to advance to the next page of license recommendations. </p>"""
    license_recommendations: NotRequired[
        "capo_compute_optimizer.types.license_recommendations.LicenseRecommendations"
    ]
    """<p> An array of objects that describe license recommendations. </p>"""
    errors: NotRequired[
        "capo_compute_optimizer.types.get_recommendation_errors.GetRecommendationErrors"
    ]
    """<p> An array of objects that describe errors of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetLicenseRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "license_recommendations" in value:
        import capo_compute_optimizer.types.license_recommendations

        out["licenseRecommendations"] = (
            capo_compute_optimizer.types.license_recommendations.serialize_aws_json_1_0(
                value["license_recommendations"]
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


def deserialize_aws_json_1_0(data: dict) -> GetLicenseRecommendationsResponse:
    out: GetLicenseRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("licenseRecommendations") is not None:
        import capo_compute_optimizer.types.license_recommendations

        out["license_recommendations"] = (
            capo_compute_optimizer.types.license_recommendations.deserialize_aws_json_1_0(
                data["licenseRecommendations"]
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
def serialize_cbor(value: GetLicenseRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "license_recommendations" in value:
        import capo_compute_optimizer.types.license_recommendations

        out["licenseRecommendations"] = (
            capo_compute_optimizer.types.license_recommendations.serialize_cbor(
                value["license_recommendations"]
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


def deserialize_cbor(data: dict) -> GetLicenseRecommendationsResponse:
    out: GetLicenseRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("licenseRecommendations") is not None:
        import capo_compute_optimizer.types.license_recommendations

        out["license_recommendations"] = (
            capo_compute_optimizer.types.license_recommendations.deserialize_cbor(
                data["licenseRecommendations"]
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
