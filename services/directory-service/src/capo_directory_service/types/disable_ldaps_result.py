"""Generated from Smithy shape ``com.amazonaws.directoryservice#DisableLDAPSResult``."""

from typing_extensions import TypedDict


class DisableLDAPSResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableLDAPSResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableLDAPSResult:
    out: DisableLDAPSResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableLDAPSResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableLDAPSResult:
    out: DisableLDAPSResult = {}  # type: ignore[typeddict-item]
    return out
