"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricName``."""

from typing import Literal, TypeAlias, cast

MetricName: TypeAlias = Literal[
    "Cpu",
    "Memory",
    "EBS_READ_OPS_PER_SECOND",
    "EBS_WRITE_OPS_PER_SECOND",
    "EBS_READ_BYTES_PER_SECOND",
    "EBS_WRITE_BYTES_PER_SECOND",
    "DISK_READ_OPS_PER_SECOND",
    "DISK_WRITE_OPS_PER_SECOND",
    "DISK_READ_BYTES_PER_SECOND",
    "DISK_WRITE_BYTES_PER_SECOND",
    "NETWORK_IN_BYTES_PER_SECOND",
    "NETWORK_OUT_BYTES_PER_SECOND",
    "NETWORK_PACKETS_IN_PER_SECOND",
    "NETWORK_PACKETS_OUT_PER_SECOND",
    "GPU_PERCENTAGE",
    "GPU_MEMORY_PERCENTAGE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricName:
    return cast(MetricName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricName) -> str:
    return value


def deserialize_cbor(data: str) -> MetricName:
    return cast(MetricName, data)
