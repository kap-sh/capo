"""Generated from Smithy shape ``com.amazonaws.comprehend#DeleteEndpointResponse``."""

from typing_extensions import TypedDict


class DeleteEndpointResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEndpointResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEndpointResponse:
    out: DeleteEndpointResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteEndpointResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteEndpointResponse:
    out: DeleteEndpointResponse = {}  # type: ignore[typeddict-item]
    return out
