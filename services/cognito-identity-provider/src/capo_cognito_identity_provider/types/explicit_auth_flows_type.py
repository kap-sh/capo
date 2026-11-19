"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ExplicitAuthFlowsType``."""

from typing import Literal, TypeAlias, cast

ExplicitAuthFlowsType: TypeAlias = Literal[
    "ADMIN_NO_SRP_AUTH",
    "CUSTOM_AUTH_FLOW_ONLY",
    "USER_PASSWORD_AUTH",
    "ALLOW_ADMIN_USER_PASSWORD_AUTH",
    "ALLOW_CUSTOM_AUTH",
    "ALLOW_USER_PASSWORD_AUTH",
    "ALLOW_USER_SRP_AUTH",
    "ALLOW_REFRESH_TOKEN_AUTH",
    "ALLOW_USER_AUTH",
    "ALLOW_TOKEN_EXCHANGE_DELEGATION",
    "ALLOW_TOKEN_EXCHANGE_IMPERSONATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExplicitAuthFlowsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExplicitAuthFlowsType:
    return cast(ExplicitAuthFlowsType, data)
