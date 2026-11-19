"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserSessionTrackingType``."""

from typing import Literal, TypeAlias, cast

UserSessionTrackingType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserSessionTrackingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserSessionTrackingType:
    return cast(UserSessionTrackingType, data)
