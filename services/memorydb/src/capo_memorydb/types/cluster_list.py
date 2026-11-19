"""Generated from Smithy shape ``com.amazonaws.memorydb#ClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.cluster

ClusterList: TypeAlias = list["capo_memorydb.types.cluster.Cluster"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterList) -> list:
    import capo_memorydb.types.cluster

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterList:
    import capo_memorydb.types.cluster

    out: ClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.cluster.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClusterList) -> list:
    import capo_memorydb.types.cluster

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.cluster.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ClusterList:
    import capo_memorydb.types.cluster

    out: ClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.cluster.deserialize_cbor(item))
    return out
