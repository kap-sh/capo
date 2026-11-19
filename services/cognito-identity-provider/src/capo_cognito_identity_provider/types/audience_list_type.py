"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AudienceListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.audience_type

AudienceListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.audience_type.AudienceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AudienceListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AudienceListType:
    return [item for item in data if item is not None]
