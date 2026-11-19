"""Generated from Smithy shape ``com.amazonaws.pi#PerformanceInsightsMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.descriptive_map
    import capo_pi.types.descriptive_string
    import capo_pi.types.double


class PerformanceInsightsMetric(TypedDict, closed=True):
    metric: NotRequired["capo_pi.types.descriptive_string.DescriptiveString"]
    """<p>The Performance Insights metric.</p>"""
    display_name: NotRequired["capo_pi.types.descriptive_string.DescriptiveString"]
    """<p>The Performance Insights metric name.</p>"""
    dimensions: NotRequired["capo_pi.types.descriptive_map.DescriptiveMap"]
    """<p>A dimension map that contains the dimensions for this partition.</p>"""
    filter: NotRequired["capo_pi.types.descriptive_map.DescriptiveMap"]
    """<p>The filter for the Performance Insights metric.</p>"""
    value: NotRequired["capo_pi.types.double.Double"]
    """<p>The value of the metric. For example, <code>9</code> for <code>db.load.avg</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PerformanceInsightsMetric) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "dimensions" in value:
        import capo_pi.types.descriptive_map

        out["Dimensions"] = capo_pi.types.descriptive_map.serialize_aws_json_1_1(
            value["dimensions"]
        )
    if "filter" in value:
        import capo_pi.types.descriptive_map

        out["Filter"] = capo_pi.types.descriptive_map.serialize_aws_json_1_1(
            value["filter"]
        )
    if "value" in value:
        out["Value"] = (
            "NaN"
            if value["value"] != value["value"]
            else "Infinity"
            if value["value"] == float("inf")
            else "-Infinity"
            if value["value"] == float("-inf")
            else value["value"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PerformanceInsightsMetric:
    out: PerformanceInsightsMetric = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Dimensions") is not None:
        import capo_pi.types.descriptive_map

        out["dimensions"] = capo_pi.types.descriptive_map.deserialize_aws_json_1_1(
            data["Dimensions"]
        )
    if data.get("Filter") is not None:
        import capo_pi.types.descriptive_map

        out["filter"] = capo_pi.types.descriptive_map.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PerformanceInsightsMetric) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "dimensions" in value:
        import capo_pi.types.descriptive_map

        out["Dimensions"] = capo_pi.types.descriptive_map.serialize_cbor(
            value["dimensions"]
        )
    if "filter" in value:
        import capo_pi.types.descriptive_map

        out["Filter"] = capo_pi.types.descriptive_map.serialize_cbor(value["filter"])
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> PerformanceInsightsMetric:
    out: PerformanceInsightsMetric = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Dimensions") is not None:
        import capo_pi.types.descriptive_map

        out["dimensions"] = capo_pi.types.descriptive_map.deserialize_cbor(
            data["Dimensions"]
        )
    if data.get("Filter") is not None:
        import capo_pi.types.descriptive_map

        out["filter"] = capo_pi.types.descriptive_map.deserialize_cbor(data["Filter"])
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out
