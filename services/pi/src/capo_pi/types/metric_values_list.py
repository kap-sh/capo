"""Generated from Smithy shape ``com.amazonaws.pi#MetricValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.double

MetricValuesList: TypeAlias = list["capo_pi.types.double.Double"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricValuesList) -> list:
    return [
        (
            "NaN"
            if item != item
            else "Infinity"
            if item == float("inf")
            else "-Infinity"
            if item == float("-inf")
            else item
        )
        for item in value
    ]


def deserialize_aws_json_1_1(data: list) -> MetricValuesList:
    return [float(item) for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricValuesList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> MetricValuesList:
    return [float(item) for item in data if item is not None]
