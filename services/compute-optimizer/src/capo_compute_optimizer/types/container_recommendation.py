"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ContainerRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.container_name
    import capo_compute_optimizer.types.memory_size_configuration
    import capo_compute_optimizer.types.nullable_cpu


class ContainerRecommendation(TypedDict, closed=True):
    container_name: NotRequired[
        "capo_compute_optimizer.types.container_name.ContainerName"
    ]
    """<p> The name of the container. </p>"""
    memory_size_configuration: NotRequired[
        "capo_compute_optimizer.types.memory_size_configuration.MemorySizeConfiguration"
    ]
    """<p> The recommended memory size configurations for the container. </p>"""
    cpu: NotRequired["capo_compute_optimizer.types.nullable_cpu.NullableCpu"]
    """<p> The recommended number of CPU units reserved for the container. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerRecommendation) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "memory_size_configuration" in value:
        import capo_compute_optimizer.types.memory_size_configuration

        out["memorySizeConfiguration"] = (
            capo_compute_optimizer.types.memory_size_configuration.serialize_aws_json_1_0(
                value["memory_size_configuration"]
            )
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ContainerRecommendation:
    out: ContainerRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    if data.get("memorySizeConfiguration") is not None:
        import capo_compute_optimizer.types.memory_size_configuration

        out["memory_size_configuration"] = (
            capo_compute_optimizer.types.memory_size_configuration.deserialize_aws_json_1_0(
                data["memorySizeConfiguration"]
            )
        )
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerRecommendation) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "memory_size_configuration" in value:
        import capo_compute_optimizer.types.memory_size_configuration

        out["memorySizeConfiguration"] = (
            capo_compute_optimizer.types.memory_size_configuration.serialize_cbor(
                value["memory_size_configuration"]
            )
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    return out


def deserialize_cbor(data: dict) -> ContainerRecommendation:
    out: ContainerRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    if data.get("memorySizeConfiguration") is not None:
        import capo_compute_optimizer.types.memory_size_configuration

        out["memory_size_configuration"] = (
            capo_compute_optimizer.types.memory_size_configuration.deserialize_cbor(
                data["memorySizeConfiguration"]
            )
        )
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    return out
