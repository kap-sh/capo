"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AcrConfigurationType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.acr_level_config_type
    import capo_cognito_identity_provider.types.acr_level_key_type

AcrConfigurationType: TypeAlias = dict[
    "capo_cognito_identity_provider.types.acr_level_key_type.AcrLevelKeyType",
    "capo_cognito_identity_provider.types.acr_level_config_type.AcrLevelConfigType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AcrConfigurationType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_cognito_identity_provider.types.acr_level_config_type

        out[key] = (
            capo_cognito_identity_provider.types.acr_level_config_type.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcrConfigurationType:
    out: AcrConfigurationType = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_cognito_identity_provider.types.acr_level_config_type

        out[key] = (
            capo_cognito_identity_provider.types.acr_level_config_type.deserialize_aws_json_1_1(
                value
            )
        )
    return out
