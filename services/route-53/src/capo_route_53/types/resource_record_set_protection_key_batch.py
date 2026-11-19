"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecordSetProtectionKeyBatch``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_record_set_protection_key

ResourceRecordSetProtectionKeyBatch: TypeAlias = list[
    "capo_route_53.types.resource_record_set_protection_key.ResourceRecordSetProtectionKey"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ResourceRecordSetProtectionKeyBatch, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.resource_record_set_protection_key

        capo_route_53.types.resource_record_set_protection_key.serialize_xml(
            item, el, "ResourceRecordSetProtectionKey"
        )


def deserialize_xml(el: Element) -> ResourceRecordSetProtectionKeyBatch:
    import capo_route_53.types.resource_record_set_protection_key

    out: ResourceRecordSetProtectionKeyBatch = []
    for child in el.findall("ResourceRecordSetProtectionKey"):
        out.append(
            capo_route_53.types.resource_record_set_protection_key.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: ResourceRecordSetProtectionKeyBatch, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.resource_record_set_protection_key

        capo_route_53.types.resource_record_set_protection_key.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> ResourceRecordSetProtectionKeyBatch:
    import capo_route_53.types.resource_record_set_protection_key

    out: ResourceRecordSetProtectionKeyBatch = []
    for child in parent.findall(tag):
        out.append(
            capo_route_53.types.resource_record_set_protection_key.deserialize_xml(
                child
            )
        )
    return out
