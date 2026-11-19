"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerDependencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_dependency

ContainerDependencyList: TypeAlias = list[
    "capo_gamelift.types.container_dependency.ContainerDependency"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDependencyList) -> list:
    import capo_gamelift.types.container_dependency

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_dependency.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerDependencyList:
    import capo_gamelift.types.container_dependency

    out: ContainerDependencyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_dependency.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerDependencyList) -> list:
    import capo_gamelift.types.container_dependency

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.container_dependency.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ContainerDependencyList:
    import capo_gamelift.types.container_dependency

    out: ContainerDependencyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.container_dependency.deserialize_cbor(item))
    return out
