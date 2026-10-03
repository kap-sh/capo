"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricsDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.cloud_watch_metrics_data_summary
    import capo_devops_guru.types.cloud_watch_metrics_dimensions
    import capo_devops_guru.types.cloud_watch_metrics_metric_name
    import capo_devops_guru.types.cloud_watch_metrics_namespace
    import capo_devops_guru.types.cloud_watch_metrics_period
    import capo_devops_guru.types.cloud_watch_metrics_stat
    import capo_devops_guru.types.cloud_watch_metrics_unit


class CloudWatchMetricsDetail(TypedDict, closed=True):
    metric_name: NotRequired[
        "capo_devops_guru.types.cloud_watch_metrics_metric_name.CloudWatchMetricsMetricName"
    ]
    """<p> The name of the CloudWatch metric. </p>"""
    namespace: NotRequired[
        "capo_devops_guru.types.cloud_watch_metrics_namespace.CloudWatchMetricsNamespace"
    ]
    """<p> The namespace of the CloudWatch metric. A namespace is a container for CloudWatch metrics. </p>"""
    dimensions: NotRequired[
        "capo_devops_guru.types.cloud_watch_metrics_dimensions.CloudWatchMetricsDimensions"
    ]
    """<p> An array of CloudWatch dimensions associated with </p>"""
    stat: NotRequired[
        "capo_devops_guru.types.cloud_watch_metrics_stat.CloudWatchMetricsStat"
    ]
    """<p> The type of statistic associated with the CloudWatch metric. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic">Statistics</a> in the <i>Amazon CloudWatch User Guide</i>. </p>"""
    unit: NotRequired[
        "capo_devops_guru.types.cloud_watch_metrics_unit.CloudWatchMetricsUnit"
    ]
    """<p> The unit of measure used for the CloudWatch metric. For example, <code>Bytes</code>, <code>Seconds</code>, <code>Count</code>, and <code>Percent</code>. </p>"""
    period: "capo_devops_guru.types.cloud_watch_metrics_period.CloudWatchMetricsPeriod"
    """<p> The length of time associated with the CloudWatch metric in number of seconds. </p>"""
    metric_data_summary: NotRequired[
        "capo_devops_guru.types.cloud_watch_metrics_data_summary.CloudWatchMetricsDataSummary"
    ]
    """<p>This object returns anomaly metric data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMetricsDetail) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "dimensions" in value:
        import capo_devops_guru.types.cloud_watch_metrics_dimensions

        out["Dimensions"] = (
            capo_devops_guru.types.cloud_watch_metrics_dimensions.serialize_json(
                value["dimensions"]
            )
        )
    if "stat" in value:
        import capo_devops_guru.types.cloud_watch_metrics_stat

        out["Stat"] = capo_devops_guru.types.cloud_watch_metrics_stat.serialize_json(
            value["stat"]
        )
    if "unit" in value:
        out["Unit"] = value["unit"]
    out["Period"] = value.get("period", 0)
    if "metric_data_summary" in value:
        import capo_devops_guru.types.cloud_watch_metrics_data_summary

        out["MetricDataSummary"] = (
            capo_devops_guru.types.cloud_watch_metrics_data_summary.serialize_json(
                value["metric_data_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchMetricsDetail:
    out: CloudWatchMetricsDetail = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("Dimensions") is not None:
        import capo_devops_guru.types.cloud_watch_metrics_dimensions

        out["dimensions"] = (
            capo_devops_guru.types.cloud_watch_metrics_dimensions.deserialize_json(
                data["Dimensions"]
            )
        )
    if data.get("Stat") is not None:
        import capo_devops_guru.types.cloud_watch_metrics_stat

        out["stat"] = capo_devops_guru.types.cloud_watch_metrics_stat.deserialize_json(
            data["Stat"]
        )
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    else:
        out["period"] = 0
    if data.get("MetricDataSummary") is not None:
        import capo_devops_guru.types.cloud_watch_metrics_data_summary

        out["metric_data_summary"] = (
            capo_devops_guru.types.cloud_watch_metrics_data_summary.deserialize_json(
                data["MetricDataSummary"]
            )
        )
    return out
