"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListStateFilterAction``."""

from typing import Literal, TypeAlias, cast

ListStateFilterAction: TypeAlias = Literal[
    "include",
    "exclude",
    "ignore",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStateFilterAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListStateFilterAction:
    return cast(ListStateFilterAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListStateFilterAction) -> str:
    return value


def deserialize_cbor(data: str) -> ListStateFilterAction:
    return cast(ListStateFilterAction, data)
