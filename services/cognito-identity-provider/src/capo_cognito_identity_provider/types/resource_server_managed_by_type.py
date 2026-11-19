"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ResourceServerManagedByType``."""

from typing import Literal, TypeAlias, cast

ResourceServerManagedByType: TypeAlias = Literal["COGNITO",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceServerManagedByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceServerManagedByType:
    return cast(ResourceServerManagedByType, data)
