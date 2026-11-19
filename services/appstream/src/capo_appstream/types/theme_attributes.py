"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.theme_attribute

ThemeAttributes: TypeAlias = list["capo_appstream.types.theme_attribute.ThemeAttribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThemeAttributes) -> list:
    import capo_appstream.types.theme_attribute

    out: list = []
    for item in value:
        out.append(capo_appstream.types.theme_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ThemeAttributes:
    import capo_appstream.types.theme_attribute

    out: ThemeAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.theme_attribute.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThemeAttributes) -> list:
    import capo_appstream.types.theme_attribute

    out: list = []
    for item in value:
        out.append(capo_appstream.types.theme_attribute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ThemeAttributes:
    import capo_appstream.types.theme_attribute

    out: ThemeAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.theme_attribute.deserialize_cbor(item))
    return out
