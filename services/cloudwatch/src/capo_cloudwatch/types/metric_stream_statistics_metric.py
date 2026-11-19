"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamStatisticsMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.namespace


class MetricStreamStatisticsMetric(TypedDict, closed=True):
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace of the metric.</p>"""
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStreamStatisticsMetric) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricStreamStatisticsMetric:
    out: MetricStreamStatisticsMetric = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStreamStatisticsMetric, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))


def deserialize_query(el: Element) -> MetricStreamStatisticsMetric:
    out: MetricStreamStatisticsMetric = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricStreamStatisticsMetric) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    return out


def deserialize_cbor(data: dict) -> MetricStreamStatisticsMetric:
    out: MetricStreamStatisticsMetric = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    return out
