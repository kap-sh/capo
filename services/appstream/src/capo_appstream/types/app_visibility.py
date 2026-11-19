"""Generated from Smithy shape ``com.amazonaws.appstream#AppVisibility``."""

from typing import Literal, TypeAlias, cast

AppVisibility: TypeAlias = Literal[
    "ALL",
    "ASSOCIATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppVisibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppVisibility:
    return cast(AppVisibility, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppVisibility) -> str:
    return value


def deserialize_cbor(data: str) -> AppVisibility:
    return cast(AppVisibility, data)
