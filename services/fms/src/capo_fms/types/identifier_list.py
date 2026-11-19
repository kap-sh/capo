"""Generated from Smithy shape ``com.amazonaws.fms#IdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.identifier

IdentifierList: TypeAlias = list["capo_fms.types.identifier.Identifier"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IdentifierList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentifierList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> IdentifierList:
    return [item for item in data if item is not None]
