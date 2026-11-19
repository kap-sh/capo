"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteRelayResponse``."""

from typing_extensions import TypedDict


class DeleteRelayResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRelayResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRelayResponse:
    out: DeleteRelayResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteRelayResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteRelayResponse:
    out: DeleteRelayResponse = {}  # type: ignore[typeddict-item]
    return out
