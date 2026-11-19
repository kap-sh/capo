"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstancesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_id

InstancesList: TypeAlias = list["capo_codedeploy.types.instance_id.InstanceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstancesList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstancesList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> InstancesList:
    return [item for item in data if item is not None]
