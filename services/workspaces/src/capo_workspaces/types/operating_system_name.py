"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystemName``."""

from typing import Literal, TypeAlias, cast

OperatingSystemName: TypeAlias = Literal[
    "AMAZON_LINUX_2",
    "UBUNTU_18_04",
    "UBUNTU_20_04",
    "UBUNTU_22_04",
    "UNKNOWN",
    "WINDOWS_10",
    "WINDOWS_11",
    "WINDOWS_7",
    "WINDOWS_SERVER_2016",
    "WINDOWS_SERVER_2019",
    "WINDOWS_SERVER_2022",
    "WINDOWS_SERVER_2025",
    "RHEL_8",
    "ROCKY_8",
    "UBUNTU_24_04",
    "RHEL_9",
    "ROCKY_9",
    "UBUNTU_26_04",
    "RHEL_10",
    "ROCKY_10",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystemName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperatingSystemName:
    return cast(OperatingSystemName, data)
