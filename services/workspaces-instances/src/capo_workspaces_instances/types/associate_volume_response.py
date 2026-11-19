"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#AssociateVolumeResponse``."""

from typing_extensions import TypedDict


class AssociateVolumeResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateVolumeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateVolumeResponse:
    out: AssociateVolumeResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateVolumeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AssociateVolumeResponse:
    out: AssociateVolumeResponse = {}  # type: ignore[typeddict-item]
    return out
