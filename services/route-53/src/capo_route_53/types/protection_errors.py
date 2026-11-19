"""Generated from Smithy shape ``com.amazonaws.route53#ProtectionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.protection_error

ProtectionErrors: TypeAlias = list[
    "capo_route_53.types.protection_error.ProtectionError"
]


# --- restXml ser/de ---
def serialize_xml(value: ProtectionErrors, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.protection_error

        capo_route_53.types.protection_error.serialize_xml(item, el, "ProtectionError")


def deserialize_xml(el: Element) -> ProtectionErrors:
    import capo_route_53.types.protection_error

    out: ProtectionErrors = []
    for child in el.findall("ProtectionError"):
        out.append(capo_route_53.types.protection_error.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ProtectionErrors, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.protection_error

        capo_route_53.types.protection_error.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ProtectionErrors:
    import capo_route_53.types.protection_error

    out: ProtectionErrors = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.protection_error.deserialize_xml(child))
    return out
