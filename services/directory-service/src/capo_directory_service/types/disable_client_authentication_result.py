"""Generated from Smithy shape ``com.amazonaws.directoryservice#DisableClientAuthenticationResult``."""

from typing_extensions import TypedDict


class DisableClientAuthenticationResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableClientAuthenticationResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableClientAuthenticationResult:
    out: DisableClientAuthenticationResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableClientAuthenticationResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableClientAuthenticationResult:
    out: DisableClientAuthenticationResult = {}  # type: ignore[typeddict-item]
    return out
