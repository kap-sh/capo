"""Generated from Smithy shape ``com.amazonaws.directoryservice#Settings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.setting

Settings: TypeAlias = list["capo_directory_service.types.setting.Setting"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Settings) -> list:
    import capo_directory_service.types.setting

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.setting.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Settings:
    import capo_directory_service.types.setting

    out: Settings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.setting.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Settings) -> list:
    import capo_directory_service.types.setting

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.setting.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Settings:
    import capo_directory_service.types.setting

    out: Settings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.setting.deserialize_cbor(item))
    return out
