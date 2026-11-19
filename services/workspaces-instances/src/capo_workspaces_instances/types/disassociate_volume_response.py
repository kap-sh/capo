"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#DisassociateVolumeResponse``."""

from typing_extensions import TypedDict


class DisassociateVolumeResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateVolumeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateVolumeResponse:
    out: DisassociateVolumeResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateVolumeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateVolumeResponse:
    out: DisassociateVolumeResponse = {}  # type: ignore[typeddict-item]
    return out
