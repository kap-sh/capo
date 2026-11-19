"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

AppBlockBuilderStateChangeReasonCode: TypeAlias = Literal["INTERNAL_ERROR",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilderStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockBuilderStateChangeReasonCode:
    return cast(AppBlockBuilderStateChangeReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppBlockBuilderStateChangeReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> AppBlockBuilderStateChangeReasonCode:
    return cast(AppBlockBuilderStateChangeReasonCode, data)
