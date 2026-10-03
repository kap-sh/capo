"""Generated from Smithy shape ``com.amazonaws.s3#EncodingType``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

"""<p>Encoding type used by Amazon S3 to encode the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html">object keys</a> in the response. Responses are encoded only in UTF-8. An object key can contain any Unicode character. However, the XML 1.0 parser can't parse certain characters, such as characters with an ASCII value from 0 to 10. For characters that aren't supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response. For more information about characters to avoid in object key names, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-guidelines">Object key naming guidelines</a>.</p> <note> <p>When using the URL encoding type, non-ASCII characters that are used in an object's key name will be percent-encoded according to UTF-8 code values. For example, the object <code>test_file(3).png</code> will appear as <code>test_file%283%29.png</code>.</p> </note>"""
EncodingType: TypeAlias = Literal["url",]


# --- restXml ser/de ---
def to_xml_text(value: EncodingType) -> str:
    return value


def from_xml_text(text: str) -> EncodingType:
    return cast(EncodingType, text)


def serialize_xml(value: EncodingType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> EncodingType:
    return from_xml_text(el.text or "")
