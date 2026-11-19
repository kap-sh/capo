"""Generated from Smithy shape ``com.amazonaws.codedeploy#ApplicationRevisionSortBy``."""

from typing import Literal, TypeAlias, cast

ApplicationRevisionSortBy: TypeAlias = Literal[
    "registerTime",
    "firstUsedTime",
    "lastUsedTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationRevisionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationRevisionSortBy:
    return cast(ApplicationRevisionSortBy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationRevisionSortBy) -> str:
    return value


def deserialize_cbor(data: str) -> ApplicationRevisionSortBy:
    return cast(ApplicationRevisionSortBy, data)
