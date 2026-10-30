"""Shared XML protocol runtime.

Hand-written, not regenerated. Holds re-exports of
``xml.etree.ElementTree`` primitives generated code depends on.
"""

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.etree.ElementTree import fromstring as _fromstring


def fromstring(text: str | bytes) -> Element:
    """Parse XML and strip namespaces so generated ``el.find("Tag")`` and
    ``el.get("attr")`` lookups match. AWS restXml responses use a default
    namespace which ElementTree otherwise qualifies onto every tag as
    ``{ns}Tag``; prefixed attributes (e.g. ``xsi:type``) get the same
    treatment on their keys."""
    root = _fromstring(text)
    for el in root.iter():
        if el.tag.startswith("{"):
            el.tag = el.tag.rpartition("}")[2]
        if any(key.startswith("{") for key in el.attrib):
            el.attrib = {
                key.rpartition("}")[2]: value for key, value in el.attrib.items()
            }
    return root


__all__ = [
    "Element",
    "SubElement",
    "fromstring",
    "tostring",
]
