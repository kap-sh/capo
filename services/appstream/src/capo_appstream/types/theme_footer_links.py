"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeFooterLinks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.theme_footer_link

ThemeFooterLinks: TypeAlias = list[
    "capo_appstream.types.theme_footer_link.ThemeFooterLink"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThemeFooterLinks) -> list:
    import capo_appstream.types.theme_footer_link

    out: list = []
    for item in value:
        out.append(capo_appstream.types.theme_footer_link.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ThemeFooterLinks:
    import capo_appstream.types.theme_footer_link

    out: ThemeFooterLinks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.theme_footer_link.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThemeFooterLinks) -> list:
    import capo_appstream.types.theme_footer_link

    out: list = []
    for item in value:
        out.append(capo_appstream.types.theme_footer_link.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ThemeFooterLinks:
    import capo_appstream.types.theme_footer_link

    out: ThemeFooterLinks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.theme_footer_link.deserialize_cbor(item))
    return out
