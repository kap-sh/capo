"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerEnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_environment

ContainerEnvironmentList: TypeAlias = list[
    "capo_gamelift.types.container_environment.ContainerEnvironment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerEnvironmentList) -> list:
    import capo_gamelift.types.container_environment

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_environment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerEnvironmentList:
    import capo_gamelift.types.container_environment

    out: ContainerEnvironmentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_environment.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerEnvironmentList) -> list:
    import capo_gamelift.types.container_environment

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.container_environment.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ContainerEnvironmentList:
    import capo_gamelift.types.container_environment

    out: ContainerEnvironmentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.container_environment.deserialize_cbor(item))
    return out
