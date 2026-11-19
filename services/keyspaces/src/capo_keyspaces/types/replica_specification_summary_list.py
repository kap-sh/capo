"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicaSpecificationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.replica_specification_summary

ReplicaSpecificationSummaryList: TypeAlias = list[
    "capo_keyspaces.types.replica_specification_summary.ReplicaSpecificationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaSpecificationSummaryList) -> list:
    import capo_keyspaces.types.replica_specification_summary

    out: list = []
    for item in value:
        out.append(
            capo_keyspaces.types.replica_specification_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaSpecificationSummaryList:
    import capo_keyspaces.types.replica_specification_summary

    out: ReplicaSpecificationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_keyspaces.types.replica_specification_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReplicaSpecificationSummaryList) -> list:
    import capo_keyspaces.types.replica_specification_summary

    out: list = []
    for item in value:
        out.append(
            capo_keyspaces.types.replica_specification_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ReplicaSpecificationSummaryList:
    import capo_keyspaces.types.replica_specification_summary

    out: ReplicaSpecificationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_keyspaces.types.replica_specification_summary.deserialize_cbor(item)
        )
    return out
