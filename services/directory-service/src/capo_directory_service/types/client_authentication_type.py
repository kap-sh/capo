"""Generated from Smithy shape ``com.amazonaws.directoryservice#ClientAuthenticationType``."""

from typing import Literal, TypeAlias, cast

ClientAuthenticationType: TypeAlias = Literal[
    "SmartCard",
    "SmartCardOrPassword",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientAuthenticationType:
    return cast(ClientAuthenticationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClientAuthenticationType) -> str:
    return value


def deserialize_cbor(data: str) -> ClientAuthenticationType:
    return cast(ClientAuthenticationType, data)
