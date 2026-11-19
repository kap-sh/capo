"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#GetEnrollmentConfigurationRequest``."""

from typing_extensions import TypedDict


class GetEnrollmentConfigurationRequest(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnrollmentConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnrollmentConfigurationRequest:
    out: GetEnrollmentConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetEnrollmentConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> GetEnrollmentConfigurationRequest:
    out: GetEnrollmentConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
