"""Generated from Smithy shape ``com.amazonaws.s3#UseSourceMultiRegionKeyStatus``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

UseSourceMultiRegionKeyStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: UseSourceMultiRegionKeyStatus) -> str:
    return value


def from_xml_text(text: str) -> UseSourceMultiRegionKeyStatus:
    return cast(UseSourceMultiRegionKeyStatus, text)


def serialize_xml(
    value: UseSourceMultiRegionKeyStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> UseSourceMultiRegionKeyStatus:
    return from_xml_text(el.text or "")
