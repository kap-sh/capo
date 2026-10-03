"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetReservationUtilizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.granularity
    import capo_cost_explorer.types.group_definitions
    import capo_cost_explorer.types.max_results
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.sort_definition


class GetReservationUtilizationRequest(TypedDict, closed=True):
    time_period: "capo_cost_explorer.types.date_interval.DateInterval"
    """<p>Sets the start and end dates for retrieving Reserved Instance (RI) utilization. The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>. </p>"""
    group_by: NotRequired["capo_cost_explorer.types.group_definitions.GroupDefinitions"]
    """<p>Groups only by <code>SUBSCRIPTION_ID</code>. Metadata is included.</p>"""
    granularity: NotRequired["capo_cost_explorer.types.granularity.Granularity"]
    """<p>If <code>GroupBy</code> is set, <code>Granularity</code> can't be set. If <code>Granularity</code> isn't set, the response object doesn't include <code>Granularity</code>, either <code>MONTHLY</code> or <code>DAILY</code>. If both <code>GroupBy</code> and <code>Granularity</code> aren't set, <code>GetReservationUtilization</code> defaults to <code>DAILY</code>.</p> <p>The <code>GetReservationUtilization</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>"""
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    """<p>Filters utilization data by dimensions. You can filter by the following dimensions:</p> <ul> <li> <p>AZ</p> </li> <li> <p>CACHE_ENGINE</p> </li> <li> <p>DEPLOYMENT_OPTION</p> </li> <li> <p>INSTANCE_TYPE</p> </li> <li> <p>LINKED_ACCOUNT</p> </li> <li> <p>OPERATING_SYSTEM</p> </li> <li> <p>PLATFORM</p> </li> <li> <p>REGION</p> </li> <li> <p>SERVICE</p> <note> <p>If not specified, the <code>SERVICE</code> filter defaults to Amazon Elastic Compute Cloud - Compute. Supported values for <code>SERVICE</code> are Amazon Elastic Compute Cloud - Compute, Amazon Relational Database Service, Amazon ElastiCache, Amazon Redshift, and Amazon Elasticsearch Service. The value for the <code>SERVICE</code> filter should not exceed "1".</p> </note> </li> <li> <p>SCOPE</p> </li> <li> <p>TENANCY</p> </li> </ul> <p> <code>GetReservationUtilization</code> uses the same <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object as the other operations, but only <code>AND</code> is supported among each dimension, and nesting is supported up to only one level deep. If there are multiple values for a dimension, they are OR'd together.</p>"""
    sort_by: NotRequired["capo_cost_explorer.types.sort_definition.SortDefinition"]
    """<p>The value that you want to sort the data by.</p> <p>The following values are supported for <code>Key</code>:</p> <ul> <li> <p> <code>UtilizationPercentage</code> </p> </li> <li> <p> <code>UtilizationPercentageInUnits</code> </p> </li> <li> <p> <code>PurchasedHours</code> </p> </li> <li> <p> <code>PurchasedUnits</code> </p> </li> <li> <p> <code>TotalActualHours</code> </p> </li> <li> <p> <code>TotalActualUnits</code> </p> </li> <li> <p> <code>UnusedHours</code> </p> </li> <li> <p> <code>UnusedUnits</code> </p> </li> <li> <p> <code>OnDemandCostOfRIHoursUsed</code> </p> </li> <li> <p> <code>NetRISavings</code> </p> </li> <li> <p> <code>TotalPotentialRISavings</code> </p> </li> <li> <p> <code>AmortizedUpfrontFee</code> </p> </li> <li> <p> <code>AmortizedRecurringFee</code> </p> </li> <li> <p> <code>TotalAmortizedFee</code> </p> </li> <li> <p> <code>RICostForUnusedHours</code> </p> </li> <li> <p> <code>RealizedSavings</code> </p> </li> <li> <p> <code>UnrealizedSavings</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""
    max_results: NotRequired["capo_cost_explorer.types.max_results.MaxResults"]
    """<p>The maximum number of objects that you returned for this request. If more objects are available, in the response, Amazon Web Services provides a NextPageToken value that you can use in a subsequent call to get the next batch of objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationUtilizationRequest) -> dict:
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
    if "sort_by" in value:
        import capo_cost_explorer.types.sort_definition

        out["SortBy"] = capo_cost_explorer.types.sort_definition.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationUtilizationRequest:
    out: GetReservationUtilizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_cost_explorer.types.date_interval

        out["time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetReservationUtilizationRequest.time_period required"
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
    if data.get("SortBy") is not None:
        import capo_cost_explorer.types.sort_definition

        out["sort_by"] = (
            capo_cost_explorer.types.sort_definition.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
