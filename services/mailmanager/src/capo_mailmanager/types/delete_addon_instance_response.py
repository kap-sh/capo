"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteAddonInstanceResponse``."""

from typing_extensions import TypedDict


class DeleteAddonInstanceResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAddonInstanceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAddonInstanceResponse:
    out: DeleteAddonInstanceResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAddonInstanceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAddonInstanceResponse:
    out: DeleteAddonInstanceResponse = {}  # type: ignore[typeddict-item]
    return out
