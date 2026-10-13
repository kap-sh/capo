"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ClientSecretDescriptorListType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_secret_descriptor_type

ClientSecretDescriptorListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.client_secret_descriptor_type.ClientSecretDescriptorType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientSecretDescriptorListType) -> list:
    import capo_cognito_identity_provider.types.client_secret_descriptor_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.client_secret_descriptor_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClientSecretDescriptorListType:
    import capo_cognito_identity_provider.types.client_secret_descriptor_type

    out: ClientSecretDescriptorListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cognito_identity_provider.types.client_secret_descriptor_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: ClientSecretDescriptorListType) -> list[Any]:
    import capo_cognito_identity_provider.types.client_secret_descriptor_type

    return [
        capo_cognito_identity_provider.types.client_secret_descriptor_type.redact_sensitive(
            item
        )
        for item in value
    ]
