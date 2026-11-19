"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderAttribute``."""

from typing import Literal, TypeAlias, cast

AppBlockBuilderAttribute: TypeAlias = Literal[
    "IAM_ROLE_ARN",
    "ACCESS_ENDPOINTS",
    "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilderAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockBuilderAttribute:
    return cast(AppBlockBuilderAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppBlockBuilderAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> AppBlockBuilderAttribute:
    return cast(AppBlockBuilderAttribute, data)
