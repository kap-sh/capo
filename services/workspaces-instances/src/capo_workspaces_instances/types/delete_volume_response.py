"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#DeleteVolumeResponse``."""

from typing_extensions import TypedDict


class DeleteVolumeResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVolumeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVolumeResponse:
    out: DeleteVolumeResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteVolumeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteVolumeResponse:
    out: DeleteVolumeResponse = {}  # type: ignore[typeddict-item]
    return out
