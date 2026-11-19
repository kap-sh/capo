"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecordSetProtections``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_record_set_protection

ResourceRecordSetProtections: TypeAlias = list[
    "capo_route_53.types.resource_record_set_protection.ResourceRecordSetProtection"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ResourceRecordSetProtections, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.resource_record_set_protection

        capo_route_53.types.resource_record_set_protection.serialize_xml(
            item, el, "ResourceRecordSetProtection"
        )


def deserialize_xml(el: Element) -> ResourceRecordSetProtections:
    import capo_route_53.types.resource_record_set_protection

    out: ResourceRecordSetProtections = []
    for child in el.findall("ResourceRecordSetProtection"):
        out.append(
            capo_route_53.types.resource_record_set_protection.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: ResourceRecordSetProtections, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.resource_record_set_protection

        capo_route_53.types.resource_record_set_protection.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> ResourceRecordSetProtections:
    import capo_route_53.types.resource_record_set_protection

    out: ResourceRecordSetProtections = []
    for child in parent.findall(tag):
        out.append(
            capo_route_53.types.resource_record_set_protection.deserialize_xml(child)
        )
    return out
