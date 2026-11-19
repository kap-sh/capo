"""Generated from Smithy shape ``com.amazonaws.gamelift#InstanceRoleCredentialsProvider``."""

from typing import Literal, TypeAlias, cast

InstanceRoleCredentialsProvider: TypeAlias = Literal["SHARED_CREDENTIAL_FILE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceRoleCredentialsProvider) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceRoleCredentialsProvider:
    return cast(InstanceRoleCredentialsProvider, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceRoleCredentialsProvider) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceRoleCredentialsProvider:
    return cast(InstanceRoleCredentialsProvider, data)
