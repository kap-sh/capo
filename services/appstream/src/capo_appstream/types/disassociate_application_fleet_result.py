"""Generated from Smithy shape ``com.amazonaws.appstream#DisassociateApplicationFleetResult``."""

from typing_extensions import TypedDict


class DisassociateApplicationFleetResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateApplicationFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateApplicationFleetResult:
    out: DisassociateApplicationFleetResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateApplicationFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateApplicationFleetResult:
    out: DisassociateApplicationFleetResult = {}  # type: ignore[typeddict-item]
    return out
