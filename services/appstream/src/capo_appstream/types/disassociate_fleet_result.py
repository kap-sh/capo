"""Generated from Smithy shape ``com.amazonaws.appstream#DisassociateFleetResult``."""

from typing_extensions import TypedDict


class DisassociateFleetResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFleetResult:
    out: DisassociateFleetResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateFleetResult:
    out: DisassociateFleetResult = {}  # type: ignore[typeddict-item]
    return out
