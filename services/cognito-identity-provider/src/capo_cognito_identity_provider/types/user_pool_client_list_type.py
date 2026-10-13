"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolClientListType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_client_description

UserPoolClientListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.user_pool_client_description.UserPoolClientDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolClientListType) -> list:
    import capo_cognito_identity_provider.types.user_pool_client_description

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.user_pool_client_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserPoolClientListType:
    import capo_cognito_identity_provider.types.user_pool_client_description

    out: UserPoolClientListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cognito_identity_provider.types.user_pool_client_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: UserPoolClientListType) -> list[Any]:
    import capo_cognito_identity_provider.types.user_pool_client_description

    return [
        capo_cognito_identity_provider.types.user_pool_client_description.redact_sensitive(
            item
        )
        for item in value
    ]
