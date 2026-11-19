"""Generated from Smithy shape ``com.amazonaws.directoryservice#EnableCAEnrollmentPolicyResult``."""

from typing_extensions import TypedDict


class EnableCAEnrollmentPolicyResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableCAEnrollmentPolicyResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableCAEnrollmentPolicyResult:
    out: EnableCAEnrollmentPolicyResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableCAEnrollmentPolicyResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableCAEnrollmentPolicyResult:
    out: EnableCAEnrollmentPolicyResult = {}  # type: ignore[typeddict-item]
    return out
