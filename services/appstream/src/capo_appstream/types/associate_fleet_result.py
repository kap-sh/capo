"""Generated from Smithy shape ``com.amazonaws.appstream#AssociateFleetResult``."""

from typing_extensions import TypedDict


class AssociateFleetResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateFleetResult:
    out: AssociateFleetResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AssociateFleetResult:
    out: AssociateFleetResult = {}  # type: ignore[typeddict-item]
    return out
