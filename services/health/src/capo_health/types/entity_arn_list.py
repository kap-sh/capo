"""Generated from Smithy shape ``com.amazonaws.health#entityArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.entity_arn

entityArnList: TypeAlias = list["capo_health.types.entity_arn.entityArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: entityArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> entityArnList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: entityArnList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> entityArnList:
    return [item for item in data if item is not None]
