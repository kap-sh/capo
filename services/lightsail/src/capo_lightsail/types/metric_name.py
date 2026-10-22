"""Generated from Smithy shape ``com.amazonaws.lightsail#MetricName``."""

from typing import Literal, TypeAlias, cast

MetricName: TypeAlias = Literal[
    "CPUUtilization",
    "NetworkIn",
    "NetworkOut",
    "StatusCheckFailed",
    "StatusCheckFailed_Instance",
    "StatusCheckFailed_System",
    "ClientTLSNegotiationErrorCount",
    "HealthyHostCount",
    "UnhealthyHostCount",
    "HTTPCode_LB_4XX_Count",
    "HTTPCode_LB_5XX_Count",
    "HTTPCode_Instance_2XX_Count",
    "HTTPCode_Instance_3XX_Count",
    "HTTPCode_Instance_4XX_Count",
    "HTTPCode_Instance_5XX_Count",
    "InstanceResponseTime",
    "RejectedConnectionCount",
    "RequestCount",
    "DatabaseConnections",
    "DiskQueueDepth",
    "FreeStorageSpace",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
    "FreeableMemory",
    "SwapUsage",
    "BurstCapacityTime",
    "BurstCapacityPercentage",
    "DiskReadOps",
    "DiskWriteOps",
    "DiskReadBytes",
    "DiskWriteBytes",
    "DiskTotalReadTime",
    "DiskTotalWriteTime",
    "DiskQueueLength",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricName:
    return cast(MetricName, data)
