"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSFilterName``."""

from typing import Literal, TypeAlias, cast

EBSFilterName: TypeAlias = Literal["Finding",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EBSFilterName:
    return cast(EBSFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EBSFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> EBSFilterName:
    return cast(EBSFilterName, data)
