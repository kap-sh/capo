"""Generated from Smithy shape ``com.amazonaws.appstream#PlatformType``."""

from typing import Literal, TypeAlias, cast

PlatformType: TypeAlias = Literal[
    "WINDOWS",
    "WINDOWS_SERVER_2016",
    "WINDOWS_SERVER_2019",
    "WINDOWS_SERVER_2022",
    "WINDOWS_SERVER_2025",
    "WINDOWS_11",
    "AMAZON_LINUX2",
    "RHEL8",
    "ROCKY_LINUX8",
    "UBUNTU_PRO_2404",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformType:
    return cast(PlatformType, data)
