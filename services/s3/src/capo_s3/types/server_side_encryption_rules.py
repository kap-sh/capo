"""Generated from Smithy shape ``com.amazonaws.s3#ServerSideEncryptionRules``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.server_side_encryption_rule

ServerSideEncryptionRules: TypeAlias = list[
    "capo_s3.types.server_side_encryption_rule.ServerSideEncryptionRule"
]


# --- restXml ser/de ---
def serialize_xml(value: ServerSideEncryptionRules, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.server_side_encryption_rule

        capo_s3.types.server_side_encryption_rule.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> ServerSideEncryptionRules:
    import capo_s3.types.server_side_encryption_rule

    out: ServerSideEncryptionRules = []
    for child in el.findall("member"):
        out.append(capo_s3.types.server_side_encryption_rule.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: ServerSideEncryptionRules, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3.types.server_side_encryption_rule

        capo_s3.types.server_side_encryption_rule.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ServerSideEncryptionRules:
    import capo_s3.types.server_side_encryption_rule

    out: ServerSideEncryptionRules = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.server_side_encryption_rule.deserialize_xml(child))
    return out


def redact_sensitive(value: ServerSideEncryptionRules) -> list[Any]:
    import capo_s3.types.server_side_encryption_rule

    return [
        capo_s3.types.server_side_encryption_rule.redact_sensitive(item)
        for item in value
    ]
