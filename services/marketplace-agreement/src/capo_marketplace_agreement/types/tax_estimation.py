"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#TaxEstimation``."""

from typing import Literal, TypeAlias, cast

TaxEstimation: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxEstimation) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TaxEstimation:
    return cast(TaxEstimation, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TaxEstimation) -> str:
    return value


def deserialize_cbor(data: str) -> TaxEstimation:
    return cast(TaxEstimation, data)
