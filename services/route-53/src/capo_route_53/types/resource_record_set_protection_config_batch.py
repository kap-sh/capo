"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecordSetProtectionConfigBatch``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_record_set_protection_config

ResourceRecordSetProtectionConfigBatch: TypeAlias = list[
    "capo_route_53.types.resource_record_set_protection_config.ResourceRecordSetProtectionConfig"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ResourceRecordSetProtectionConfigBatch, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.resource_record_set_protection_config

        capo_route_53.types.resource_record_set_protection_config.serialize_xml(
            item, el, "ResourceRecordSetProtectionConfig"
        )


def deserialize_xml(el: Element) -> ResourceRecordSetProtectionConfigBatch:
    import capo_route_53.types.resource_record_set_protection_config

    out: ResourceRecordSetProtectionConfigBatch = []
    for child in el.findall("ResourceRecordSetProtectionConfig"):
        out.append(
            capo_route_53.types.resource_record_set_protection_config.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: ResourceRecordSetProtectionConfigBatch, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.resource_record_set_protection_config

        capo_route_53.types.resource_record_set_protection_config.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> ResourceRecordSetProtectionConfigBatch:
    import capo_route_53.types.resource_record_set_protection_config

    out: ResourceRecordSetProtectionConfigBatch = []
    for child in parent.findall(tag):
        out.append(
            capo_route_53.types.resource_record_set_protection_config.deserialize_xml(
                child
            )
        )
    return out
