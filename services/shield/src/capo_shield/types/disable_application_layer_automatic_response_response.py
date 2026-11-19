"""Generated from Smithy shape ``com.amazonaws.shield#DisableApplicationLayerAutomaticResponseResponse``."""

from typing_extensions import TypedDict


class DisableApplicationLayerAutomaticResponseResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisableApplicationLayerAutomaticResponseResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisableApplicationLayerAutomaticResponseResponse:
    out: DisableApplicationLayerAutomaticResponseResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableApplicationLayerAutomaticResponseResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableApplicationLayerAutomaticResponseResponse:
    out: DisableApplicationLayerAutomaticResponseResponse = {}  # type: ignore[typeddict-item]
    return out
