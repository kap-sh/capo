"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TokenTypeIdentifierType``."""

from typing import Literal, TypeAlias, cast

TokenTypeIdentifierType: TypeAlias = Literal[
    "ACCESS_TOKEN",
    "ID_TOKEN",
    "SAML2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TokenTypeIdentifierType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TokenTypeIdentifierType:
    return cast(TokenTypeIdentifierType, data)
