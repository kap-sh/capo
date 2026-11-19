"""Generated from Smithy shape ``com.amazonaws.directconnect#CommunityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.community_entry

CommunityList: TypeAlias = list[
    "capo_direct_connect.types.community_entry.CommunityEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommunityList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CommunityList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CommunityList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CommunityList:
    return [item for item in data if item is not None]
