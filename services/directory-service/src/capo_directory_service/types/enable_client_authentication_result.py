"""Generated from Smithy shape ``com.amazonaws.directoryservice#EnableClientAuthenticationResult``."""

from typing_extensions import TypedDict


class EnableClientAuthenticationResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableClientAuthenticationResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableClientAuthenticationResult:
    out: EnableClientAuthenticationResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableClientAuthenticationResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableClientAuthenticationResult:
    out: EnableClientAuthenticationResult = {}  # type: ignore[typeddict-item]
    return out
