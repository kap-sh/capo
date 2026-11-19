"""Generated from Smithy shape ``com.amazonaws.directoryservice#TrustState``."""

from typing import Literal, TypeAlias, cast

TrustState: TypeAlias = Literal[
    "Creating",
    "Created",
    "Verifying",
    "VerifyFailed",
    "Verified",
    "Updating",
    "UpdateFailed",
    "Updated",
    "Deleting",
    "Deleted",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrustState:
    return cast(TrustState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TrustState) -> str:
    return value


def deserialize_cbor(data: str) -> TrustState:
    return cast(TrustState, data)
