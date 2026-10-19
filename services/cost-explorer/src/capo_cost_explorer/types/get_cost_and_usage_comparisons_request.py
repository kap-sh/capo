"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostAndUsageComparisonsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.billing_view_arn
    import capo_cost_explorer.types.cost_and_usage_comparisons_max_results
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.group_definitions
    import capo_cost_explorer.types.metric_name
    import capo_cost_explorer.types.next_page_token


class GetCostAndUsageComparisonsRequest(TypedDict, closed=True):
    billing_view_arn: NotRequired[
        "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    baseline_time_period: "capo_cost_explorer.types.date_interval.DateInterval"
    """<p>The reference time period for comparison. This time period serves as the baseline against which other cost and usage data will be compared. The interval must start and end on the first day of a month, with a duration of exactly one month.</p>"""
    comparison_time_period: "capo_cost_explorer.types.date_interval.DateInterval"
    """<p>The comparison time period for analysis. This time period's cost and usage data will be compared against the baseline time period. The interval must start and end on the first day of a month, with a duration of exactly one month.</p>"""
    metric_for_comparison: "capo_cost_explorer.types.metric_name.MetricName"
    """<p>The cost and usage metric to compare. Valid values are <code>AmortizedCost</code>, <code>BlendedCost</code>, <code>NetAmortizedCost</code>, <code>NetUnblendedCost</code>, <code>NormalizedUsageAmount</code>, <code>UnblendedCost</code>, and <code>UsageQuantity</code>.</p>"""
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    group_by: NotRequired["capo_cost_explorer.types.group_definitions.GroupDefinitions"]
    """<p>You can group results using the attributes <code>DIMENSION</code>, <code>TAG</code>, and <code>COST_CATEGORY</code>. </p>"""
    max_results: NotRequired[
        "capo_cost_explorer.types.cost_and_usage_comparisons_max_results.CostAndUsageComparisonsMaxResults"
    ]
    """<p>The maximum number of results that are returned for the request.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of paginated results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostAndUsageComparisonsRequest) -> dict:
    out: dict = {}
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    import capo_cost_explorer.types.date_interval

    out["BaselineTimePeriod"] = (
        capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
            value["baseline_time_period"]
        )
    )
    import capo_cost_explorer.types.date_interval

    out["ComparisonTimePeriod"] = (
        capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
            value["comparison_time_period"]
        )
    )
    out["MetricForComparison"] = value["metric_for_comparison"]
    if "filter" in value:
        import capo_cost_explorer.types.expression

        out["Filter"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    if "group_by" in value:
        import capo_cost_explorer.types.group_definitions

        out["GroupBy"] = (
            capo_cost_explorer.types.group_definitions.serialize_aws_json_1_1(
                value["group_by"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostAndUsageComparisonsRequest:
    out: GetCostAndUsageComparisonsRequest = {}  # type: ignore[typeddict-item]
    if data.get("BillingViewArn") is not None:
        out["billing_view_arn"] = data["BillingViewArn"]
    if data.get("BaselineTimePeriod") is not None:
        import capo_cost_explorer.types.date_interval

        out["baseline_time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["BaselineTimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetCostAndUsageComparisonsRequest.baseline_time_period required"
        )
    if data.get("ComparisonTimePeriod") is not None:
        import capo_cost_explorer.types.date_interval

        out["comparison_time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["ComparisonTimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetCostAndUsageComparisonsRequest.comparison_time_period required"
        )
    if data.get("MetricForComparison") is not None:
        out["metric_for_comparison"] = data["MetricForComparison"]
    else:
        out["metric_for_comparison"] = ""
    if data.get("Filter") is not None:
        import capo_cost_explorer.types.expression

        out["filter"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("GroupBy") is not None:
        import capo_cost_explorer.types.group_definitions

        out["group_by"] = (
            capo_cost_explorer.types.group_definitions.deserialize_aws_json_1_1(
                data["GroupBy"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
