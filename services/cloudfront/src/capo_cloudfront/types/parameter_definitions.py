"""Generated from Smithy shape ``com.amazonaws.cloudfront#ParameterDefinitions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.parameter_definition

ParameterDefinitions: TypeAlias = list[
    "capo_cloudfront.types.parameter_definition.ParameterDefinition"
]


# --- restXml ser/de ---
def serialize_xml(value: ParameterDefinitions, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.parameter_definition

        capo_cloudfront.types.parameter_definition.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> ParameterDefinitions:
    import capo_cloudfront.types.parameter_definition

    out: ParameterDefinitions = []
    for child in el.findall("member"):
        out.append(capo_cloudfront.types.parameter_definition.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ParameterDefinitions, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.parameter_definition

        capo_cloudfront.types.parameter_definition.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ParameterDefinitions:
    import capo_cloudfront.types.parameter_definition

    out: ParameterDefinitions = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.parameter_definition.deserialize_xml(child))
    return out


def redact_sensitive(value: ParameterDefinitions) -> list[Any]:
    import capo_cloudfront.types.parameter_definition

    return [
        capo_cloudfront.types.parameter_definition.redact_sensitive(item)
        for item in value
    ]
