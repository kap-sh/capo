"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublicKeyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class PublicKeyConfig(TypedDict, closed=True):
    caller_reference: "capo_cloudfront.types.string.string"
    """<p>A string included in the request to help make sure that the request can't be replayed.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>A name to help identify the public key.</p>"""
    encoded_key: "capo_cloudfront.types.string.string"
    """<p>The public key that you can use with <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">signed URLs and signed cookies</a>, or with <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html">field-level encryption</a>.</p>"""
    comment: NotRequired["capo_cloudfront.types.string.string"]
    """<p>A comment to describe the public key. The comment cannot be longer than 128 characters.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PublicKeyConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "EncodedKey").text = str(value["encoded_key"])
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> PublicKeyConfig:
    out: PublicKeyConfig = {}  # type: ignore[typeddict-item]
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        raise DeserializationError("PublicKeyConfig.caller_reference required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("PublicKeyConfig.name required")
    child_encoded_key = el.find("EncodedKey")
    if child_encoded_key is not None:
        out["encoded_key"] = str(child_encoded_key.text or "")
    else:
        raise DeserializationError("PublicKeyConfig.encoded_key required")
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
