"""Generated from Smithy shape ``com.amazonaws.directoryservice#SettingEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.setting_entry

SettingEntries: TypeAlias = list[
    "capo_directory_service.types.setting_entry.SettingEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettingEntries) -> list:
    import capo_directory_service.types.setting_entry

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.setting_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SettingEntries:
    import capo_directory_service.types.setting_entry

    out: SettingEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.setting_entry.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SettingEntries) -> list:
    import capo_directory_service.types.setting_entry

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.setting_entry.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SettingEntries:
    import capo_directory_service.types.setting_entry

    out: SettingEntries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.setting_entry.deserialize_cbor(item))
    return out
