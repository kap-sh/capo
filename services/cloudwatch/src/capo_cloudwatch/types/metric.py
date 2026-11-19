"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Metric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.namespace


class Metric(TypedDict, closed=True):
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace of the metric.</p>"""
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>The name of the metric. This is a required field.</p>"""
    dimensions: NotRequired["capo_cloudwatch.types.dimensions.Dimensions"]
    """<p>The dimensions for the metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Metric) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_aws_json_1_0(
            data["Dimensions"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(value: Metric, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        capo_cloudwatch.types.dimensions.serialize_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )


def deserialize_query(el: Element) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_query(
            child_dimensions
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Metric) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_cbor(
            value["dimensions"]
        )
    return out


def deserialize_cbor(data: dict) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_cbor(
            data["Dimensions"]
        )
    return out
