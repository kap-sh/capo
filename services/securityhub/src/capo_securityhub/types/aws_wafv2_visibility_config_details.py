"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2VisibilityConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsWafv2VisibilityConfigDetails(TypedDict, closed=True):
    cloud_watch_metrics_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> A boolean indicating whether the associated resource sends metrics to Amazon CloudWatch. For the list of available metrics, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#waf-metrics">WAF metrics and dimensions</a> in the <i>WAF Developer Guide</i>. </p>"""
    metric_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> A name of the Amazon CloudWatch metric. </p>"""
    sampled_requests_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> A boolean indicating whether WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the WAF console. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2VisibilityConfigDetails) -> dict:
    out: dict = {}
    if "cloud_watch_metrics_enabled" in value:
        out["CloudWatchMetricsEnabled"] = value["cloud_watch_metrics_enabled"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "sampled_requests_enabled" in value:
        out["SampledRequestsEnabled"] = value["sampled_requests_enabled"]
    return out


def deserialize_json(data: dict) -> AwsWafv2VisibilityConfigDetails:
    out: AwsWafv2VisibilityConfigDetails = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchMetricsEnabled") is not None:
        out["cloud_watch_metrics_enabled"] = data["CloudWatchMetricsEnabled"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("SampledRequestsEnabled") is not None:
        out["sampled_requests_enabled"] = data["SampledRequestsEnabled"]
    return out
