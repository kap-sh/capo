"""Generated from Smithy shape ``com.amazonaws.directoryservice#ClientAuthenticationSettingsInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.client_authentication_setting_info

ClientAuthenticationSettingsInfo: TypeAlias = list[
    "capo_directory_service.types.client_authentication_setting_info.ClientAuthenticationSettingInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientAuthenticationSettingsInfo) -> list:
    import capo_directory_service.types.client_authentication_setting_info

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.client_authentication_setting_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClientAuthenticationSettingsInfo:
    import capo_directory_service.types.client_authentication_setting_info

    out: ClientAuthenticationSettingsInfo = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.client_authentication_setting_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClientAuthenticationSettingsInfo) -> list:
    import capo_directory_service.types.client_authentication_setting_info

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.client_authentication_setting_info.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ClientAuthenticationSettingsInfo:
    import capo_directory_service.types.client_authentication_setting_info

    out: ClientAuthenticationSettingsInfo = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.client_authentication_setting_info.deserialize_cbor(
                item
            )
        )
    return out
