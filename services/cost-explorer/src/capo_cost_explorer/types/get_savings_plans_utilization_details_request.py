"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlansUtilizationDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.max_results
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.savings_plans_data_types
    import capo_cost_explorer.types.sort_definition


class GetSavingsPlansUtilizationDetailsRequest(TypedDict, closed=True):
    time_period: "capo_cost_explorer.types.date_interval.DateInterval"
    """<p>The time period that you want the usage and costs for. The <code>Start</code> date must be within 13 months. The <code>End</code> date must be after the <code>Start</code> date, and before the current date. Future dates can't be used as an <code>End</code> date.</p>"""
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    """<p>Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can filter data with the following dimensions:</p> <ul> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>SAVINGS_PLAN_ARN</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>PAYMENT_OPTION</code> </p> </li> <li> <p> <code>INSTANCE_TYPE_FAMILY</code> </p> </li> </ul> <p> <code>GetSavingsPlansUtilizationDetails</code> uses the same <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object as the other operations, but only <code>AND</code> is supported among each dimension.</p>"""
    data_type: NotRequired[
        "capo_cost_explorer.types.savings_plans_data_types.SavingsPlansDataTypes"
    ]
    """<p>The data type.</p>"""
    next_token: NotRequired["capo_cost_explorer.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""
    max_results: NotRequired["capo_cost_explorer.types.max_results.MaxResults"]
    """<p>The number of items to be returned in a response. The default is <code>20</code>, with a minimum value of <code>1</code>.</p>"""
    sort_by: NotRequired["capo_cost_explorer.types.sort_definition.SortDefinition"]
    """<p>The value that you want to sort the data by.</p> <p>The following values are supported for <code>Key</code>:</p> <ul> <li> <p> <code>UtilizationPercentage</code> </p> </li> <li> <p> <code>TotalCommitment</code> </p> </li> <li> <p> <code>UsedCommitment</code> </p> </li> <li> <p> <code>UnusedCommitment</code> </p> </li> <li> <p> <code>NetSavings</code> </p> </li> <li> <p> <code>AmortizedRecurringCommitment</code> </p> </li> <li> <p> <code>AmortizedUpfrontCommitment</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSavingsPlansUtilizationDetailsRequest) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.date_interval

    out["TimePeriod"] = capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
        value["time_period"]
    )
    if "filter" in value:
        import capo_cost_explorer.types.expression

        out["Filter"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    if "data_type" in value:
        import capo_cost_explorer.types.savings_plans_data_types

        out["DataType"] = (
            capo_cost_explorer.types.savings_plans_data_types.serialize_aws_json_1_1(
                value["data_type"]
            )
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


def deserialize_aws_json_1_1(data: dict) -> GetSavingsPlansUtilizationDetailsRequest:
    out: GetSavingsPlansUtilizationDetailsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_cost_explorer.types.date_interval

        out["time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansUtilizationDetailsRequest.time_period required"
        )
    if data.get("Filter") is not None:
        import capo_cost_explorer.types.expression

        out["filter"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("DataType") is not None:
        import capo_cost_explorer.types.savings_plans_data_types

        out["data_type"] = (
            capo_cost_explorer.types.savings_plans_data_types.deserialize_aws_json_1_1(
                data["DataType"]
            )
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
