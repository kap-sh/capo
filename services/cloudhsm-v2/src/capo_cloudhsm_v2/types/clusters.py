"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Clusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cluster

Clusters: TypeAlias = list["capo_cloudhsm_v2.types.cluster.Cluster"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Clusters) -> list:
    import capo_cloudhsm_v2.types.cluster

    out: list = []
    for item in value:
        out.append(capo_cloudhsm_v2.types.cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Clusters:
    import capo_cloudhsm_v2.types.cluster

    out: Clusters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudhsm_v2.types.cluster.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Clusters) -> list:
    import capo_cloudhsm_v2.types.cluster

    out: list = []
    for item in value:
        out.append(capo_cloudhsm_v2.types.cluster.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Clusters:
    import capo_cloudhsm_v2.types.cluster

    out: Clusters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudhsm_v2.types.cluster.deserialize_cbor(item))
    return out
