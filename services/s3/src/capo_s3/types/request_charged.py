"""Generated from Smithy shape ``com.amazonaws.s3#RequestCharged``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

"""<p>If present, indicates that the requester was successfully charged for the request. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html">Using Requester Pays buckets for storage transfers and usage</a> in the <i>Amazon Simple Storage Service user guide</i>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
RequestCharged: TypeAlias = Literal["requester",]


# --- restXml ser/de ---
def to_xml_text(value: RequestCharged) -> str:
    return value


def from_xml_text(text: str) -> RequestCharged:
    return cast(RequestCharged, text)


def serialize_xml(value: RequestCharged, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> RequestCharged:
    return from_xml_text(el.text or "")
