"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormEntityType``."""

from typing import Literal, TypeAlias, cast

RxNormEntityType: TypeAlias = Literal[
    "BRAND_NAME",
    "GENERIC_NAME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RxNormEntityType:
    return cast(RxNormEntityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RxNormEntityType) -> str:
    return value


def deserialize_cbor(data: str) -> RxNormEntityType:
    return cast(RxNormEntityType, data)
