"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryptionProfileConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.encryption_entities
    import capo_cloudfront.types.string


class FieldLevelEncryptionProfileConfig(TypedDict, closed=True):
    name: "capo_cloudfront.types.string.string"
    """<p>Profile name for the field-level encryption profile.</p>"""
    caller_reference: "capo_cloudfront.types.string.string"
    """<p>A unique number that ensures that the request can't be replayed.</p>"""
    comment: NotRequired["capo_cloudfront.types.string.string"]
    """<p>An optional comment for the field-level encryption profile. The comment cannot be longer than 128 characters.</p>"""
    encryption_entities: "capo_cloudfront.types.encryption_entities.EncryptionEntities"
    """<p>A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: FieldLevelEncryptionProfileConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    import capo_cloudfront.types.encryption_entities

    capo_cloudfront.types.encryption_entities.serialize_xml(
        value["encryption_entities"], el, "EncryptionEntities"
    )


def deserialize_xml(el: Element) -> FieldLevelEncryptionProfileConfig:
    out: FieldLevelEncryptionProfileConfig = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        out["caller_reference"] = ""
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_encryption_entities = el.find("EncryptionEntities")
    if child_encryption_entities is not None:
        import capo_cloudfront.types.encryption_entities

        out["encryption_entities"] = (
            capo_cloudfront.types.encryption_entities.deserialize_xml(
                child_encryption_entities
            )
        )
    else:
        raise DeserializationError(
            "FieldLevelEncryptionProfileConfig.encryption_entities required"
        )
    return out
