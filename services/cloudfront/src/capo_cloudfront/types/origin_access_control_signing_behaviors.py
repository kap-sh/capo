"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlSigningBehaviors``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

OriginAccessControlSigningBehaviors: TypeAlias = Literal[
    "never",
    "always",
    "no-override",
    "always-amz-auth",
]


# --- restXml ser/de ---
def to_xml_text(value: OriginAccessControlSigningBehaviors) -> str:
    return value


def from_xml_text(text: str) -> OriginAccessControlSigningBehaviors:
    return cast(OriginAccessControlSigningBehaviors, text)


def serialize_xml(
    value: OriginAccessControlSigningBehaviors, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginAccessControlSigningBehaviors:
    return from_xml_text(el.text or "")
