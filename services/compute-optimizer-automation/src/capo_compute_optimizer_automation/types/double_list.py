"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#DoubleList``."""

from typing import TypeAlias

DoubleList: TypeAlias = list["float"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DoubleList) -> list:
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


def deserialize_aws_json_1_0(data: list) -> DoubleList:
    return [float(item) for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DoubleList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DoubleList:
    return [float(item) for item in data if item is not None]
