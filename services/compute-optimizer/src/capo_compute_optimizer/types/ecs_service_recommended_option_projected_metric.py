"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendedOptionProjectedMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.cpu_size
    import capo_compute_optimizer.types.ecs_service_projected_metrics
    import capo_compute_optimizer.types.memory_size


class ECSServiceRecommendedOptionProjectedMetric(TypedDict, closed=True):
    recommended_cpu_units: "capo_compute_optimizer.types.cpu_size.CpuSize"
    """<p> The recommended CPU size for the Amazon ECS service. </p>"""
    recommended_memory_size: "capo_compute_optimizer.types.memory_size.MemorySize"
    """<p> The recommended memory size for the Amazon ECS service. </p>"""
    projected_metrics: NotRequired[
        "capo_compute_optimizer.types.ecs_service_projected_metrics.ECSServiceProjectedMetrics"
    ]
    """<p> An array of objects that describe the projected metric. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendedOptionProjectedMetric) -> dict:
    out: dict = {}
    out["recommendedCpuUnits"] = value.get("recommended_cpu_units", 0)
    out["recommendedMemorySize"] = value.get("recommended_memory_size", 0)
    if "projected_metrics" in value:
        import capo_compute_optimizer.types.ecs_service_projected_metrics

        out["projectedMetrics"] = (
            capo_compute_optimizer.types.ecs_service_projected_metrics.serialize_aws_json_1_0(
                value["projected_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSServiceRecommendedOptionProjectedMetric:
    out: ECSServiceRecommendedOptionProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("recommendedCpuUnits") is not None:
        out["recommended_cpu_units"] = data["recommendedCpuUnits"]
    else:
        out["recommended_cpu_units"] = 0
    if data.get("recommendedMemorySize") is not None:
        out["recommended_memory_size"] = data["recommendedMemorySize"]
    else:
        out["recommended_memory_size"] = 0
    if data.get("projectedMetrics") is not None:
        import capo_compute_optimizer.types.ecs_service_projected_metrics

        out["projected_metrics"] = (
            capo_compute_optimizer.types.ecs_service_projected_metrics.deserialize_aws_json_1_0(
                data["projectedMetrics"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceRecommendedOptionProjectedMetric) -> dict:
    out: dict = {}
    out["recommendedCpuUnits"] = value.get("recommended_cpu_units", 0)
    out["recommendedMemorySize"] = value.get("recommended_memory_size", 0)
    if "projected_metrics" in value:
        import capo_compute_optimizer.types.ecs_service_projected_metrics

        out["projectedMetrics"] = (
            capo_compute_optimizer.types.ecs_service_projected_metrics.serialize_cbor(
                value["projected_metrics"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ECSServiceRecommendedOptionProjectedMetric:
    out: ECSServiceRecommendedOptionProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("recommendedCpuUnits") is not None:
        out["recommended_cpu_units"] = data["recommendedCpuUnits"]
    else:
        out["recommended_cpu_units"] = 0
    if data.get("recommendedMemorySize") is not None:
        out["recommended_memory_size"] = data["recommendedMemorySize"]
    else:
        out["recommended_memory_size"] = 0
    if data.get("projectedMetrics") is not None:
        import capo_compute_optimizer.types.ecs_service_projected_metrics

        out["projected_metrics"] = (
            capo_compute_optimizer.types.ecs_service_projected_metrics.deserialize_cbor(
                data["projectedMetrics"]
            )
        )
    return out
