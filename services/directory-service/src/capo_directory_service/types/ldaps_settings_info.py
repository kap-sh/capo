"""Generated from Smithy shape ``com.amazonaws.directoryservice#LDAPSSettingsInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.ldaps_setting_info

LDAPSSettingsInfo: TypeAlias = list[
    "capo_directory_service.types.ldaps_setting_info.LDAPSSettingInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LDAPSSettingsInfo) -> list:
    import capo_directory_service.types.ldaps_setting_info

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.ldaps_setting_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LDAPSSettingsInfo:
    import capo_directory_service.types.ldaps_setting_info

    out: LDAPSSettingsInfo = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.ldaps_setting_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LDAPSSettingsInfo) -> list:
    import capo_directory_service.types.ldaps_setting_info

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.ldaps_setting_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LDAPSSettingsInfo:
    import capo_directory_service.types.ldaps_setting_info

    out: LDAPSSettingsInfo = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.ldaps_setting_info.deserialize_cbor(item)
        )
    return out
