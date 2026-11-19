"""Generated from Smithy shape ``com.amazonaws.workspaces#UserSettingActionEnum``."""

from typing import Literal, TypeAlias, cast

UserSettingActionEnum: TypeAlias = Literal[
    "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
    "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
    "PRINTING_TO_LOCAL_DEVICE",
    "SMART_CARD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserSettingActionEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserSettingActionEnum:
    return cast(UserSettingActionEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UserSettingActionEnum) -> str:
    return value


def deserialize_cbor(data: str) -> UserSettingActionEnum:
    return cast(UserSettingActionEnum, data)
