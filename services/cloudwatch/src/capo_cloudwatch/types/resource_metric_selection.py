"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ResourceMetricSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_name_list


class ResourceMetricSelection(TypedDict, closed=True):
    include_metrics: NotRequired[
        "capo_cloudwatch.types.metric_name_list.MetricNameList"
    ]
    """<p>The names of the metrics to collect for the resource. Amazon CloudWatch collects only the metrics that you list here.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceMetricSelection) -> dict:
    out: dict = {}
    if "include_metrics" in value:
        import capo_cloudwatch.types.metric_name_list

        out["IncludeMetrics"] = (
            capo_cloudwatch.types.metric_name_list.serialize_aws_json_1_0(
                value["include_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceMetricSelection:
    out: ResourceMetricSelection = {}  # type: ignore[typeddict-item]
    if data.get("IncludeMetrics") is not None:
        import capo_cloudwatch.types.metric_name_list

        out["include_metrics"] = (
            capo_cloudwatch.types.metric_name_list.deserialize_aws_json_1_0(
                data["IncludeMetrics"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceMetricSelection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "include_metrics" in value:
        import capo_cloudwatch.types.metric_name_list

        capo_cloudwatch.types.metric_name_list.serialize_query(
            value["include_metrics"], pairs, f"{key_prefix}IncludeMetrics"
        )


def deserialize_query(el: Element) -> ResourceMetricSelection:
    out: ResourceMetricSelection = {}  # type: ignore[typeddict-item]
    child_include_metrics = el.find("IncludeMetrics")
    if child_include_metrics is not None:
        import capo_cloudwatch.types.metric_name_list

        out["include_metrics"] = (
            capo_cloudwatch.types.metric_name_list.deserialize_query(
                child_include_metrics
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceMetricSelection) -> dict:
    out: dict = {}
    if "include_metrics" in value:
        import capo_cloudwatch.types.metric_name_list

        out["IncludeMetrics"] = capo_cloudwatch.types.metric_name_list.serialize_cbor(
            value["include_metrics"]
        )
    return out


def deserialize_cbor(data: dict) -> ResourceMetricSelection:
    out: ResourceMetricSelection = {}  # type: ignore[typeddict-item]
    if data.get("IncludeMetrics") is not None:
        import capo_cloudwatch.types.metric_name_list

        out["include_metrics"] = (
            capo_cloudwatch.types.metric_name_list.deserialize_cbor(
                data["IncludeMetrics"]
            )
        )
    return out
