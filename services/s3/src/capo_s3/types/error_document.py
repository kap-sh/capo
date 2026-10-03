"""Generated from Smithy shape ``com.amazonaws.s3#ErrorDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.object_key


class ErrorDocument(TypedDict, closed=True):
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>The object key name to use when a 4XX class error occurs.</p> <important> <p>Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints"> XML related object key constraints</a>.</p> </important>"""


# --- restXml ser/de ---
def serialize_xml(value: ErrorDocument, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Key").text = str(value["key"])


def deserialize_xml(el: Element) -> ErrorDocument:
    out: ErrorDocument = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    else:
        raise DeserializationError("ErrorDocument.key required")
    return out
