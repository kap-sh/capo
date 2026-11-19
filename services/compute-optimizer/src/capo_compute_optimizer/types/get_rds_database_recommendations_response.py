"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRDSDatabaseRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.get_recommendation_errors
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.rdsdb_recommendations


class GetRDSDatabaseRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p> The token to advance to the next page of Amazon Aurora and RDS database recommendations. </p>"""
    rds_db_recommendations: NotRequired[
        "capo_compute_optimizer.types.rdsdb_recommendations.RDSDBRecommendations"
    ]
    """<p> An array of objects that describe the Amazon Aurora and RDS database recommendations. </p>"""
    errors: NotRequired[
        "capo_compute_optimizer.types.get_recommendation_errors.GetRecommendationErrors"
    ]
    """<p> An array of objects that describe errors of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRDSDatabaseRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "rds_db_recommendations" in value:
        import capo_compute_optimizer.types.rdsdb_recommendations

        out["rdsDBRecommendations"] = (
            capo_compute_optimizer.types.rdsdb_recommendations.serialize_aws_json_1_0(
                value["rds_db_recommendations"]
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


def deserialize_aws_json_1_0(data: dict) -> GetRDSDatabaseRecommendationsResponse:
    out: GetRDSDatabaseRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("rdsDBRecommendations") is not None:
        import capo_compute_optimizer.types.rdsdb_recommendations

        out["rds_db_recommendations"] = (
            capo_compute_optimizer.types.rdsdb_recommendations.deserialize_aws_json_1_0(
                data["rdsDBRecommendations"]
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
def serialize_cbor(value: GetRDSDatabaseRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "rds_db_recommendations" in value:
        import capo_compute_optimizer.types.rdsdb_recommendations

        out["rdsDBRecommendations"] = (
            capo_compute_optimizer.types.rdsdb_recommendations.serialize_cbor(
                value["rds_db_recommendations"]
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


def deserialize_cbor(data: dict) -> GetRDSDatabaseRecommendationsResponse:
    out: GetRDSDatabaseRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("rdsDBRecommendations") is not None:
        import capo_compute_optimizer.types.rdsdb_recommendations

        out["rds_db_recommendations"] = (
            capo_compute_optimizer.types.rdsdb_recommendations.deserialize_cbor(
                data["rdsDBRecommendations"]
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
