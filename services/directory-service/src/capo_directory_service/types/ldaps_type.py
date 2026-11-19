"""Generated from Smithy shape ``com.amazonaws.directoryservice#LDAPSType``."""

from typing import Literal, TypeAlias, cast

LDAPSType: TypeAlias = Literal["Client",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LDAPSType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LDAPSType:
    return cast(LDAPSType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LDAPSType) -> str:
    return value


def deserialize_cbor(data: str) -> LDAPSType:
    return cast(LDAPSType, data)
