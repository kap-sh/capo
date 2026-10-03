"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublicKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.public_key_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class PublicKey(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier of the public key.</p>"""
    created_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the public key was uploaded.</p>"""
    public_key_config: "capo_cloudfront.types.public_key_config.PublicKeyConfig"
    """<p>Configuration information about a public key that you can use with <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">signed URLs and signed cookies</a>, or with <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html">field-level encryption</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PublicKey, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["created_time"], el, "CreatedTime"
    )
    import capo_cloudfront.types.public_key_config

    capo_cloudfront.types.public_key_config.serialize_xml(
        value["public_key_config"], el, "PublicKeyConfig"
    )


def deserialize_xml(el: Element) -> PublicKey:
    out: PublicKey = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("PublicKey.id required")
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_cloudfront.types.timestamp

        out["created_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    else:
        raise DeserializationError("PublicKey.created_time required")
    child_public_key_config = el.find("PublicKeyConfig")
    if child_public_key_config is not None:
        import capo_cloudfront.types.public_key_config

        out["public_key_config"] = (
            capo_cloudfront.types.public_key_config.deserialize_xml(
                child_public_key_config
            )
        )
    else:
        raise DeserializationError("PublicKey.public_key_config required")
    return out
