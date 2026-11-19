"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegisterEventTopicResult``."""

from typing_extensions import TypedDict


class RegisterEventTopicResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterEventTopicResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterEventTopicResult:
    out: RegisterEventTopicResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegisterEventTopicResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RegisterEventTopicResult:
    out: RegisterEventTopicResult = {}  # type: ignore[typeddict-item]
    return out
