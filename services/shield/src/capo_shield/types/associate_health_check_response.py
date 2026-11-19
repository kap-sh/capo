"""Generated from Smithy shape ``com.amazonaws.shield#AssociateHealthCheckResponse``."""

from typing_extensions import TypedDict


class AssociateHealthCheckResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateHealthCheckResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateHealthCheckResponse:
    out: AssociateHealthCheckResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateHealthCheckResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AssociateHealthCheckResponse:
    out: AssociateHealthCheckResponse = {}  # type: ignore[typeddict-item]
    return out
