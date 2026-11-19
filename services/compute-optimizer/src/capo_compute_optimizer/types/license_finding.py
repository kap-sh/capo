"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseFinding``."""

from typing import Literal, TypeAlias, cast

LicenseFinding: TypeAlias = Literal[
    "InsufficientMetrics",
    "Optimized",
    "NotOptimized",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseFinding:
    return cast(LicenseFinding, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseFinding) -> str:
    return value


def deserialize_cbor(data: str) -> LicenseFinding:
    return cast(LicenseFinding, data)
