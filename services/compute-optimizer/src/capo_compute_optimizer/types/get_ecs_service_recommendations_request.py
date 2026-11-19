"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetECSServiceRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_ids
    import capo_compute_optimizer.types.ecs_service_recommendation_filters
    import capo_compute_optimizer.types.max_results
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.service_arns


class GetECSServiceRecommendationsRequest(TypedDict, closed=True):
    service_arns: NotRequired["capo_compute_optimizer.types.service_arns.ServiceArns"]
    """<p> The ARN that identifies the Amazon ECS service. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name</code> </p>"""
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p> The token to advance to the next page of Amazon ECS service recommendations. </p>"""
    max_results: NotRequired["capo_compute_optimizer.types.max_results.MaxResults"]
    """<p> The maximum number of Amazon ECS service recommendations to return with a single request. </p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired[
        "capo_compute_optimizer.types.ecs_service_recommendation_filters.ECSServiceRecommendationFilters"
    ]
    """<p> An array of objects to specify a filter that returns a more specific list of Amazon ECS service recommendations. </p>"""
    account_ids: NotRequired["capo_compute_optimizer.types.account_ids.AccountIds"]
    """<p> Return the Amazon ECS service recommendations to the specified Amazon Web Services account IDs. </p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to return the Amazon ECS service recommendations to specific member accounts.</p> <p>You can only specify one account ID per request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetECSServiceRecommendationsRequest) -> dict:
    out: dict = {}
    if "service_arns" in value:
        import capo_compute_optimizer.types.service_arns

        out["serviceArns"] = (
            capo_compute_optimizer.types.service_arns.serialize_aws_json_1_0(
                value["service_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_compute_optimizer.types.ecs_service_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_filters.serialize_aws_json_1_0(
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
    return out


def deserialize_aws_json_1_0(data: dict) -> GetECSServiceRecommendationsRequest:
    out: GetECSServiceRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArns") is not None:
        import capo_compute_optimizer.types.service_arns

        out["service_arns"] = (
            capo_compute_optimizer.types.service_arns.deserialize_aws_json_1_0(
                data["serviceArns"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.ecs_service_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_filters.deserialize_aws_json_1_0(
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetECSServiceRecommendationsRequest) -> dict:
    out: dict = {}
    if "service_arns" in value:
        import capo_compute_optimizer.types.service_arns

        out["serviceArns"] = capo_compute_optimizer.types.service_arns.serialize_cbor(
            value["service_arns"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_compute_optimizer.types.ecs_service_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_filters.serialize_cbor(
                value["filters"]
            )
        )
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = capo_compute_optimizer.types.account_ids.serialize_cbor(
            value["account_ids"]
        )
    return out


def deserialize_cbor(data: dict) -> GetECSServiceRecommendationsRequest:
    out: GetECSServiceRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArns") is not None:
        import capo_compute_optimizer.types.service_arns

        out["service_arns"] = (
            capo_compute_optimizer.types.service_arns.deserialize_cbor(
                data["serviceArns"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.ecs_service_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_filters.deserialize_cbor(
                data["filters"]
            )
        )
    if data.get("accountIds") is not None:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = capo_compute_optimizer.types.account_ids.deserialize_cbor(
            data["accountIds"]
        )
    return out
