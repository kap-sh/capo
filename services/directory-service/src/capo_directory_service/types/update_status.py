"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateStatus``."""

from typing import Literal, TypeAlias, cast

UpdateStatus: TypeAlias = Literal[
    "Updated",
    "Updating",
    "UpdateFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateStatus:
    return cast(UpdateStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateStatus) -> str:
    return value


def deserialize_cbor(data: str) -> UpdateStatus:
    return cast(UpdateStatus, data)
