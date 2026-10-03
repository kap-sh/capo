"""Generated from Smithy shape ``com.amazonaws.s3#RequestPayer``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

"""<p>Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html">Downloading Objects in Requester Pays Buckets</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
RequestPayer: TypeAlias = Literal["requester",]


# --- restXml ser/de ---
def to_xml_text(value: RequestPayer) -> str:
    return value


def from_xml_text(text: str) -> RequestPayer:
    return cast(RequestPayer, text)


def serialize_xml(value: RequestPayer, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> RequestPayer:
    return from_xml_text(el.text or "")
