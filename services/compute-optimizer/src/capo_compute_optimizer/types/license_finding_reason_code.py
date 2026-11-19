"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

LicenseFindingReasonCode: TypeAlias = Literal[
    "InvalidCloudWatchApplicationInsightsSetup",
    "CloudWatchApplicationInsightsError",
    "LicenseOverprovisioned",
    "Optimized",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseFindingReasonCode:
    return cast(LicenseFindingReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseFindingReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> LicenseFindingReasonCode:
    return cast(LicenseFindingReasonCode, data)
