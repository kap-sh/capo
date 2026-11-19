"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicationGroupStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.replication_group_status

ReplicationGroupStatusList: TypeAlias = list[
    "capo_keyspaces.types.replication_group_status.ReplicationGroupStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicationGroupStatusList) -> list:
    import capo_keyspaces.types.replication_group_status

    out: list = []
    for item in value:
        out.append(
            capo_keyspaces.types.replication_group_status.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicationGroupStatusList:
    import capo_keyspaces.types.replication_group_status

    out: ReplicationGroupStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_keyspaces.types.replication_group_status.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReplicationGroupStatusList) -> list:
    import capo_keyspaces.types.replication_group_status

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.replication_group_status.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ReplicationGroupStatusList:
    import capo_keyspaces.types.replication_group_status

    out: ReplicationGroupStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_keyspaces.types.replication_group_status.deserialize_cbor(item))
    return out
