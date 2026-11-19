"""Generated from Smithy shape ``com.amazonaws.comprehend#DeleteFlywheelResponse``."""

from typing_extensions import TypedDict


class DeleteFlywheelResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFlywheelResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFlywheelResponse:
    out: DeleteFlywheelResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteFlywheelResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteFlywheelResponse:
    out: DeleteFlywheelResponse = {}  # type: ignore[typeddict-item]
    return out
