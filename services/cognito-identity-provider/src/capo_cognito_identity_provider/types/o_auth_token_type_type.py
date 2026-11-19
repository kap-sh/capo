"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#OAuthTokenTypeType``."""

from typing import Literal, TypeAlias, cast

OAuthTokenTypeType: TypeAlias = Literal[
    "Bearer",
    "N_A",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OAuthTokenTypeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OAuthTokenTypeType:
    return cast(OAuthTokenTypeType, data)
