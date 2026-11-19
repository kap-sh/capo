"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetIdleRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_ids
    import capo_compute_optimizer.types.idle_max_results
    import capo_compute_optimizer.types.idle_recommendation_filters
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.order_by
    import capo_compute_optimizer.types.resource_arns


class GetIdleRecommendationsRequest(TypedDict, closed=True):
    resource_arns: NotRequired[
        "capo_compute_optimizer.types.resource_arns.ResourceArns"
    ]
    """<p>The ARN that identifies the idle resource.</p>"""
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of idle resource recommendations.</p>"""
    max_results: NotRequired[
        "capo_compute_optimizer.types.idle_max_results.IdleMaxResults"
    ]
    """<p>The maximum number of idle resource recommendations to return with a single request. </p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired[
        "capo_compute_optimizer.types.idle_recommendation_filters.IdleRecommendationFilters"
    ]
    """<p>An array of objects to specify a filter that returns a more specific list of idle resource recommendations.</p>"""
    account_ids: NotRequired["capo_compute_optimizer.types.account_ids.AccountIds"]
    """<p>Return the idle resource recommendations to the specified Amazon Web Services account IDs.</p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to return the idle resource recommendations to specific member accounts.</p> <p>You can only specify one account ID per request.</p>"""
    order_by: NotRequired["capo_compute_optimizer.types.order_by.OrderBy"]
    """<p>The order to sort the idle resource recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIdleRecommendationsRequest) -> dict:
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
        import capo_compute_optimizer.types.idle_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.idle_recommendation_filters.serialize_aws_json_1_0(
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
    if "order_by" in value:
        import capo_compute_optimizer.types.order_by

        out["orderBy"] = capo_compute_optimizer.types.order_by.serialize_aws_json_1_0(
            value["order_by"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIdleRecommendationsRequest:
    out: GetIdleRecommendationsRequest = {}  # type: ignore[typeddict-item]
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
        import capo_compute_optimizer.types.idle_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.idle_recommendation_filters.deserialize_aws_json_1_0(
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
    if data.get("orderBy") is not None:
        import capo_compute_optimizer.types.order_by

        out["order_by"] = (
            capo_compute_optimizer.types.order_by.deserialize_aws_json_1_0(
                data["orderBy"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetIdleRecommendationsRequest) -> dict:
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
        import capo_compute_optimizer.types.idle_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.idle_recommendation_filters.serialize_cbor(
                value["filters"]
            )
        )
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = capo_compute_optimizer.types.account_ids.serialize_cbor(
            value["account_ids"]
        )
    if "order_by" in value:
        import capo_compute_optimizer.types.order_by

        out["orderBy"] = capo_compute_optimizer.types.order_by.serialize_cbor(
            value["order_by"]
        )
    return out


def deserialize_cbor(data: dict) -> GetIdleRecommendationsRequest:
    out: GetIdleRecommendationsRequest = {}  # type: ignore[typeddict-item]
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
        import capo_compute_optimizer.types.idle_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.idle_recommendation_filters.deserialize_cbor(
                data["filters"]
            )
        )
    if data.get("accountIds") is not None:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = capo_compute_optimizer.types.account_ids.deserialize_cbor(
            data["accountIds"]
        )
    if data.get("orderBy") is not None:
        import capo_compute_optimizer.types.order_by

        out["order_by"] = capo_compute_optimizer.types.order_by.deserialize_cbor(
            data["orderBy"]
        )
    return out
