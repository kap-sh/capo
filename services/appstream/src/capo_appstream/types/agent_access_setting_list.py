"""Generated from Smithy shape ``com.amazonaws.appstream#AgentAccessSettingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.agent_access_setting

AgentAccessSettingList: TypeAlias = list[
    "capo_appstream.types.agent_access_setting.AgentAccessSetting"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentAccessSettingList) -> list:
    import capo_appstream.types.agent_access_setting

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.agent_access_setting.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AgentAccessSettingList:
    import capo_appstream.types.agent_access_setting

    out: AgentAccessSettingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.agent_access_setting.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgentAccessSettingList) -> list:
    import capo_appstream.types.agent_access_setting

    out: list = []
    for item in value:
        out.append(capo_appstream.types.agent_access_setting.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AgentAccessSettingList:
    import capo_appstream.types.agent_access_setting

    out: AgentAccessSettingList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.agent_access_setting.deserialize_cbor(item))
    return out
