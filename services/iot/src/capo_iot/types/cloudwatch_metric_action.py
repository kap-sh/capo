"""Generated from Smithy shape ``com.amazonaws.iot#CloudwatchMetricAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.string


class CloudwatchMetricAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The IAM role that allows access to the CloudWatch metric.</p>"""
    metric_namespace: "capo_iot.types.string.String"
    """<p>The CloudWatch metric namespace name.</p>"""
    metric_name: "capo_iot.types.string.String"
    """<p>The CloudWatch metric name.</p>"""
    metric_value: "capo_iot.types.string.String"
    """<p>The CloudWatch metric value.</p>"""
    metric_unit: "capo_iot.types.string.String"
    """<p>The <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit">metric unit</a> supported by CloudWatch.</p>"""
    metric_timestamp: NotRequired["capo_iot.types.string.String"]
    """<p>An optional <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp">Unix timestamp</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudwatchMetricAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["metricNamespace"] = value["metric_namespace"]
    out["metricName"] = value["metric_name"]
    out["metricValue"] = value["metric_value"]
    out["metricUnit"] = value["metric_unit"]
    if "metric_timestamp" in value:
        out["metricTimestamp"] = value["metric_timestamp"]
    return out


def deserialize_json(data: dict) -> CloudwatchMetricAction:
    out: CloudwatchMetricAction = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CloudwatchMetricAction.role_arn required")
    if data.get("metricNamespace") is not None:
        out["metric_namespace"] = data["metricNamespace"]
    else:
        raise DeserializationError("CloudwatchMetricAction.metric_namespace required")
    if data.get("metricName") is not None:
        out["metric_name"] = data["metricName"]
    else:
        raise DeserializationError("CloudwatchMetricAction.metric_name required")
    if data.get("metricValue") is not None:
        out["metric_value"] = data["metricValue"]
    else:
        raise DeserializationError("CloudwatchMetricAction.metric_value required")
    if data.get("metricUnit") is not None:
        out["metric_unit"] = data["metricUnit"]
    else:
        raise DeserializationError("CloudwatchMetricAction.metric_unit required")
    if data.get("metricTimestamp") is not None:
        out["metric_timestamp"] = data["metricTimestamp"]
    return out
