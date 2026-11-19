"""Generated from Smithy shape ``com.amazonaws.shield#DisassociateHealthCheckResponse``."""

from typing_extensions import TypedDict


class DisassociateHealthCheckResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateHealthCheckResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateHealthCheckResponse:
    out: DisassociateHealthCheckResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateHealthCheckResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateHealthCheckResponse:
    out: DisassociateHealthCheckResponse = {}  # type: ignore[typeddict-item]
    return out
