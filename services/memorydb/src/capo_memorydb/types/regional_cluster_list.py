"""Generated from Smithy shape ``com.amazonaws.memorydb#RegionalClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.regional_cluster

RegionalClusterList: TypeAlias = list[
    "capo_memorydb.types.regional_cluster.RegionalCluster"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionalClusterList) -> list:
    import capo_memorydb.types.regional_cluster

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.regional_cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegionalClusterList:
    import capo_memorydb.types.regional_cluster

    out: RegionalClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.regional_cluster.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegionalClusterList) -> list:
    import capo_memorydb.types.regional_cluster

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.regional_cluster.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RegionalClusterList:
    import capo_memorydb.types.regional_cluster

    out: RegionalClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.regional_cluster.deserialize_cbor(item))
    return out
