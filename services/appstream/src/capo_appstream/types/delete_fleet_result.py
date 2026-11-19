"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteFleetResult``."""

from typing_extensions import TypedDict


class DeleteFleetResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetResult:
    out: DeleteFleetResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteFleetResult:
    out: DeleteFleetResult = {}  # type: ignore[typeddict-item]
    return out
