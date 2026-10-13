"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AttributeListType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.attribute_type

AttributeListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.attribute_type.AttributeType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeListType) -> list:
    import capo_cognito_identity_provider.types.attribute_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.attribute_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AttributeListType:
    import capo_cognito_identity_provider.types.attribute_type

    out: AttributeListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cognito_identity_provider.types.attribute_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: AttributeListType) -> list[Any]:
    import capo_cognito_identity_provider.types.attribute_type

    return [
        capo_cognito_identity_provider.types.attribute_type.redact_sensitive(item)
        for item in value
    ]
