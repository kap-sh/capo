"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AccessLevelFilterKey``."""

from typing import Literal, TypeAlias, cast

AccessLevelFilterKey: TypeAlias = Literal[
    "Account",
    "Role",
    "User",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessLevelFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessLevelFilterKey:
    return cast(AccessLevelFilterKey, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessLevelFilterKey) -> str:
    return value


def deserialize_cbor(data: str) -> AccessLevelFilterKey:
    return cast(AccessLevelFilterKey, data)
