"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryptionProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.encryption_entities
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class FieldLevelEncryptionProfileSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>ID for the field-level encryption profile summary.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The time when the field-level encryption profile summary was last updated.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>Name for the field-level encryption profile summary.</p>"""
    encryption_entities: "capo_cloudfront.types.encryption_entities.EncryptionEntities"
    """<p>A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.</p>"""
    comment: NotRequired["capo_cloudfront.types.string.string"]
    """<p>An optional comment for the field-level encryption profile summary. The comment cannot be longer than 128 characters.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: FieldLevelEncryptionProfileSummary, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    SubElement(el, "Name").text = str(value["name"])
    import capo_cloudfront.types.encryption_entities

    capo_cloudfront.types.encryption_entities.serialize_xml(
        value["encryption_entities"], el, "EncryptionEntities"
    )
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> FieldLevelEncryptionProfileSummary:
    out: FieldLevelEncryptionProfileSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
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
            "FieldLevelEncryptionProfileSummary.encryption_entities required"
        )
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
