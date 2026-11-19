"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SessionsListType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.session_description_type

SessionsListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.session_description_type.SessionDescriptionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionsListType) -> list:
    import capo_cognito_identity_provider.types.session_description_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.session_description_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SessionsListType:
    import capo_cognito_identity_provider.types.session_description_type

    out: SessionsListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cognito_identity_provider.types.session_description_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: SessionsListType) -> list[Any]:
    import capo_cognito_identity_provider.types.session_description_type

    return [
        capo_cognito_identity_provider.types.session_description_type.redact_sensitive(
            item
        )
        for item in value
    ]
