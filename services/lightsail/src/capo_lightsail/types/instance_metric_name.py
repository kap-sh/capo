"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceMetricName``."""

from typing import Literal, TypeAlias, cast

InstanceMetricName: TypeAlias = Literal[
    "CPUUtilization",
    "NetworkIn",
    "NetworkOut",
    "StatusCheckFailed",
    "StatusCheckFailed_Instance",
    "StatusCheckFailed_System",
    "BurstCapacityTime",
    "BurstCapacityPercentage",
    "MetadataNoToken",
    "DiskReadOps",
    "DiskWriteOps",
    "DiskReadBytes",
    "DiskWriteBytes",
    "DiskTotalReadTime",
    "DiskTotalWriteTime",
    "DiskQueueLength",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceMetricName:
    return cast(InstanceMetricName, data)
