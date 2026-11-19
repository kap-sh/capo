"""Generated from Smithy shape ``com.amazonaws.cloudwatch#OTelEnrichmentMetricSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.namespace
    import capo_cloudwatch.types.o_tel_enrichment_metric_name_list


class OTelEnrichmentMetricSelector(TypedDict, closed=True):
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace of the metrics to select. Namespaces are matched exactly and are case-sensitive.</p>"""
    metric_names: NotRequired[
        "capo_cloudwatch.types.o_tel_enrichment_metric_name_list.OTelEnrichmentMetricNameList"
    ]
    """<p>The names of the metrics to select within the namespace. Metric names are matched exactly and are case-sensitive. If this parameter is omitted, every metric in the namespace is selected.</p> <p>A maximum of 100 metric names is allowed for each selector.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OTelEnrichmentMetricSelector) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_names" in value:
        import capo_cloudwatch.types.o_tel_enrichment_metric_name_list

        out["MetricNames"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_name_list.serialize_aws_json_1_0(
                value["metric_names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OTelEnrichmentMetricSelector:
    out: OTelEnrichmentMetricSelector = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricNames") is not None:
        import capo_cloudwatch.types.o_tel_enrichment_metric_name_list

        out["metric_names"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_name_list.deserialize_aws_json_1_0(
                data["MetricNames"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: OTelEnrichmentMetricSelector, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "metric_names" in value:
        import capo_cloudwatch.types.o_tel_enrichment_metric_name_list

        capo_cloudwatch.types.o_tel_enrichment_metric_name_list.serialize_query(
            value["metric_names"], pairs, f"{key_prefix}MetricNames"
        )


def deserialize_query(el: Element) -> OTelEnrichmentMetricSelector:
    out: OTelEnrichmentMetricSelector = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_names = el.find("MetricNames")
    if child_metric_names is not None:
        import capo_cloudwatch.types.o_tel_enrichment_metric_name_list

        out["metric_names"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_name_list.deserialize_query(
                child_metric_names
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OTelEnrichmentMetricSelector) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_names" in value:
        import capo_cloudwatch.types.o_tel_enrichment_metric_name_list

        out["MetricNames"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_name_list.serialize_cbor(
                value["metric_names"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> OTelEnrichmentMetricSelector:
    out: OTelEnrichmentMetricSelector = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricNames") is not None:
        import capo_cloudwatch.types.o_tel_enrichment_metric_name_list

        out["metric_names"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_name_list.deserialize_cbor(
                data["MetricNames"]
            )
        )
    return out
