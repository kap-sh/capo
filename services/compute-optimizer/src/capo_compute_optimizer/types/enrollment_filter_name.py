"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EnrollmentFilterName``."""

from typing import Literal, TypeAlias, cast

EnrollmentFilterName: TypeAlias = Literal["Status",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnrollmentFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnrollmentFilterName:
    return cast(EnrollmentFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnrollmentFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> EnrollmentFilterName:
    return cast(EnrollmentFilterName, data)
