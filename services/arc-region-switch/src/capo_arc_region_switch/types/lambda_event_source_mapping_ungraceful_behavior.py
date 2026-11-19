"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#LambdaEventSourceMappingUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

LambdaEventSourceMappingUngracefulBehavior: TypeAlias = Literal["skip",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaEventSourceMappingUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaEventSourceMappingUngracefulBehavior:
    return cast(LambdaEventSourceMappingUngracefulBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaEventSourceMappingUngracefulBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> LambdaEventSourceMappingUngracefulBehavior:
    return cast(LambdaEventSourceMappingUngracefulBehavior, data)
