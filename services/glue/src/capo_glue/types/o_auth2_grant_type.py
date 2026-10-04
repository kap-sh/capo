"""Generated from Smithy shape ``com.amazonaws.glue#OAuth2GrantType``."""

from typing import Literal, TypeAlias, cast

OAuth2GrantType: TypeAlias = Literal[
    "AUTHORIZATION_CODE",
    "CLIENT_CREDENTIALS",
    "JWT_BEARER",
    "REFRESH_TOKEN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OAuth2GrantType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OAuth2GrantType:
    return cast(OAuth2GrantType, data)
