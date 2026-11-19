"""Generated from Smithy shape ``com.amazonaws.directoryservice#DomainControllerStatus``."""

from typing import Literal, TypeAlias, cast

DomainControllerStatus: TypeAlias = Literal[
    "Creating",
    "Active",
    "Impaired",
    "Restoring",
    "Deleting",
    "Deleted",
    "Failed",
    "Updating",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainControllerStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainControllerStatus:
    return cast(DomainControllerStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainControllerStatus) -> str:
    return value


def deserialize_cbor(data: str) -> DomainControllerStatus:
    return cast(DomainControllerStatus, data)
