"""Generated from Smithy shape ``com.amazonaws.shield#EnableApplicationLayerAutomaticResponseResponse``."""

from typing_extensions import TypedDict


class EnableApplicationLayerAutomaticResponseResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: EnableApplicationLayerAutomaticResponseResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> EnableApplicationLayerAutomaticResponseResponse:
    out: EnableApplicationLayerAutomaticResponseResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableApplicationLayerAutomaticResponseResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableApplicationLayerAutomaticResponseResponse:
    out: EnableApplicationLayerAutomaticResponseResponse = {}  # type: ignore[typeddict-item]
    return out
