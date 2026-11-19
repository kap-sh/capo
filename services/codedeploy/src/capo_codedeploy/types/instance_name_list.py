"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_name

InstanceNameList: TypeAlias = list["capo_codedeploy.types.instance_name.InstanceName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstanceNameList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceNameList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> InstanceNameList:
    return [item for item in data if item is not None]
