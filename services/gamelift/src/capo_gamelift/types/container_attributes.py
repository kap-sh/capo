"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_attribute

ContainerAttributes: TypeAlias = list[
    "capo_gamelift.types.container_attribute.ContainerAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerAttributes) -> list:
    import capo_gamelift.types.container_attribute

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.container_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerAttributes:
    import capo_gamelift.types.container_attribute

    out: ContainerAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_attribute.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerAttributes) -> list:
    import capo_gamelift.types.container_attribute

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.container_attribute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ContainerAttributes:
    import capo_gamelift.types.container_attribute

    out: ContainerAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.container_attribute.deserialize_cbor(item))
    return out
