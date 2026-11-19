"""Generated from Smithy shape ``com.amazonaws.codebuild#HostKernel``."""

from typing import Literal, TypeAlias, cast

HostKernel: TypeAlias = Literal[
    "LINUX_KERNEL_4",
    "LINUX_KERNEL_6",
    "LINUX_KERNEL_LATEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostKernel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HostKernel:
    return cast(HostKernel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HostKernel) -> str:
    return value


def deserialize_cbor(data: str) -> HostKernel:
    return cast(HostKernel, data)
