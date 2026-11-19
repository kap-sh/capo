"""Generated from Smithy shape ``com.amazonaws.appstream#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.string

SecurityGroupIdList: TypeAlias = list["capo_appstream.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecurityGroupIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SecurityGroupIdList:
    return [item for item in data if item is not None]
