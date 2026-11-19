"""Generated from Smithy shape ``com.amazonaws.health#entityValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.entity_value

entityValueList: TypeAlias = list["capo_health.types.entity_value.entityValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: entityValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> entityValueList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: entityValueList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> entityValueList:
    return [item for item in data if item is not None]
