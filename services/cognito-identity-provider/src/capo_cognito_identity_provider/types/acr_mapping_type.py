"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AcrMappingType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.acr_mapping_key_type
    import capo_cognito_identity_provider.types.acr_value_type

AcrMappingType: TypeAlias = dict[
    "capo_cognito_identity_provider.types.acr_mapping_key_type.AcrMappingKeyType",
    "capo_cognito_identity_provider.types.acr_value_type.AcrValueType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AcrMappingType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> AcrMappingType:
    out: AcrMappingType = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
