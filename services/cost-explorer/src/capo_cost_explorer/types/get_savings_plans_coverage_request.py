"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlansCoverageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.granularity
    import capo_cost_explorer.types.group_definitions
    import capo_cost_explorer.types.max_results
    import capo_cost_explorer.types.metric_names
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.sort_definition


class GetSavingsPlansCoverageRequest(TypedDict, closed=True):
    time_period: "capo_cost_explorer.types.date_interval.DateInterval"
    """<p>The time period that you want the usage and costs for. The <code>Start</code> date must be within 13 months. The <code>End</code> date must be after the <code>Start</code> date, and before the current date. Future dates can't be used as an <code>End</code> date.</p>"""
    group_by: NotRequired["capo_cost_explorer.types.group_definitions.GroupDefinitions"]
    """<p>You can group the data using the attributes <code>INSTANCE_FAMILY</code>, <code>REGION</code>, or <code>SERVICE</code>.</p>"""
    granularity: NotRequired["capo_cost_explorer.types.granularity.Granularity"]
    """<p>The granularity of the Amazon Web Services cost data for your Savings Plans. <code>Granularity</code> can't be set if <code>GroupBy</code> is set.</p> <p>The <code>GetSavingsPlansCoverage</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>"""
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    """<p>Filters Savings Plans coverage data by dimensions. You can filter data for Savings Plans usage with the following dimensions:</p> <ul> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>SERVICE</code> </p> </li> <li> <p> <code>INSTANCE_FAMILY</code> </p> </li> </ul> <p> <code>GetSavingsPlansCoverage</code> uses the same <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object as the other operations, but only <code>AND</code> is supported among each dimension. If there are multiple values for a dimension, they are OR'd together.</p> <p>Cost category is also supported.</p>"""
    metrics: NotRequired["capo_cost_explorer.types.metric_names.MetricNames"]
    """<p>The measurement that you want your Savings Plans coverage reported in. The only valid value is <code>SpendCoveredBySavingsPlans</code>.</p>"""
    next_token: NotRequired["capo_cost_explorer.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""
    max_results: NotRequired["capo_cost_explorer.types.max_results.MaxResults"]
    """<p>The number of items to be returned in a response. The default is <code>20</code>, with a minimum value of <code>1</code>.</p>"""
    sort_by: NotRequired["capo_cost_explorer.types.sort_definition.SortDefinition"]
    """<p>The value that you want to sort the data by.</p> <p>The following values are supported for <code>Key</code>:</p> <ul> <li> <p> <code>SpendCoveredBySavingsPlan</code> </p> </li> <li> <p> <code>OnDemandCost</code> </p> </li> <li> <p> <code>CoveragePercentage</code> </p> </li> <li> <p> <code>TotalCost</code> </p> </li> <li> <p> <code>InstanceFamily</code> </p> </li> <li> <p> <code>Region</code> </p> </li> <li> <p> <code>Service</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSavingsPlansCoverageRequest) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.date_interval

    out["TimePeriod"] = capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
        value["time_period"]
    )
    if "group_by" in value:
        import capo_cost_explorer.types.group_definitions

        out["GroupBy"] = (
            capo_cost_explorer.types.group_definitions.serialize_aws_json_1_1(
                value["group_by"]
            )
        )
    if "granularity" in value:
        import capo_cost_explorer.types.granularity

        out["Granularity"] = (
            capo_cost_explorer.types.granularity.serialize_aws_json_1_1(
                value["granularity"]
            )
        )
    if "filter" in value:
        import capo_cost_explorer.types.expression

        out["Filter"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    if "metrics" in value:
        import capo_cost_explorer.types.metric_names

        out["Metrics"] = capo_cost_explorer.types.metric_names.serialize_aws_json_1_1(
            value["metrics"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "sort_by" in value:
        import capo_cost_explorer.types.sort_definition

        out["SortBy"] = capo_cost_explorer.types.sort_definition.serialize_aws_json_1_1(
            value["sort_by"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSavingsPlansCoverageRequest:
    out: GetSavingsPlansCoverageRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_cost_explorer.types.date_interval

        out["time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansCoverageRequest.time_period required"
        )
    if data.get("GroupBy") is not None:
        import capo_cost_explorer.types.group_definitions

        out["group_by"] = (
            capo_cost_explorer.types.group_definitions.deserialize_aws_json_1_1(
                data["GroupBy"]
            )
        )
    if data.get("Granularity") is not None:
        import capo_cost_explorer.types.granularity

        out["granularity"] = (
            capo_cost_explorer.types.granularity.deserialize_aws_json_1_1(
                data["Granularity"]
            )
        )
    if data.get("Filter") is not None:
        import capo_cost_explorer.types.expression

        out["filter"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("Metrics") is not None:
        import capo_cost_explorer.types.metric_names

        out["metrics"] = capo_cost_explorer.types.metric_names.deserialize_aws_json_1_1(
            data["Metrics"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("SortBy") is not None:
        import capo_cost_explorer.types.sort_definition

        out["sort_by"] = (
            capo_cost_explorer.types.sort_definition.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    return out
