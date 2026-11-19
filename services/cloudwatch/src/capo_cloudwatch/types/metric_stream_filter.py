"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_stream_filter_metric_names
    import capo_cloudwatch.types.namespace


class MetricStreamFilter(TypedDict, closed=True):
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The name of the metric namespace for this filter.</p> <p>The namespace can contain only ASCII printable characters (ASCII range 32 through 126). It must contain at least one non-whitespace character.</p>"""
    metric_names: NotRequired[
        "capo_cloudwatch.types.metric_stream_filter_metric_names.MetricStreamFilterMetricNames"
    ]
    """<p>The names of the metrics to either include or exclude from the metric stream. </p> <p>If you omit this parameter, all metrics in the namespace are included or excluded, depending on whether this filter is specified as an exclude filter or an include filter.</p> <p>Each metric name can contain only ASCII printable characters (ASCII range 32 through 126). Each metric name must contain at least one non-whitespace character.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStreamFilter) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_names" in value:
        import capo_cloudwatch.types.metric_stream_filter_metric_names

        out["MetricNames"] = (
            capo_cloudwatch.types.metric_stream_filter_metric_names.serialize_aws_json_1_0(
                value["metric_names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricStreamFilter:
    out: MetricStreamFilter = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricNames") is not None:
        import capo_cloudwatch.types.metric_stream_filter_metric_names

        out["metric_names"] = (
            capo_cloudwatch.types.metric_stream_filter_metric_names.deserialize_aws_json_1_0(
                data["MetricNames"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStreamFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "metric_names" in value:
        import capo_cloudwatch.types.metric_stream_filter_metric_names

        capo_cloudwatch.types.metric_stream_filter_metric_names.serialize_query(
            value["metric_names"], pairs, f"{key_prefix}MetricNames"
        )


def deserialize_query(el: Element) -> MetricStreamFilter:
    out: MetricStreamFilter = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_names = el.find("MetricNames")
    if child_metric_names is not None:
        import capo_cloudwatch.types.metric_stream_filter_metric_names

        out["metric_names"] = (
            capo_cloudwatch.types.metric_stream_filter_metric_names.deserialize_query(
                child_metric_names
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricStreamFilter) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_names" in value:
        import capo_cloudwatch.types.metric_stream_filter_metric_names

        out["MetricNames"] = (
            capo_cloudwatch.types.metric_stream_filter_metric_names.serialize_cbor(
                value["metric_names"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> MetricStreamFilter:
    out: MetricStreamFilter = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricNames") is not None:
        import capo_cloudwatch.types.metric_stream_filter_metric_names

        out["metric_names"] = (
            capo_cloudwatch.types.metric_stream_filter_metric_names.deserialize_cbor(
                data["MetricNames"]
            )
        )
    return out
