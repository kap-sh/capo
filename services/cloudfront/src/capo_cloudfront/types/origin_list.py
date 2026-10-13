"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin

OriginList: TypeAlias = list["capo_cloudfront.types.origin.Origin"]


# --- restXml ser/de ---
def serialize_xml(value: OriginList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.origin

        capo_cloudfront.types.origin.serialize_xml(item, el, "Origin")


def deserialize_xml(el: Element) -> OriginList:
    import capo_cloudfront.types.origin

    out: OriginList = []
    for child in el.findall("Origin"):
        out.append(capo_cloudfront.types.origin.deserialize_xml(child))
    return out


def serialize_xml_flat(value: OriginList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.origin

        capo_cloudfront.types.origin.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> OriginList:
    import capo_cloudfront.types.origin

    out: OriginList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.origin.deserialize_xml(child))
    return out


def redact_sensitive(value: OriginList) -> list[Any]:
    import capo_cloudfront.types.origin

    return [capo_cloudfront.types.origin.redact_sensitive(item) for item in value]
