"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualInterfaceState``."""

from typing import Literal, TypeAlias, cast

VirtualInterfaceState: TypeAlias = Literal[
    "confirming",
    "verifying",
    "pending",
    "available",
    "down",
    "testing",
    "deleting",
    "deleted",
    "rejected",
    "unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualInterfaceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VirtualInterfaceState:
    return cast(VirtualInterfaceState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VirtualInterfaceState) -> str:
    return value


def deserialize_cbor(data: str) -> VirtualInterfaceState:
    return cast(VirtualInterfaceState, data)
