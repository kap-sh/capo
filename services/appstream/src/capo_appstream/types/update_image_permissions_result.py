"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateImagePermissionsResult``."""

from typing_extensions import TypedDict


class UpdateImagePermissionsResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImagePermissionsResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImagePermissionsResult:
    out: UpdateImagePermissionsResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateImagePermissionsResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateImagePermissionsResult:
    out: UpdateImagePermissionsResult = {}  # type: ignore[typeddict-item]
    return out
