"""Generated from Smithy shape ``com.amazonaws.cloudfront#VpcIpAddressType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

"""IP address type supported for VPC Origins. IPv6-only is not supported for VPC Origins."""
VpcIpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
]


# --- restXml ser/de ---
def to_xml_text(value: VpcIpAddressType) -> str:
    return value


def from_xml_text(text: str) -> VpcIpAddressType:
    return cast(VpcIpAddressType, text)


def serialize_xml(value: VpcIpAddressType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> VpcIpAddressType:
    return from_xml_text(el.text or "")
