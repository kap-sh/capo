"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RestorationListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.restoration_description_type

RestorationListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.restoration_description_type.RestorationDescriptionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestorationListType) -> list:
    import capo_cognito_identity_provider.types.restoration_description_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.restoration_description_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RestorationListType:
    import capo_cognito_identity_provider.types.restoration_description_type

    out: RestorationListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cognito_identity_provider.types.restoration_description_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
