"""Generated from Smithy shape ``com.amazonaws.servicediscovery#InstanceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.resource_id

InstanceIdList: TypeAlias = list["capo_servicediscovery.types.resource_id.ResourceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstanceIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> InstanceIdList:
    return [item for item in data if item is not None]
