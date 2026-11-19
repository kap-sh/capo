"""Generated from Smithy shape ``com.amazonaws.pi#AdditionalMetricsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.double
    import capo_pi.types.request_string

AdditionalMetricsMap: TypeAlias = dict[
    "capo_pi.types.request_string.RequestString", "capo_pi.types.double.Double"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AdditionalMetricsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = (
            "NaN"
            if value != value
            else "Infinity"
            if value == float("inf")
            else "-Infinity"
            if value == float("-inf")
            else value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalMetricsMap:
    out: AdditionalMetricsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = float(value)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: AdditionalMetricsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> AdditionalMetricsMap:
    out: AdditionalMetricsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = float(value)
    return out
