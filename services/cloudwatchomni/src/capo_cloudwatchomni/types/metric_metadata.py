"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#MetricMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.metadata_attribute_map
    import capo_cloudwatchomni.types.metric_aggregation_temporality
    import capo_cloudwatchomni.types.metric_monotonicity
    import capo_cloudwatchomni.types.metric_semantics


class MetricMetadata(TypedDict, closed=True):
    name: NotRequired["str"]
    """The metric name as emitted, such as "Duration"."""
    preferred_stat: NotRequired["str"]
    """The statistic to chart or alarm on, such as "p99" or "Sum". Free-form and frequently absent."""
    metric_type: NotRequired["str"]
    """OTel metric kind: "gauge", "sum", "histogram", "exponential_histogram", or "summary" (CloudWatch-vended metrics carry the same kinds). Absent when the producer did not report one."""
    attributes: NotRequired[
        "capo_cloudwatchomni.types.metadata_attribute_map.MetadataAttributeMap"
    ]
    """Per-metric qualifying attributes used to query this metric's telemetry. Keys are the metric store's own label names, not bare OTel attribute names: service identity arrives as "@resource.service.name" and "@resource.service.namespace", and the instrumentation scope as "@instrumentation.@name". Span-derived metrics can additionally carry the service as a bare data point "service.name" label. Cloud provider, account and region are not repeated per metric — read those from the node. Values are RAW, deliberately NOT the node's merged identity, so a selector built from them matches the emitted series. A merged node can carry different values per metric, which is why these live here rather than on the node."""
    semantics: NotRequired["capo_cloudwatchomni.types.metric_semantics.MetricSemantics"]
    """What the metric means and the unit it is reported in."""
    aggregation_temporality: NotRequired[
        "capo_cloudwatchomni.types.metric_aggregation_temporality.MetricAggregationTemporality"
    ]
    """Aggregation temporality for the selected metric stream represented by this metadata entry. Present when known, including cumulative for OTel Summary metrics. Absent for Gauge metrics or when the information is unavailable."""
    monotonicity: NotRequired[
        "capo_cloudwatchomni.types.metric_monotonicity.MetricMonotonicity"
    ]
    """Whether the selected Sum metric stream represented by this metadata entry is a non-negative accumulation. Absent for metrics other than Sum or when the information is unavailable."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "preferred_stat" in value:
        out["preferredStat"] = value["preferred_stat"]
    if "metric_type" in value:
        out["metricType"] = value["metric_type"]
    if "attributes" in value:
        import capo_cloudwatchomni.types.metadata_attribute_map

        out["attributes"] = (
            capo_cloudwatchomni.types.metadata_attribute_map.serialize_cbor(
                value["attributes"]
            )
        )
    if "semantics" in value:
        import capo_cloudwatchomni.types.metric_semantics

        out["semantics"] = capo_cloudwatchomni.types.metric_semantics.serialize_cbor(
            value["semantics"]
        )
    if "aggregation_temporality" in value:
        import capo_cloudwatchomni.types.metric_aggregation_temporality

        out["aggregationTemporality"] = (
            capo_cloudwatchomni.types.metric_aggregation_temporality.serialize_cbor(
                value["aggregation_temporality"]
            )
        )
    if "monotonicity" in value:
        import capo_cloudwatchomni.types.metric_monotonicity

        out["monotonicity"] = (
            capo_cloudwatchomni.types.metric_monotonicity.serialize_cbor(
                value["monotonicity"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> MetricMetadata:
    out: MetricMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("preferredStat") is not None:
        out["preferred_stat"] = data["preferredStat"]
    if data.get("metricType") is not None:
        out["metric_type"] = data["metricType"]
    if data.get("attributes") is not None:
        import capo_cloudwatchomni.types.metadata_attribute_map

        out["attributes"] = (
            capo_cloudwatchomni.types.metadata_attribute_map.deserialize_cbor(
                data["attributes"]
            )
        )
    if data.get("semantics") is not None:
        import capo_cloudwatchomni.types.metric_semantics

        out["semantics"] = capo_cloudwatchomni.types.metric_semantics.deserialize_cbor(
            data["semantics"]
        )
    if data.get("aggregationTemporality") is not None:
        import capo_cloudwatchomni.types.metric_aggregation_temporality

        out["aggregation_temporality"] = (
            capo_cloudwatchomni.types.metric_aggregation_temporality.deserialize_cbor(
                data["aggregationTemporality"]
            )
        )
    if data.get("monotonicity") is not None:
        import capo_cloudwatchomni.types.metric_monotonicity

        out["monotonicity"] = (
            capo_cloudwatchomni.types.metric_monotonicity.deserialize_cbor(
                data["monotonicity"]
            )
        )
    return out
