"""Generated from Smithy shape ``com.amazonaws.directoryservice#DisableCAEnrollmentPolicyResult``."""

from typing_extensions import TypedDict


class DisableCAEnrollmentPolicyResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableCAEnrollmentPolicyResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableCAEnrollmentPolicyResult:
    out: DisableCAEnrollmentPolicyResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableCAEnrollmentPolicyResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableCAEnrollmentPolicyResult:
    out: DisableCAEnrollmentPolicyResult = {}  # type: ignore[typeddict-item]
    return out
