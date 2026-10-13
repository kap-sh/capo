"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginCustomHeadersList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_custom_header

OriginCustomHeadersList: TypeAlias = list[
    "capo_cloudfront.types.origin_custom_header.OriginCustomHeader"
]


# --- restXml ser/de ---
def serialize_xml(value: OriginCustomHeadersList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.origin_custom_header

        capo_cloudfront.types.origin_custom_header.serialize_xml(
            item, el, "OriginCustomHeader"
        )


def deserialize_xml(el: Element) -> OriginCustomHeadersList:
    import capo_cloudfront.types.origin_custom_header

    out: OriginCustomHeadersList = []
    for child in el.findall("OriginCustomHeader"):
        out.append(capo_cloudfront.types.origin_custom_header.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: OriginCustomHeadersList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.origin_custom_header

        capo_cloudfront.types.origin_custom_header.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> OriginCustomHeadersList:
    import capo_cloudfront.types.origin_custom_header

    out: OriginCustomHeadersList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.origin_custom_header.deserialize_xml(child))
    return out


def redact_sensitive(value: OriginCustomHeadersList) -> list[Any]:
    import capo_cloudfront.types.origin_custom_header

    return [
        capo_cloudfront.types.origin_custom_header.redact_sensitive(item)
        for item in value
    ]
