"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEnrollmentStatusRequest``."""

from typing_extensions import TypedDict


class GetEnrollmentStatusRequest(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnrollmentStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnrollmentStatusRequest:
    out: GetEnrollmentStatusRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetEnrollmentStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> GetEnrollmentStatusRequest:
    out: GetEnrollmentStatusRequest = {}  # type: ignore[typeddict-item]
    return out
