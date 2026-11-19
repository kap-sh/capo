"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicaSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.replica_specification

ReplicaSpecificationList: TypeAlias = list[
    "capo_keyspaces.types.replica_specification.ReplicaSpecification"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaSpecificationList) -> list:
    import capo_keyspaces.types.replica_specification

    out: list = []
    for item in value:
        out.append(
            capo_keyspaces.types.replica_specification.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaSpecificationList:
    import capo_keyspaces.types.replica_specification

    out: ReplicaSpecificationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_keyspaces.types.replica_specification.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReplicaSpecificationList) -> list:
    import capo_keyspaces.types.replica_specification

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.replica_specification.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ReplicaSpecificationList:
    import capo_keyspaces.types.replica_specification

    out: ReplicaSpecificationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_keyspaces.types.replica_specification.deserialize_cbor(item))
    return out
