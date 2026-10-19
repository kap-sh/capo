"""Generated from Smithy shape ``com.amazonaws.cloudfront#EncryptionEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.field_patterns
    import capo_cloudfront.types.string


class EncryptionEntity(TypedDict, closed=True):
    public_key_id: "capo_cloudfront.types.string.string"
    """<p>The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.</p>"""
    provider_id: "capo_cloudfront.types.string.string"
    """<p>The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.</p>"""
    field_patterns: "capo_cloudfront.types.field_patterns.FieldPatterns"
    """<p>Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can't overlap field patterns. For example, you can't have both ABC* and AB*. Note that field patterns are case-sensitive.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: EncryptionEntity, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "PublicKeyId").text = str(value["public_key_id"])
    SubElement(el, "ProviderId").text = str(value["provider_id"])
    import capo_cloudfront.types.field_patterns

    capo_cloudfront.types.field_patterns.serialize_xml(
        value["field_patterns"], el, "FieldPatterns"
    )


def deserialize_xml(el: Element) -> EncryptionEntity:
    out: EncryptionEntity = {}  # type: ignore[typeddict-item]
    child_public_key_id = el.find("PublicKeyId")
    if child_public_key_id is not None:
        out["public_key_id"] = str(child_public_key_id.text or "")
    else:
        out["public_key_id"] = ""
    child_provider_id = el.find("ProviderId")
    if child_provider_id is not None:
        out["provider_id"] = str(child_provider_id.text or "")
    else:
        out["provider_id"] = ""
    child_field_patterns = el.find("FieldPatterns")
    if child_field_patterns is not None:
        import capo_cloudfront.types.field_patterns

        out["field_patterns"] = capo_cloudfront.types.field_patterns.deserialize_xml(
            child_field_patterns
        )
    else:
        raise DeserializationError("EncryptionEntity.field_patterns required")
    return out
