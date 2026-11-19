"""Generated from Smithy shape ``com.amazonaws.fms#CustomerPolicyStatus``."""

from typing import Literal, TypeAlias, cast

CustomerPolicyStatus: TypeAlias = Literal[
    "ACTIVE",
    "OUT_OF_ADMIN_SCOPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerPolicyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomerPolicyStatus:
    return cast(CustomerPolicyStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomerPolicyStatus) -> str:
    return value


def deserialize_cbor(data: str) -> CustomerPolicyStatus:
    return cast(CustomerPolicyStatus, data)
