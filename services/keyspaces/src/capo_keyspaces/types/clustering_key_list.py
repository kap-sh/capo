"""Generated from Smithy shape ``com.amazonaws.keyspaces#ClusteringKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.clustering_key

ClusteringKeyList: TypeAlias = list["capo_keyspaces.types.clustering_key.ClusteringKey"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusteringKeyList) -> list:
    import capo_keyspaces.types.clustering_key

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.clustering_key.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ClusteringKeyList:
    import capo_keyspaces.types.clustering_key

    out: ClusteringKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_keyspaces.types.clustering_key.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClusteringKeyList) -> list:
    import capo_keyspaces.types.clustering_key

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.clustering_key.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ClusteringKeyList:
    import capo_keyspaces.types.clustering_key

    out: ClusteringKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_keyspaces.types.clustering_key.deserialize_cbor(item))
    return out
