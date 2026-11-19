"""Generated from Smithy shape ``com.amazonaws.memorydb#UnprocessedClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.unprocessed_cluster

UnprocessedClusterList: TypeAlias = list[
    "capo_memorydb.types.unprocessed_cluster.UnprocessedCluster"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedClusterList) -> list:
    import capo_memorydb.types.unprocessed_cluster

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.unprocessed_cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UnprocessedClusterList:
    import capo_memorydb.types.unprocessed_cluster

    out: UnprocessedClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_memorydb.types.unprocessed_cluster.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UnprocessedClusterList) -> list:
    import capo_memorydb.types.unprocessed_cluster

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.unprocessed_cluster.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> UnprocessedClusterList:
    import capo_memorydb.types.unprocessed_cluster

    out: UnprocessedClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.unprocessed_cluster.deserialize_cbor(item))
    return out
