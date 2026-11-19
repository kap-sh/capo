"""Generated from Smithy shape ``com.amazonaws.shield#DescribeEmergencyContactSettingsRequest``."""

from typing_extensions import TypedDict


class DescribeEmergencyContactSettingsRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEmergencyContactSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEmergencyContactSettingsRequest:
    out: DescribeEmergencyContactSettingsRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEmergencyContactSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DescribeEmergencyContactSettingsRequest:
    out: DescribeEmergencyContactSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
