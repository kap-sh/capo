"""Generated from Smithy shape ``com.amazonaws.snowball#UpdateClusterResult``."""

from typing_extensions import TypedDict


class UpdateClusterResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterResult:
    out: UpdateClusterResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateClusterResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateClusterResult:
    out: UpdateClusterResult = {}  # type: ignore[typeddict-item]
    return out
