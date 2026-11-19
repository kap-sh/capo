"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RestorePreviewListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.restore_preview_type

RestorePreviewListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.restore_preview_type.RestorePreviewType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestorePreviewListType) -> list:
    import capo_cognito_identity_provider.types.restore_preview_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.restore_preview_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RestorePreviewListType:
    import capo_cognito_identity_provider.types.restore_preview_type

    out: RestorePreviewListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cognito_identity_provider.types.restore_preview_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
