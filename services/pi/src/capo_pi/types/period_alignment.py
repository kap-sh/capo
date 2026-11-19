"""Generated from Smithy shape ``com.amazonaws.pi#PeriodAlignment``."""

from typing import Literal, TypeAlias, cast

PeriodAlignment: TypeAlias = Literal[
    "END_TIME",
    "START_TIME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PeriodAlignment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PeriodAlignment:
    return cast(PeriodAlignment, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PeriodAlignment) -> str:
    return value


def deserialize_cbor(data: str) -> PeriodAlignment:
    return cast(PeriodAlignment, data)
