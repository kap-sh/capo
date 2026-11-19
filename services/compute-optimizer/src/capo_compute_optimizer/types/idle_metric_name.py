"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleMetricName``."""

from typing import Literal, TypeAlias, cast

IdleMetricName: TypeAlias = Literal[
    "CPU",
    "Memory",
    "NetworkOutBytesPerSecond",
    "NetworkInBytesPerSecond",
    "DatabaseConnections",
    "EBSVolumeReadIOPS",
    "EBSVolumeWriteIOPS",
    "VolumeReadOpsPerSecond",
    "VolumeWriteOpsPerSecond",
    "ActiveConnectionCount",
    "PacketsInFromSource",
    "PacketsInFromDestination",
    "ConsumedReadCapacityUnits",
    "ConsumedWriteCapacityUnits",
    "ConsumedChangeDataCaptureUnits",
    "NewConnections",
    "EngineCPUUtilization",
    "CacheHits",
    "CacheMisses",
    "KeyspaceHits",
    "KeyspaceMisses",
    "IsIdle",
    "UserConnected",
    "Invocations",
    "GetTypeCmds",
    "SetTypeCmds",
    "ElastiCacheProcessingUnits",
    "CurrConnections",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdleMetricName:
    return cast(IdleMetricName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleMetricName) -> str:
    return value


def deserialize_cbor(data: str) -> IdleMetricName:
    return cast(IdleMetricName, data)
