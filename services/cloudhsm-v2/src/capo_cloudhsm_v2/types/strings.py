"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Strings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.string

Strings: TypeAlias = list["capo_cloudhsm_v2.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Strings) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Strings:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Strings) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Strings:
    return [item for item in data if item is not None]
