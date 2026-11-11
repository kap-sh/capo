"""Generated from Smithy shape ``com.amazonaws.s3control#InstanceScope``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

InstanceScope: TypeAlias = Literal[
    "SELF",
    "ALL",
]


# --- restXml ser/de ---
def to_xml_text(value: InstanceScope) -> str:
    return value


def from_xml_text(text: str) -> InstanceScope:
    return cast(InstanceScope, text)


def serialize_xml(value: InstanceScope, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InstanceScope:
    return from_xml_text(el.text or "")
