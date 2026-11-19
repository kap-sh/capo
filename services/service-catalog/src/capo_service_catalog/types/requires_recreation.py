"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RequiresRecreation``."""

from typing import Literal, TypeAlias, cast

RequiresRecreation: TypeAlias = Literal[
    "NEVER",
    "CONDITIONALLY",
    "ALWAYS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequiresRecreation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RequiresRecreation:
    return cast(RequiresRecreation, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RequiresRecreation) -> str:
    return value


def deserialize_cbor(data: str) -> RequiresRecreation:
    return cast(RequiresRecreation, data)
