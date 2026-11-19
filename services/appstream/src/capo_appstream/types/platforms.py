"""Generated from Smithy shape ``com.amazonaws.appstream#Platforms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.platform_type

Platforms: TypeAlias = list["capo_appstream.types.platform_type.PlatformType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Platforms) -> list:
    import capo_appstream.types.platform_type

    out: list = []
    for item in value:
        out.append(capo_appstream.types.platform_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Platforms:
    import capo_appstream.types.platform_type

    out: Platforms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.platform_type.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Platforms) -> list:
    import capo_appstream.types.platform_type

    out: list = []
    for item in value:
        out.append(capo_appstream.types.platform_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Platforms:
    import capo_appstream.types.platform_type

    out: Platforms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.platform_type.deserialize_cbor(item))
    return out
