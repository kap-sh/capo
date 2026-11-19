"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBMetricName``."""

from typing import Literal, TypeAlias, cast

RDSDBMetricName: TypeAlias = Literal[
    "CPU",
    "Memory",
    "EBSVolumeStorageSpaceUtilization",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
    "EBSVolumeReadIOPS",
    "EBSVolumeWriteIOPS",
    "EBSVolumeReadThroughput",
    "EBSVolumeWriteThroughput",
    "DatabaseConnections",
    "StorageNetworkReceiveThroughput",
    "StorageNetworkTransmitThroughput",
    "AuroraMemoryHealthState",
    "AuroraMemoryNumDeclinedSql",
    "AuroraMemoryNumKillConnTotal",
    "AuroraMemoryNumKillQueryTotal",
    "ReadIOPSEphemeralStorage",
    "WriteIOPSEphemeralStorage",
    "VolumeReadIOPs",
    "VolumeBytesUsed",
    "VolumeWriteIOPs",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSDBMetricName:
    return cast(RDSDBMetricName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSDBMetricName) -> str:
    return value


def deserialize_cbor(data: str) -> RDSDBMetricName:
    return cast(RDSDBMetricName, data)
