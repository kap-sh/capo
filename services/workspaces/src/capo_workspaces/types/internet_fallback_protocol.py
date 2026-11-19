"""Generated from Smithy shape ``com.amazonaws.workspaces#InternetFallbackProtocol``."""

from typing import Literal, TypeAlias, cast

InternetFallbackProtocol: TypeAlias = Literal["PCOIP",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternetFallbackProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InternetFallbackProtocol:
    return cast(InternetFallbackProtocol, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InternetFallbackProtocol) -> str:
    return value


def deserialize_cbor(data: str) -> InternetFallbackProtocol:
    return cast(InternetFallbackProtocol, data)
