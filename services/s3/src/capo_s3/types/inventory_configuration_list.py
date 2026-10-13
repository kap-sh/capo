"""Generated from Smithy shape ``com.amazonaws.s3#InventoryConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.inventory_configuration

InventoryConfigurationList: TypeAlias = list[
    "capo_s3.types.inventory_configuration.InventoryConfiguration"
]


# --- restXml ser/de ---
def serialize_xml(value: InventoryConfigurationList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.inventory_configuration

        capo_s3.types.inventory_configuration.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> InventoryConfigurationList:
    import capo_s3.types.inventory_configuration

    out: InventoryConfigurationList = []
    for child in el.findall("member"):
        out.append(capo_s3.types.inventory_configuration.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: InventoryConfigurationList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3.types.inventory_configuration

        capo_s3.types.inventory_configuration.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> InventoryConfigurationList:
    import capo_s3.types.inventory_configuration

    out: InventoryConfigurationList = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.inventory_configuration.deserialize_xml(child))
    return out


def redact_sensitive(value: InventoryConfigurationList) -> list[Any]:
    import capo_s3.types.inventory_configuration

    return [
        capo_s3.types.inventory_configuration.redact_sensitive(item) for item in value
    ]
