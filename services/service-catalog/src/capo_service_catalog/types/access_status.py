"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AccessStatus``."""

from typing import Literal, TypeAlias, cast

AccessStatus: TypeAlias = Literal[
    "ENABLED",
    "UNDER_CHANGE",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessStatus:
    return cast(AccessStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AccessStatus:
    return cast(AccessStatus, data)
