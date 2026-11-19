"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ResourceListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.resource_server_identifier_type

ResourceListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.resource_server_identifier_type.ResourceServerIdentifierType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceListType:
    return [item for item in data if item is not None]
