"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#IssuedTokenTypeIdentifierType``."""

from typing import Literal, TypeAlias, cast

IssuedTokenTypeIdentifierType: TypeAlias = Literal[
    "ACCESS_TOKEN",
    "ID_TOKEN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IssuedTokenTypeIdentifierType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IssuedTokenTypeIdentifierType:
    return cast(IssuedTokenTypeIdentifierType, data)
