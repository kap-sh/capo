"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ListRecommendationSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.filter
    import capo_cost_optimization_hub.types.max_results
    import capo_cost_optimization_hub.types.summary_metrics_list


class ListRecommendationSummariesRequest(TypedDict, closed=True):
    filter: NotRequired["capo_cost_optimization_hub.types.filter.Filter"]
    group_by: "str"
    """<p>The grouping of recommendations by a dimension.</p>"""
    max_results: NotRequired["capo_cost_optimization_hub.types.max_results.MaxResults"]
    """<p>The maximum number of recommendations to be returned for the request.</p>"""
    metrics: NotRequired[
        "capo_cost_optimization_hub.types.summary_metrics_list.SummaryMetricsList"
    ]
    """<p>Additional metrics to be returned for the request. The only valid value is <code>savingsPercentage</code>.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendationSummariesRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_cost_optimization_hub.types.filter

        out["filter"] = capo_cost_optimization_hub.types.filter.serialize_aws_json_1_0(
            value["filter"]
        )
    out["groupBy"] = value["group_by"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "metrics" in value:
        import capo_cost_optimization_hub.types.summary_metrics_list

        out["metrics"] = (
            capo_cost_optimization_hub.types.summary_metrics_list.serialize_aws_json_1_0(
                value["metrics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendationSummariesRequest:
    out: ListRecommendationSummariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_cost_optimization_hub.types.filter

        out["filter"] = (
            capo_cost_optimization_hub.types.filter.deserialize_aws_json_1_0(
                data["filter"]
            )
        )
    if data.get("groupBy") is not None:
        out["group_by"] = data["groupBy"]
    else:
        out["group_by"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("metrics") is not None:
        import capo_cost_optimization_hub.types.summary_metrics_list

        out["metrics"] = (
            capo_cost_optimization_hub.types.summary_metrics_list.deserialize_aws_json_1_0(
                data["metrics"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
