"""Generated from Smithy shape ``com.amazonaws.directoryservice#ClientAuthenticationStatus``."""

from typing import Literal, TypeAlias, cast

ClientAuthenticationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientAuthenticationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientAuthenticationStatus:
    return cast(ClientAuthenticationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClientAuthenticationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ClientAuthenticationStatus:
    return cast(ClientAuthenticationStatus, data)
