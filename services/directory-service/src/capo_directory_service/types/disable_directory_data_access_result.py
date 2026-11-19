"""Generated from Smithy shape ``com.amazonaws.directoryservice#DisableDirectoryDataAccessResult``."""

from typing_extensions import TypedDict


class DisableDirectoryDataAccessResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableDirectoryDataAccessResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableDirectoryDataAccessResult:
    out: DisableDirectoryDataAccessResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableDirectoryDataAccessResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableDirectoryDataAccessResult:
    out: DisableDirectoryDataAccessResult = {}  # type: ignore[typeddict-item]
    return out
