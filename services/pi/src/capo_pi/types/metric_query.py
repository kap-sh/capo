"""Generated from Smithy shape ``com.amazonaws.pi#MetricQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pi.types.dimension_group
    import capo_pi.types.metric_query_filter_map
    import capo_pi.types.sanitized_string


class MetricQuery(TypedDict, closed=True):
    metric: "capo_pi.types.sanitized_string.SanitizedString"
    """<p>The name of a Performance Insights metric to be measured.</p> <p>Valid values for <code>Metric</code> are:</p> <ul> <li> <p> <code>db.load.avg</code> - A scaled representation of the number of active sessions for the database engine.</p> </li> <li> <p> <code>db.sampledload.avg</code> - The raw number of active sessions for the database engine.</p> </li> <li> <p>The counter metrics listed in <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS">Performance Insights operating system counters</a> in the <i>Amazon Aurora User Guide</i>.</p> </li> <li> <p>The counter metrics listed in <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS">Performance Insights operating system counters</a> in the <i>Amazon RDS User Guide</i>.</p> </li> </ul> <p>If the number of active sessions is less than an internal Performance Insights threshold, <code>db.load.avg</code> and <code>db.sampledload.avg</code> are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with <code>db.load.avg</code> showing the scaled values, <code>db.sampledload.avg</code> showing the raw values, and <code>db.sampledload.avg</code> less than <code>db.load.avg</code>. For most use cases, you can query <code>db.load.avg</code> only.</p>"""
    group_by: NotRequired["capo_pi.types.dimension_group.DimensionGroup"]
    """<p>A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.</p>"""
    filter: NotRequired["capo_pi.types.metric_query_filter_map.MetricQueryFilterMap"]
    """<p>One or more filters to apply in the request. Restrictions:</p> <ul> <li> <p>Any number of filters by the same dimension, as specified in the <code>GroupBy</code> parameter.</p> </li> <li> <p>A single filter for any other dimension in this dimension group.</p> </li> </ul> <note> <p>The <code>db.sql.db_id</code> filter isn't available for RDS for SQL Server DB instances.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricQuery) -> dict:
    out: dict = {}
    out["Metric"] = value["metric"]
    if "group_by" in value:
        import capo_pi.types.dimension_group

        out["GroupBy"] = capo_pi.types.dimension_group.serialize_aws_json_1_1(
            value["group_by"]
        )
    if "filter" in value:
        import capo_pi.types.metric_query_filter_map

        out["Filter"] = capo_pi.types.metric_query_filter_map.serialize_aws_json_1_1(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricQuery:
    out: MetricQuery = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    else:
        raise DeserializationError("MetricQuery.metric required")
    if data.get("GroupBy") is not None:
        import capo_pi.types.dimension_group

        out["group_by"] = capo_pi.types.dimension_group.deserialize_aws_json_1_1(
            data["GroupBy"]
        )
    if data.get("Filter") is not None:
        import capo_pi.types.metric_query_filter_map

        out["filter"] = capo_pi.types.metric_query_filter_map.deserialize_aws_json_1_1(
            data["Filter"]
        )
    return out
