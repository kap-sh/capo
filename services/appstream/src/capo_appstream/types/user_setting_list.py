"""Generated from Smithy shape ``com.amazonaws.appstream#UserSettingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.user_setting

UserSettingList: TypeAlias = list["capo_appstream.types.user_setting.UserSetting"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserSettingList) -> list:
    import capo_appstream.types.user_setting

    out: list = []
    for item in value:
        out.append(capo_appstream.types.user_setting.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UserSettingList:
    import capo_appstream.types.user_setting

    out: UserSettingList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.user_setting.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UserSettingList) -> list:
    import capo_appstream.types.user_setting

    out: list = []
    for item in value:
        out.append(capo_appstream.types.user_setting.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> UserSettingList:
    import capo_appstream.types.user_setting

    out: UserSettingList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.user_setting.deserialize_cbor(item))
    return out
