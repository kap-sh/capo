"""Generated from Smithy shape ``com.amazonaws.directoryservice#CaEnrollmentPolicyStatus``."""

from typing import Literal, TypeAlias, cast

CaEnrollmentPolicyStatus: TypeAlias = Literal[
    "InProgress",
    "Success",
    "Failed",
    "Disabling",
    "Disabled",
    "Impaired",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaEnrollmentPolicyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CaEnrollmentPolicyStatus:
    return cast(CaEnrollmentPolicyStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CaEnrollmentPolicyStatus) -> str:
    return value


def deserialize_cbor(data: str) -> CaEnrollmentPolicyStatus:
    return cast(CaEnrollmentPolicyStatus, data)
