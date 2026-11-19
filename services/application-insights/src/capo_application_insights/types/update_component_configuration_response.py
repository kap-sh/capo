"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateComponentConfigurationResponse``."""

from typing_extensions import TypedDict


class UpdateComponentConfigurationResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateComponentConfigurationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateComponentConfigurationResponse:
    out: UpdateComponentConfigurationResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateComponentConfigurationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateComponentConfigurationResponse:
    out: UpdateComponentConfigurationResponse = {}  # type: ignore[typeddict-item]
    return out
