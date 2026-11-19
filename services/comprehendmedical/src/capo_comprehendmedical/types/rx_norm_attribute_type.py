"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormAttributeType``."""

from typing import Literal, TypeAlias, cast

RxNormAttributeType: TypeAlias = Literal[
    "DOSAGE",
    "DURATION",
    "FORM",
    "FREQUENCY",
    "RATE",
    "ROUTE_OR_MODE",
    "STRENGTH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RxNormAttributeType:
    return cast(RxNormAttributeType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RxNormAttributeType) -> str:
    return value


def deserialize_cbor(data: str) -> RxNormAttributeType:
    return cast(RxNormAttributeType, data)
