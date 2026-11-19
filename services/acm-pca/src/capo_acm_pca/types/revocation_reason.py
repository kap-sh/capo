"""Generated from Smithy shape ``com.amazonaws.acmpca#RevocationReason``."""

from typing import Literal, TypeAlias, cast

RevocationReason: TypeAlias = Literal[
    "UNSPECIFIED",
    "KEY_COMPROMISE",
    "CERTIFICATE_AUTHORITY_COMPROMISE",
    "AFFILIATION_CHANGED",
    "SUPERSEDED",
    "CESSATION_OF_OPERATION",
    "PRIVILEGE_WITHDRAWN",
    "A_A_COMPROMISE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevocationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RevocationReason:
    return cast(RevocationReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevocationReason) -> str:
    return value


def deserialize_cbor(data: str) -> RevocationReason:
    return cast(RevocationReason, data)
