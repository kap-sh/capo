"""Generated from Smithy shape ``com.amazonaws.rds#PerformanceInsightsMetricQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.performance_insights_metric_dimension_group
    import capo_rds.types.string


class PerformanceInsightsMetricQuery(TypedDict, closed=True):
    group_by: NotRequired[
        "capo_rds.types.performance_insights_metric_dimension_group.PerformanceInsightsMetricDimensionGroup"
    ]
    """<p>A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.</p>"""
    metric: NotRequired["capo_rds.types.string.String"]
    """<p>The name of a Performance Insights metric to be measured.</p> <p>Valid Values:</p> <ul> <li> <p> <code>db.load.avg</code> - A scaled representation of the number of active sessions for the database engine.</p> </li> <li> <p> <code>db.sampledload.avg</code> - The raw number of active sessions for the database engine.</p> </li> <li> <p>The counter metrics listed in <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS">Performance Insights operating system counters</a> in the <i>Amazon Aurora User Guide</i>.</p> </li> </ul> <p>If the number of active sessions is less than an internal Performance Insights threshold, <code>db.load.avg</code> and <code>db.sampledload.avg</code> are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with <code>db.load.avg</code> showing the scaled values, <code>db.sampledload.avg</code> showing the raw values, and <code>db.sampledload.avg</code> less than <code>db.load.avg</code>. For most use cases, you can query <code>db.load.avg</code> only.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PerformanceInsightsMetricQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_by" in value:
        import capo_rds.types.performance_insights_metric_dimension_group

        capo_rds.types.performance_insights_metric_dimension_group.serialize_query(
            value["group_by"], pairs, f"{key_prefix}GroupBy"
        )
    if "metric" in value:
        pairs.append((f"{key_prefix}Metric", str(value["metric"])))


def deserialize_query(el: Element) -> PerformanceInsightsMetricQuery:
    out: PerformanceInsightsMetricQuery = {}  # type: ignore[typeddict-item]
    child_group_by = el.find("GroupBy")
    if child_group_by is not None:
        import capo_rds.types.performance_insights_metric_dimension_group

        out["group_by"] = (
            capo_rds.types.performance_insights_metric_dimension_group.deserialize_query(
                child_group_by
            )
        )
    child_metric = el.find("Metric")
    if child_metric is not None:
        out["metric"] = str(child_metric.text or "")
    return out
