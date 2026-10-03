"""Generated from Smithy shape ``com.amazonaws.wafv2#VisibilityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.boolean
    import capo_wafv2.types.metric_name


class VisibilityConfig(TypedDict, closed=True):
    sampled_requests_enabled: "capo_wafv2.types.boolean.Boolean"
    """<p>Indicates whether WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the WAF console. </p> <p>If you configure data protection for the web ACL, the protection applies to the web ACL's sampled web request data. </p> <note> <p>Request sampling doesn't provide a field redaction option, and any field redaction that you specify in your logging configuration doesn't affect sampling. You can only exclude fields from request sampling by disabling sampling in the web ACL visibility configuration or by configuring data protection for the web ACL.</p> </note>"""
    cloud_watch_metrics_enabled: "capo_wafv2.types.boolean.Boolean"
    """<p>Indicates whether the associated resource sends metrics to Amazon CloudWatch. For the list of available metrics, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#waf-metrics">WAF Metrics</a> in the <i>WAF Developer Guide</i>.</p> <p>For web ACLs, the metrics are for web requests that have the web ACL default action applied. WAF applies the default action to web requests that pass the inspection of all rules in the web ACL without being either allowed or blocked. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-default-action.html">The web ACL default action</a> in the <i>WAF Developer Guide</i>.</p>"""
    metric_name: "capo_wafv2.types.metric_name.MetricName"
    """<p>A name of the Amazon CloudWatch metric dimension. The name can contain only the characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore). The name can be from one to 128 characters long. It can't contain whitespace or metric names that are reserved for WAF, for example <code>All</code> and <code>Default_Action</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VisibilityConfig) -> dict:
    out: dict = {}
    out["SampledRequestsEnabled"] = value.get("sampled_requests_enabled", False)
    out["CloudWatchMetricsEnabled"] = value.get("cloud_watch_metrics_enabled", False)
    out["MetricName"] = value["metric_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VisibilityConfig:
    out: VisibilityConfig = {}  # type: ignore[typeddict-item]
    if data.get("SampledRequestsEnabled") is not None:
        out["sampled_requests_enabled"] = data["SampledRequestsEnabled"]
    else:
        out["sampled_requests_enabled"] = False
    if data.get("CloudWatchMetricsEnabled") is not None:
        out["cloud_watch_metrics_enabled"] = data["CloudWatchMetricsEnabled"]
    else:
        out["cloud_watch_metrics_enabled"] = False
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    else:
        raise DeserializationError("VisibilityConfig.metric_name required")
    return out
