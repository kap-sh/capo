"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicaAutoScalingSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.replica_auto_scaling_specification

ReplicaAutoScalingSpecificationList: TypeAlias = list[
    "capo_keyspaces.types.replica_auto_scaling_specification.ReplicaAutoScalingSpecification"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAutoScalingSpecificationList) -> list:
    import capo_keyspaces.types.replica_auto_scaling_specification

    out: list = []
    for item in value:
        out.append(
            capo_keyspaces.types.replica_auto_scaling_specification.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaAutoScalingSpecificationList:
    import capo_keyspaces.types.replica_auto_scaling_specification

    out: ReplicaAutoScalingSpecificationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_keyspaces.types.replica_auto_scaling_specification.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReplicaAutoScalingSpecificationList) -> list:
    import capo_keyspaces.types.replica_auto_scaling_specification

    out: list = []
    for item in value:
        out.append(
            capo_keyspaces.types.replica_auto_scaling_specification.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ReplicaAutoScalingSpecificationList:
    import capo_keyspaces.types.replica_auto_scaling_specification

    out: ReplicaAutoScalingSpecificationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_keyspaces.types.replica_auto_scaling_specification.deserialize_cbor(
                item
            )
        )
    return out
