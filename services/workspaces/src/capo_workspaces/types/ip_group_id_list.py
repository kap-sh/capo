"""Generated from Smithy shape ``com.amazonaws.workspaces#IpGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.ip_group_id

IpGroupIdList: TypeAlias = list["capo_workspaces.types.ip_group_id.IpGroupId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpGroupIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IpGroupIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpGroupIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> IpGroupIdList:
    return [item for item in data if item is not None]
