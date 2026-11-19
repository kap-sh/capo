"""Generated from Smithy shape ``com.amazonaws.directoryservice#SchemaExtensionStatus``."""

from typing import Literal, TypeAlias, cast

SchemaExtensionStatus: TypeAlias = Literal[
    "Initializing",
    "CreatingSnapshot",
    "UpdatingSchema",
    "Replicating",
    "CancelInProgress",
    "RollbackInProgress",
    "Cancelled",
    "Failed",
    "Completed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaExtensionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaExtensionStatus:
    return cast(SchemaExtensionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SchemaExtensionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> SchemaExtensionStatus:
    return cast(SchemaExtensionStatus, data)
