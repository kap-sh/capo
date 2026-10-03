"""Generated from Smithy shape ``com.amazonaws.internetmonitor#StartQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_internetmonitor.types.account_id
    import capo_internetmonitor.types.filter_parameters
    import capo_internetmonitor.types.query_type
    import capo_internetmonitor.types.resource_name


class StartQueryInput(TypedDict, closed=True):
    monitor_name: "capo_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor to query.</p>"""
    start_time: "datetime.datetime"
    """<p>The timestamp that is the beginning of the period that you want to retrieve data for with your query.</p>"""
    end_time: "datetime.datetime"
    """<p>The timestamp that is the end of the period that you want to retrieve data for with your query.</p>"""
    query_type: "capo_internetmonitor.types.query_type.QueryType"
    """<p>The type of query to run. The following are the three types of queries that you can run using the Internet Monitor query interface:</p> <ul> <li> <p> <code>MEASUREMENTS</code>: Provides availability score, performance score, total traffic, and round-trip times, at 5 minute intervals.</p> </li> <li> <p> <code>TOP_LOCATIONS</code>: Provides availability score, performance score, total traffic, and time to first byte (TTFB) information, for the top location and ASN combinations that you're monitoring, by traffic volume.</p> </li> <li> <p> <code>TOP_LOCATION_DETAILS</code>: Provides TTFB for Amazon CloudFront, your current configuration, and the best performing EC2 configuration, at 1 hour intervals.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS</code>: Provides TTFB, using a 30-day weighted average, for all traffic in each Amazon Web Services location that is monitored.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS_DETAILS</code>: Provides TTFB, using a 30-day weighted average, for each top location, for a proposed Amazon Web Services location. Must provide an Amazon Web Services location to search.</p> </li> <li> <p> <code>ROUTING_SUGGESTIONS</code>: Provides the predicted average round-trip time (RTT) from an IP prefix toward an Amazon Web Services location for a DNS resolver. The RTT is calculated at one hour intervals, over a one hour period.</p> </li> </ul> <p>For lists of the fields returned with each query type and more information about how each type of query is performed, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html"> Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""
    filter_parameters: NotRequired[
        "capo_internetmonitor.types.filter_parameters.FilterParameters"
    ]
    """<p>The <code>FilterParameters</code> field that you use with Amazon CloudWatch Internet Monitor queries is a string the defines how you want a query to be filtered. The filter parameters that you can specify depend on the query type, since each query type returns a different set of Internet Monitor data.</p> <p>For more information about specifying filter parameters, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""
    linked_account_id: NotRequired["capo_internetmonitor.types.account_id.AccountId"]
    """<p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryInput) -> dict:
    out: dict = {}
    import capo_internetmonitor._protocol.serialize

    out["StartTime"] = capo_internetmonitor._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    import capo_internetmonitor._protocol.serialize

    out["EndTime"] = capo_internetmonitor._protocol.serialize.fmt_date_time(
        value["end_time"]
    )
    out["QueryType"] = value["query_type"]
    if "filter_parameters" in value:
        import capo_internetmonitor.types.filter_parameters

        out["FilterParameters"] = (
            capo_internetmonitor.types.filter_parameters.serialize_json(
                value["filter_parameters"]
            )
        )
    if "linked_account_id" in value:
        out["LinkedAccountId"] = value["linked_account_id"]
    return out


def deserialize_json(data: dict) -> StartQueryInput:
    out: StartQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["StartTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("StartQueryInput.start_time required")
    if data.get("EndTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["EndTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("StartQueryInput.end_time required")
    if data.get("QueryType") is not None:
        out["query_type"] = data["QueryType"]
    else:
        raise DeserializationError("StartQueryInput.query_type required")
    if data.get("FilterParameters") is not None:
        import capo_internetmonitor.types.filter_parameters

        out["filter_parameters"] = (
            capo_internetmonitor.types.filter_parameters.deserialize_json(
                data["FilterParameters"]
            )
        )
    if data.get("LinkedAccountId") is not None:
        out["linked_account_id"] = data["LinkedAccountId"]
    return out
