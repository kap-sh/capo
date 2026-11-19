"""Generated from Smithy shape ``com.amazonaws.cloudwatch#UntagResourceOutput``."""

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element


class UntagResourceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceOutput:
    out: UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagResourceOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> UntagResourceOutput:
    out: UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UntagResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UntagResourceOutput:
    out: UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out
