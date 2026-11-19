"""Generated from Smithy shape ``com.amazonaws.workspaces#UserSettingPermissionEnum``."""

from typing import Literal, TypeAlias, cast

UserSettingPermissionEnum: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserSettingPermissionEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserSettingPermissionEnum:
    return cast(UserSettingPermissionEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UserSettingPermissionEnum) -> str:
    return value


def deserialize_cbor(data: str) -> UserSettingPermissionEnum:
    return cast(UserSettingPermissionEnum, data)
