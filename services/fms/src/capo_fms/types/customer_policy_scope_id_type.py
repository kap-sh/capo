"""Generated from Smithy shape ``com.amazonaws.fms#CustomerPolicyScopeIdType``."""

from typing import Literal, TypeAlias, cast

CustomerPolicyScopeIdType: TypeAlias = Literal[
    "ACCOUNT",
    "ORG_UNIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerPolicyScopeIdType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomerPolicyScopeIdType:
    return cast(CustomerPolicyScopeIdType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomerPolicyScopeIdType) -> str:
    return value


def deserialize_cbor(data: str) -> CustomerPolicyScopeIdType:
    return cast(CustomerPolicyScopeIdType, data)
