"""Generated from Smithy shape ``com.amazonaws.shield#UpdateEmergencyContactSettingsResponse``."""

from typing_extensions import TypedDict


class UpdateEmergencyContactSettingsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEmergencyContactSettingsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEmergencyContactSettingsResponse:
    out: UpdateEmergencyContactSettingsResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateEmergencyContactSettingsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateEmergencyContactSettingsResponse:
    out: UpdateEmergencyContactSettingsResponse = {}  # type: ignore[typeddict-item]
    return out
