"""Generated from Smithy shape ``com.amazonaws.shield#UpdateApplicationLayerAutomaticResponseResponse``."""

from typing_extensions import TypedDict


class UpdateApplicationLayerAutomaticResponseResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateApplicationLayerAutomaticResponseResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateApplicationLayerAutomaticResponseResponse:
    out: UpdateApplicationLayerAutomaticResponseResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateApplicationLayerAutomaticResponseResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateApplicationLayerAutomaticResponseResponse:
    out: UpdateApplicationLayerAutomaticResponseResponse = {}  # type: ignore[typeddict-item]
    return out
