"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LookBackPeriodPreference``."""

from typing import Literal, TypeAlias, cast

LookBackPeriodPreference: TypeAlias = Literal[
    "DAYS_14",
    "DAYS_32",
    "DAYS_93",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LookBackPeriodPreference) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LookBackPeriodPreference:
    return cast(LookBackPeriodPreference, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LookBackPeriodPreference) -> str:
    return value


def deserialize_cbor(data: str) -> LookBackPeriodPreference:
    return cast(LookBackPeriodPreference, data)
