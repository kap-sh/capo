"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeregisterEventTopicResult``."""

from typing_extensions import TypedDict


class DeregisterEventTopicResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterEventTopicResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterEventTopicResult:
    out: DeregisterEventTopicResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeregisterEventTopicResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeregisterEventTopicResult:
    out: DeregisterEventTopicResult = {}  # type: ignore[typeddict-item]
    return out
