"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublicKeySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class PublicKeySummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier of the public key.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>A name to help identify the public key.</p>"""
    created_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the public key was uploaded.</p>"""
    encoded_key: "capo_cloudfront.types.string.string"
    """<p>The public key.</p>"""
    comment: NotRequired["capo_cloudfront.types.string.string"]
    """<p>A comment to describe the public key. The comment cannot be longer than 128 characters.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PublicKeySummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Name").text = str(value["name"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["created_time"], el, "CreatedTime"
    )
    SubElement(el, "EncodedKey").text = str(value["encoded_key"])
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> PublicKeySummary:
    out: PublicKeySummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_cloudfront.types.timestamp

        out["created_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_encoded_key = el.find("EncodedKey")
    if child_encoded_key is not None:
        out["encoded_key"] = str(child_encoded_key.text or "")
    else:
        out["encoded_key"] = ""
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
