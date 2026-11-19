"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendedOptionProjectedMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.projected_metrics
    import capo_compute_optimizer.types.rank
    import capo_compute_optimizer.types.recommended_instance_type


class RecommendedOptionProjectedMetric(TypedDict, closed=True):
    recommended_instance_type: NotRequired[
        "capo_compute_optimizer.types.recommended_instance_type.RecommendedInstanceType"
    ]
    """<p>The recommended instance type.</p>"""
    rank: "capo_compute_optimizer.types.rank.Rank"
    """<p>The rank of the recommendation option projected metric.</p> <p>The top recommendation option is ranked as <code>1</code>.</p> <p>The projected metric rank correlates to the recommendation option rank. For example, the projected metric ranked as <code>1</code> is related to the recommendation option that is also ranked as <code>1</code> in the same response.</p>"""
    projected_metrics: NotRequired[
        "capo_compute_optimizer.types.projected_metrics.ProjectedMetrics"
    ]
    """<p>An array of objects that describe a projected utilization metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedOptionProjectedMetric) -> dict:
    out: dict = {}
    if "recommended_instance_type" in value:
        out["recommendedInstanceType"] = value["recommended_instance_type"]
    out["rank"] = value.get("rank", 0)
    if "projected_metrics" in value:
        import capo_compute_optimizer.types.projected_metrics

        out["projectedMetrics"] = (
            capo_compute_optimizer.types.projected_metrics.serialize_aws_json_1_0(
                value["projected_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendedOptionProjectedMetric:
    out: RecommendedOptionProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("recommendedInstanceType") is not None:
        out["recommended_instance_type"] = data["recommendedInstanceType"]
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("projectedMetrics") is not None:
        import capo_compute_optimizer.types.projected_metrics

        out["projected_metrics"] = (
            capo_compute_optimizer.types.projected_metrics.deserialize_aws_json_1_0(
                data["projectedMetrics"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendedOptionProjectedMetric) -> dict:
    out: dict = {}
    if "recommended_instance_type" in value:
        out["recommendedInstanceType"] = value["recommended_instance_type"]
    out["rank"] = value.get("rank", 0)
    if "projected_metrics" in value:
        import capo_compute_optimizer.types.projected_metrics

        out["projectedMetrics"] = (
            capo_compute_optimizer.types.projected_metrics.serialize_cbor(
                value["projected_metrics"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RecommendedOptionProjectedMetric:
    out: RecommendedOptionProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("recommendedInstanceType") is not None:
        out["recommended_instance_type"] = data["recommendedInstanceType"]
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("projectedMetrics") is not None:
        import capo_compute_optimizer.types.projected_metrics

        out["projected_metrics"] = (
            capo_compute_optimizer.types.projected_metrics.deserialize_cbor(
                data["projectedMetrics"]
            )
        )
    return out
