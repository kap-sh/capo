"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UsersListType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_type

UsersListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.user_type.UserType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsersListType) -> list:
    import capo_cognito_identity_provider.types.user_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.user_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsersListType:
    import capo_cognito_identity_provider.types.user_type

    out: UsersListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cognito_identity_provider.types.user_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: UsersListType) -> list[Any]:
    import capo_cognito_identity_provider.types.user_type

    return [
        capo_cognito_identity_provider.types.user_type.redact_sensitive(item)
        for item in value
    ]
