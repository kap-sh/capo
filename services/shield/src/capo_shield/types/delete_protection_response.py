"""Generated from Smithy shape ``com.amazonaws.shield#DeleteProtectionResponse``."""

from typing_extensions import TypedDict


class DeleteProtectionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProtectionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProtectionResponse:
    out: DeleteProtectionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteProtectionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteProtectionResponse:
    out: DeleteProtectionResponse = {}  # type: ignore[typeddict-item]
    return out
