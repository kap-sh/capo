"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationPrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.prefix

ReplicationPrefixList: TypeAlias = list["capo_s3.types.prefix.Prefix"]


# --- restXml ser/de ---
def serialize_xml(value: ReplicationPrefixList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "Prefix").text = str(item)


def deserialize_xml(el: Element) -> ReplicationPrefixList:
    out: ReplicationPrefixList = []
    for child in el.findall("Prefix"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: ReplicationPrefixList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> ReplicationPrefixList:
    out: ReplicationPrefixList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
