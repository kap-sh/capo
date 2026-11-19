"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ContainerConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.container_configuration

ContainerConfigurations: TypeAlias = list[
    "capo_compute_optimizer.types.container_configuration.ContainerConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerConfigurations) -> list:
    import capo_compute_optimizer.types.container_configuration

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.container_configuration.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ContainerConfigurations:
    import capo_compute_optimizer.types.container_configuration

    out: ContainerConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.container_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerConfigurations) -> list:
    import capo_compute_optimizer.types.container_configuration

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.container_configuration.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ContainerConfigurations:
    import capo_compute_optimizer.types.container_configuration

    out: ContainerConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.container_configuration.deserialize_cbor(item)
        )
    return out
