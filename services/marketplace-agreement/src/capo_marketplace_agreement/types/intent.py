"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Intent``."""

from typing import Literal, TypeAlias, cast

Intent: TypeAlias = Literal[
    "NEW",
    "AMEND",
    "REPLACE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Intent) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Intent:
    return cast(Intent, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Intent) -> str:
    return value


def deserialize_cbor(data: str) -> Intent:
    return cast(Intent, data)
