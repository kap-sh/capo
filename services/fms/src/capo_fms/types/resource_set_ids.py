"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.base62_id

ResourceSetIds: TypeAlias = list["capo_fms.types.base62_id.Base62Id"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSetIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceSetIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceSetIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ResourceSetIds:
    return [item for item in data if item is not None]
