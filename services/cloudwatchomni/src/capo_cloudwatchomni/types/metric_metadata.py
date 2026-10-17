"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#MetricMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.metadata_attribute_map
    import capo_cloudwatchomni.types.metric_semantics


class MetricMetadata(TypedDict, closed=True):
    name: NotRequired["str"]
    """The metric name as emitted, such as "Duration"."""
    namespace: NotRequired["str"]
    """DEPRECATED: read attributes["service.namespace"] instead. Retained (deprecated) for backward compatibility with existing consumers; will be removed once they migrate. The logical service grouping the metric belongs to."""
    preferred_stat: NotRequired["str"]
    """The statistic to chart or alarm on, such as "p99" or "Sum". Free-form and frequently absent."""
    metric_type: NotRequired["str"]
    """OTel metric kind: "gauge", "sum", "histogram", "exponential_histogram", or "summary" (CloudWatch-vended metrics carry the same kinds). Absent when the producer did not report one."""
    attributes: NotRequired[
        "capo_cloudwatchomni.types.metadata_attribute_map.MetadataAttributeMap"
    ]
    """Per-metric qualifying attributes the console uses to query this metric's telemetry. These are the RAW, store-matching values keyed by their OTel names ("service.name", "service.namespace", "cloud.provider", "cloud.account.id", "cloud.region", "instrumentation_scope") — deliberately NOT the node's normalized/merged identity, so the query selectors match the emitted series. A merged node can carry different values per metric, which is why they live here rather than on the node."""
    semantics: NotRequired["capo_cloudwatchomni.types.metric_semantics.MetricSemantics"]
    """What the metric means and the unit it is reported in."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
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
    return out


def deserialize_cbor(data: dict) -> MetricMetadata:
    out: MetricMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
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
    return out
