"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeviceListType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_type

DeviceListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.device_type.DeviceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceListType) -> list:
    import capo_cognito_identity_provider.types.device_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.device_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeviceListType:
    import capo_cognito_identity_provider.types.device_type

    out: DeviceListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cognito_identity_provider.types.device_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: DeviceListType) -> list[Any]:
    import capo_cognito_identity_provider.types.device_type

    return [
        capo_cognito_identity_provider.types.device_type.redact_sensitive(item)
        for item in value
    ]
