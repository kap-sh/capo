"""Generated from Smithy shape ``com.amazonaws.directoryservice#EnableLDAPSResult``."""

from typing_extensions import TypedDict


class EnableLDAPSResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableLDAPSResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableLDAPSResult:
    out: EnableLDAPSResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableLDAPSResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableLDAPSResult:
    out: EnableLDAPSResult = {}  # type: ignore[typeddict-item]
    return out
