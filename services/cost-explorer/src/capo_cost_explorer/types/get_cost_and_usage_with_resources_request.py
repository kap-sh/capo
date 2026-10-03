"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostAndUsageWithResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.billing_view_arn
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.granularity
    import capo_cost_explorer.types.group_definitions
    import capo_cost_explorer.types.metric_names
    import capo_cost_explorer.types.next_page_token


class GetCostAndUsageWithResourcesRequest(TypedDict, closed=True):
    time_period: "capo_cost_explorer.types.date_interval.DateInterval"
    """<p>Sets the start and end dates for retrieving Amazon Web Services costs. The range must be within the last 14 days (the start date cannot be earlier than 14 days ago). The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>.</p>"""
    granularity: "capo_cost_explorer.types.granularity.Granularity"
    """<p>Sets the Amazon Web Services cost granularity to <code>MONTHLY</code>, <code>DAILY</code>, or <code>HOURLY</code>. If <code>Granularity</code> isn't set, the response object doesn't include the <code>Granularity</code>, <code>MONTHLY</code>, <code>DAILY</code>, or <code>HOURLY</code>. </p>"""
    filter: "capo_cost_explorer.types.expression.Expression"
    """<p>Filters Amazon Web Services costs by different dimensions. For example, you can specify <code>SERVICE</code> and <code>LINKED_ACCOUNT</code> and get the costs that are associated with that account's usage of that service. You can nest <code>Expression</code> objects to define any combination of dimension filters. For more information, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a>. </p> <p>The <code>GetCostAndUsageWithResources</code> operation requires that you either group by or filter by a <code>ResourceId</code>. It requires the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> <code>"SERVICE = Amazon Elastic Compute Cloud - Compute"</code> in the filter.</p> <p>Valid values for <code>MatchOptions</code> for <code>Dimensions</code> are <code>EQUALS</code> and <code>CASE_SENSITIVE</code>.</p> <p>Valid values for <code>MatchOptions</code> for <code>CostCategories</code> and <code>Tags</code> are <code>EQUALS</code>, <code>ABSENT</code>, and <code>CASE_SENSITIVE</code>. Default values are <code>EQUALS</code> and <code>CASE_SENSITIVE</code>.</p>"""
    metrics: NotRequired["capo_cost_explorer.types.metric_names.MetricNames"]
    """<p>Which metrics are returned in the query. For more information about blended and unblended rates, see <a href="http://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/">Why does the "blended" annotation appear on some line items in my bill?</a>. </p> <p>Valid values are <code>AmortizedCost</code>, <code>BlendedCost</code>, <code>NetAmortizedCost</code>, <code>NetUnblendedCost</code>, <code>NormalizedUsageAmount</code>, <code>UnblendedCost</code>, and <code>UsageQuantity</code>. </p> <note> <p>If you return the <code>UsageQuantity</code> metric, the service aggregates all usage numbers without taking the units into account. For example, if you aggregate <code>usageQuantity</code> across all of Amazon EC2, the results aren't meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hour or GB). To get more meaningful <code>UsageQuantity</code> metrics, filter by <code>UsageType</code> or <code>UsageTypeGroups</code>. </p> </note> <p> <code>Metrics</code> is required for <code>GetCostAndUsageWithResources</code> requests.</p>"""
    group_by: NotRequired["capo_cost_explorer.types.group_definitions.GroupDefinitions"]
    """<p>You can group Amazon Web Services costs using up to two different groups: <code>DIMENSION</code>, <code>TAG</code>, <code>COST_CATEGORY</code>.</p>"""
    billing_view_arn: NotRequired[
        "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostAndUsageWithResourcesRequest) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.date_interval

    out["TimePeriod"] = capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
        value["time_period"]
    )
    import capo_cost_explorer.types.granularity

    out["Granularity"] = capo_cost_explorer.types.granularity.serialize_aws_json_1_1(
        value["granularity"]
    )
    import capo_cost_explorer.types.expression

    out["Filter"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
        value["filter"]
    )
    if "metrics" in value:
        import capo_cost_explorer.types.metric_names

        out["Metrics"] = capo_cost_explorer.types.metric_names.serialize_aws_json_1_1(
            value["metrics"]
        )
    if "group_by" in value:
        import capo_cost_explorer.types.group_definitions

        out["GroupBy"] = (
            capo_cost_explorer.types.group_definitions.serialize_aws_json_1_1(
                value["group_by"]
            )
        )
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostAndUsageWithResourcesRequest:
    out: GetCostAndUsageWithResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_cost_explorer.types.date_interval

        out["time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetCostAndUsageWithResourcesRequest.time_period required"
        )
    if data.get("Granularity") is not None:
        import capo_cost_explorer.types.granularity

        out["granularity"] = (
            capo_cost_explorer.types.granularity.deserialize_aws_json_1_1(
                data["Granularity"]
            )
        )
    else:
        raise DeserializationError(
            "GetCostAndUsageWithResourcesRequest.granularity required"
        )
    if data.get("Filter") is not None:
        import capo_cost_explorer.types.expression

        out["filter"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    else:
        raise DeserializationError(
            "GetCostAndUsageWithResourcesRequest.filter required"
        )
    if data.get("Metrics") is not None:
        import capo_cost_explorer.types.metric_names

        out["metrics"] = capo_cost_explorer.types.metric_names.deserialize_aws_json_1_1(
            data["Metrics"]
        )
    if data.get("GroupBy") is not None:
        import capo_cost_explorer.types.group_definitions

        out["group_by"] = (
            capo_cost_explorer.types.group_definitions.deserialize_aws_json_1_1(
                data["GroupBy"]
            )
        )
    if data.get("BillingViewArn") is not None:
        out["billing_view_arn"] = data["BillingViewArn"]
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
