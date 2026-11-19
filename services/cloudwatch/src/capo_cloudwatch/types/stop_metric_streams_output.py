"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StopMetricStreamsOutput``."""

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element


class StopMetricStreamsOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopMetricStreamsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> StopMetricStreamsOutput:
    out: StopMetricStreamsOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: StopMetricStreamsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> StopMetricStreamsOutput:
    out: StopMetricStreamsOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopMetricStreamsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopMetricStreamsOutput:
    out: StopMetricStreamsOutput = {}  # type: ignore[typeddict-item]
    return out
