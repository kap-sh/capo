"""Generated from Smithy shape ``com.amazonaws.applicationinsights#GroupingType``."""

from typing import Literal, TypeAlias, cast

GroupingType: TypeAlias = Literal["ACCOUNT_BASED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GroupingType:
    return cast(GroupingType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GroupingType) -> str:
    return value


def deserialize_cbor(data: str) -> GroupingType:
    return cast(GroupingType, data)
