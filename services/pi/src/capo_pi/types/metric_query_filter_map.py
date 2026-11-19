"""Generated from Smithy shape ``com.amazonaws.pi#MetricQueryFilterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.request_string
    import capo_pi.types.sanitized_string

MetricQueryFilterMap: TypeAlias = dict[
    "capo_pi.types.sanitized_string.SanitizedString",
    "capo_pi.types.request_string.RequestString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MetricQueryFilterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricQueryFilterMap:
    out: MetricQueryFilterMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: MetricQueryFilterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> MetricQueryFilterMap:
    out: MetricQueryFilterMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
