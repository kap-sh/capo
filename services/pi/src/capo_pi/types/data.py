"""Generated from Smithy shape ``com.amazonaws.pi#Data``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.performance_insights_metric


class Data(TypedDict, closed=True):
    performance_insights_metric: NotRequired[
        "capo_pi.types.performance_insights_metric.PerformanceInsightsMetric"
    ]
    """<p>This field determines the Performance Insights metric to render for the insight. The <code>name</code> field refers to a Performance Insights metric. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Data) -> dict:
    out: dict = {}
    if "performance_insights_metric" in value:
        import capo_pi.types.performance_insights_metric

        out["PerformanceInsightsMetric"] = (
            capo_pi.types.performance_insights_metric.serialize_aws_json_1_1(
                value["performance_insights_metric"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Data:
    out: Data = {}  # type: ignore[typeddict-item]
    if data.get("PerformanceInsightsMetric") is not None:
        import capo_pi.types.performance_insights_metric

        out["performance_insights_metric"] = (
            capo_pi.types.performance_insights_metric.deserialize_aws_json_1_1(
                data["PerformanceInsightsMetric"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Data) -> dict:
    out: dict = {}
    if "performance_insights_metric" in value:
        import capo_pi.types.performance_insights_metric

        out["PerformanceInsightsMetric"] = (
            capo_pi.types.performance_insights_metric.serialize_cbor(
                value["performance_insights_metric"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Data:
    out: Data = {}  # type: ignore[typeddict-item]
    if data.get("PerformanceInsightsMetric") is not None:
        import capo_pi.types.performance_insights_metric

        out["performance_insights_metric"] = (
            capo_pi.types.performance_insights_metric.deserialize_cbor(
                data["PerformanceInsightsMetric"]
            )
        )
    return out
