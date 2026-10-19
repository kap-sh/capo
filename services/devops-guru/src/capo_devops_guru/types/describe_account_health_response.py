"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeAccountHealthResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.analyzed_resource_count
    import capo_devops_guru.types.num_metrics_analyzed
    import capo_devops_guru.types.num_open_proactive_insights
    import capo_devops_guru.types.num_open_reactive_insights
    import capo_devops_guru.types.resource_hours


class DescribeAccountHealthResponse(TypedDict, closed=True):
    open_reactive_insights: (
        "capo_devops_guru.types.num_open_reactive_insights.NumOpenReactiveInsights"
    )
    """<p> An integer that specifies the number of open reactive insights in your Amazon Web Services account. </p>"""
    open_proactive_insights: (
        "capo_devops_guru.types.num_open_proactive_insights.NumOpenProactiveInsights"
    )
    """<p> An integer that specifies the number of open proactive insights in your Amazon Web Services account. </p>"""
    metrics_analyzed: "capo_devops_guru.types.num_metrics_analyzed.NumMetricsAnalyzed"
    """<p> An integer that specifies the number of metrics that have been analyzed in your Amazon Web Services account. </p>"""
    resource_hours: "capo_devops_guru.types.resource_hours.ResourceHours"
    """<p>The number of Amazon DevOps Guru resource analysis hours billed to the current Amazon Web Services account in the last hour. </p>"""
    analyzed_resource_count: NotRequired[
        "capo_devops_guru.types.analyzed_resource_count.AnalyzedResourceCount"
    ]
    """<p> Number of resources that DevOps Guru is monitoring in your Amazon Web Services account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountHealthResponse) -> dict:
    out: dict = {}
    out["OpenReactiveInsights"] = value.get("open_reactive_insights", 0)
    out["OpenProactiveInsights"] = value.get("open_proactive_insights", 0)
    out["MetricsAnalyzed"] = value.get("metrics_analyzed", 0)
    out["ResourceHours"] = value["resource_hours"]
    if "analyzed_resource_count" in value:
        out["AnalyzedResourceCount"] = value["analyzed_resource_count"]
    return out


def deserialize_json(data: dict) -> DescribeAccountHealthResponse:
    out: DescribeAccountHealthResponse = {}  # type: ignore[typeddict-item]
    if data.get("OpenReactiveInsights") is not None:
        out["open_reactive_insights"] = data["OpenReactiveInsights"]
    else:
        out["open_reactive_insights"] = 0
    if data.get("OpenProactiveInsights") is not None:
        out["open_proactive_insights"] = data["OpenProactiveInsights"]
    else:
        out["open_proactive_insights"] = 0
    if data.get("MetricsAnalyzed") is not None:
        out["metrics_analyzed"] = data["MetricsAnalyzed"]
    else:
        out["metrics_analyzed"] = 0
    if data.get("ResourceHours") is not None:
        out["resource_hours"] = data["ResourceHours"]
    else:
        out["resource_hours"] = 0
    if data.get("AnalyzedResourceCount") is not None:
        out["analyzed_resource_count"] = data["AnalyzedResourceCount"]
    return out
