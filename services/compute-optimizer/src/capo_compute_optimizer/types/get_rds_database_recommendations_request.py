"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRDSDatabaseRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_ids
    import capo_compute_optimizer.types.max_results
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.rdsdb_recommendation_filters
    import capo_compute_optimizer.types.recommendation_preferences
    import capo_compute_optimizer.types.resource_arns


class GetRDSDatabaseRecommendationsRequest(TypedDict, closed=True):
    resource_arns: NotRequired[
        "capo_compute_optimizer.types.resource_arns.ResourceArns"
    ]
    """<p> The ARN that identifies the Amazon Aurora or RDS database. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:rds:{region}:{accountId}:db:{resourceName}</code> </p> <p> The following is the format of a DB Cluster ARN: </p> <p> <code>arn:aws:rds:{region}:{accountId}:cluster:{resourceName}</code> </p>"""
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p> The token to advance to the next page of Amazon Aurora and RDS database recommendations. </p>"""
    max_results: NotRequired["capo_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of Amazon Aurora and RDS database recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired[
        "capo_compute_optimizer.types.rdsdb_recommendation_filters.RDSDBRecommendationFilters"
    ]
    """<p> An array of objects to specify a filter that returns a more specific list of Amazon Aurora and RDS database recommendations. </p>"""
    account_ids: NotRequired["capo_compute_optimizer.types.account_ids.AccountIds"]
    """<p> Return the Amazon Aurora and RDS database recommendations to the specified Amazon Web Services account IDs. </p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to return the Amazon Aurora and RDS database recommendations to specific member accounts.</p> <p>You can only specify one account ID per request.</p>"""
    recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRDSDatabaseRecommendationsRequest) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import capo_compute_optimizer.types.resource_arns

        out["resourceArns"] = (
            capo_compute_optimizer.types.resource_arns.serialize_aws_json_1_0(
                value["resource_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_compute_optimizer.types.rdsdb_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.rdsdb_recommendation_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = (
            capo_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "recommendation_preferences" in value:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendationPreferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.serialize_aws_json_1_0(
                value["recommendation_preferences"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRDSDatabaseRecommendationsRequest:
    out: GetRDSDatabaseRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArns") is not None:
        import capo_compute_optimizer.types.resource_arns

        out["resource_arns"] = (
            capo_compute_optimizer.types.resource_arns.deserialize_aws_json_1_0(
                data["resourceArns"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.rdsdb_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.rdsdb_recommendation_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if data.get("accountIds") is not None:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = (
            capo_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if data.get("recommendationPreferences") is not None:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendation_preferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.deserialize_aws_json_1_0(
                data["recommendationPreferences"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRDSDatabaseRecommendationsRequest) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import capo_compute_optimizer.types.resource_arns

        out["resourceArns"] = capo_compute_optimizer.types.resource_arns.serialize_cbor(
            value["resource_arns"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_compute_optimizer.types.rdsdb_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.rdsdb_recommendation_filters.serialize_cbor(
                value["filters"]
            )
        )
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = capo_compute_optimizer.types.account_ids.serialize_cbor(
            value["account_ids"]
        )
    if "recommendation_preferences" in value:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendationPreferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.serialize_cbor(
                value["recommendation_preferences"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetRDSDatabaseRecommendationsRequest:
    out: GetRDSDatabaseRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArns") is not None:
        import capo_compute_optimizer.types.resource_arns

        out["resource_arns"] = (
            capo_compute_optimizer.types.resource_arns.deserialize_cbor(
                data["resourceArns"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.rdsdb_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.rdsdb_recommendation_filters.deserialize_cbor(
                data["filters"]
            )
        )
    if data.get("accountIds") is not None:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = capo_compute_optimizer.types.account_ids.deserialize_cbor(
            data["accountIds"]
        )
    if data.get("recommendationPreferences") is not None:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendation_preferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.deserialize_cbor(
                data["recommendationPreferences"]
            )
        )
    return out
