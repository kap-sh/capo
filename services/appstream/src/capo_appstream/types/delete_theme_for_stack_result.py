"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteThemeForStackResult``."""

from typing_extensions import TypedDict


class DeleteThemeForStackResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteThemeForStackResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteThemeForStackResult:
    out: DeleteThemeForStackResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteThemeForStackResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteThemeForStackResult:
    out: DeleteThemeForStackResult = {}  # type: ignore[typeddict-item]
    return out
