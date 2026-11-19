"""Generated from Smithy shape ``com.amazonaws.workspaces#UserIdentityType``."""

from typing import Literal, TypeAlias, cast

UserIdentityType: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_DIRECTORY_SERVICE",
    "AWS_IAM_IDENTITY_CENTER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserIdentityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserIdentityType:
    return cast(UserIdentityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UserIdentityType) -> str:
    return value


def deserialize_cbor(data: str) -> UserIdentityType:
    return cast(UserIdentityType, data)
