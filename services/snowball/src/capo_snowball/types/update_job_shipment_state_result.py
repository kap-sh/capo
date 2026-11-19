"""Generated from Smithy shape ``com.amazonaws.snowball#UpdateJobShipmentStateResult``."""

from typing_extensions import TypedDict


class UpdateJobShipmentStateResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJobShipmentStateResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJobShipmentStateResult:
    out: UpdateJobShipmentStateResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateJobShipmentStateResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateJobShipmentStateResult:
    out: UpdateJobShipmentStateResult = {}  # type: ignore[typeddict-item]
    return out
