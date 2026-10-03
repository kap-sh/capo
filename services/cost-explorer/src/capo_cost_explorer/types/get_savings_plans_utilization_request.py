"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlansUtilizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.granularity
    import capo_cost_explorer.types.sort_definition


class GetSavingsPlansUtilizationRequest(TypedDict, closed=True):
    time_period: "capo_cost_explorer.types.date_interval.DateInterval"
    """<p>The time period that you want the usage and costs for. The <code>Start</code> date must be within 13 months. The <code>End</code> date must be after the <code>Start</code> date, and before the current date. Future dates can't be used as an <code>End</code> date.</p>"""
    granularity: NotRequired["capo_cost_explorer.types.granularity.Granularity"]
    """<p>The granularity of the Amazon Web Services utillization data for your Savings Plans.</p> <p>The <code>GetSavingsPlansUtilization</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>"""
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    """<p>Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can filter data with the following dimensions:</p> <ul> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>SAVINGS_PLAN_ARN</code> </p> </li> <li> <p> <code>SAVINGS_PLANS_TYPE</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>PAYMENT_OPTION</code> </p> </li> <li> <p> <code>INSTANCE_TYPE_FAMILY</code> </p> </li> </ul> <p> <code>GetSavingsPlansUtilization</code> uses the same <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object as the other operations, but only <code>AND</code> is supported among each dimension.</p>"""
    sort_by: NotRequired["capo_cost_explorer.types.sort_definition.SortDefinition"]
    """<p>The value that you want to sort the data by.</p> <p>The following values are supported for <code>Key</code>:</p> <ul> <li> <p> <code>UtilizationPercentage</code> </p> </li> <li> <p> <code>TotalCommitment</code> </p> </li> <li> <p> <code>UsedCommitment</code> </p> </li> <li> <p> <code>UnusedCommitment</code> </p> </li> <li> <p> <code>NetSavings</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSavingsPlansUtilizationRequest) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.date_interval

    out["TimePeriod"] = capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
        value["time_period"]
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
    if "sort_by" in value:
        import capo_cost_explorer.types.sort_definition

        out["SortBy"] = capo_cost_explorer.types.sort_definition.serialize_aws_json_1_1(
            value["sort_by"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSavingsPlansUtilizationRequest:
    out: GetSavingsPlansUtilizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_cost_explorer.types.date_interval

        out["time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansUtilizationRequest.time_period required"
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
    if data.get("SortBy") is not None:
        import capo_cost_explorer.types.sort_definition

        out["sort_by"] = (
            capo_cost_explorer.types.sort_definition.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    return out
