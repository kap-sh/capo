"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EnrollmentStatus``."""

from typing import Literal, TypeAlias, cast

EnrollmentStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
    "Pending",
    "Failed",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnrollmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnrollmentStatus:
    return cast(EnrollmentStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnrollmentStatus) -> str:
    return value


def deserialize_cbor(data: str) -> EnrollmentStatus:
    return cast(EnrollmentStatus, data)
