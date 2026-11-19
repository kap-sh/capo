"""Generated from Smithy shape ``com.amazonaws.directoryservice#EnableDirectoryDataAccessResult``."""

from typing_extensions import TypedDict


class EnableDirectoryDataAccessResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableDirectoryDataAccessResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableDirectoryDataAccessResult:
    out: EnableDirectoryDataAccessResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableDirectoryDataAccessResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableDirectoryDataAccessResult:
    out: EnableDirectoryDataAccessResult = {}  # type: ignore[typeddict-item]
    return out
