"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateDirectorySetupResult``."""

from typing_extensions import TypedDict


class UpdateDirectorySetupResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDirectorySetupResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDirectorySetupResult:
    out: UpdateDirectorySetupResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateDirectorySetupResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateDirectorySetupResult:
    out: UpdateDirectorySetupResult = {}  # type: ignore[typeddict-item]
    return out
