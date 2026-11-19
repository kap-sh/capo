"""Generated from Smithy shape ``com.amazonaws.interconnect#BandwidthList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_interconnect.types.connection_bandwidth

BandwidthList: TypeAlias = list[
    "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BandwidthList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BandwidthList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BandwidthList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> BandwidthList:
    return [item for item in data if item is not None]
