"""Generated from Smithy shape ``com.amazonaws.directoryservice#TopicStatus``."""

from typing import Literal, TypeAlias, cast

TopicStatus: TypeAlias = Literal[
    "Registered",
    "Topic not found",
    "Failed",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TopicStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TopicStatus:
    return cast(TopicStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TopicStatus) -> str:
    return value


def deserialize_cbor(data: str) -> TopicStatus:
    return cast(TopicStatus, data)
