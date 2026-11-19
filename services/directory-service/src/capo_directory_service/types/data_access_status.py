"""Generated from Smithy shape ``com.amazonaws.directoryservice#DataAccessStatus``."""

from typing import Literal, TypeAlias, cast

DataAccessStatus: TypeAlias = Literal[
    "Disabled",
    "Disabling",
    "Enabled",
    "Enabling",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataAccessStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataAccessStatus:
    return cast(DataAccessStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DataAccessStatus) -> str:
    return value


def deserialize_cbor(data: str) -> DataAccessStatus:
    return cast(DataAccessStatus, data)
