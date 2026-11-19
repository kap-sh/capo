"""Generated from Smithy shape ``com.amazonaws.workspaces#Tenancy``."""

from typing import Literal, TypeAlias, cast

Tenancy: TypeAlias = Literal[
    "DEDICATED",
    "SHARED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tenancy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Tenancy:
    return cast(Tenancy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Tenancy) -> str:
    return value


def deserialize_cbor(data: str) -> Tenancy:
    return cast(Tenancy, data)
