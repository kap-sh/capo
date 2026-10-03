"""Generated from Smithy shape ``com.amazonaws.s3#IndexDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.suffix


class IndexDocument(TypedDict, closed=True):
    suffix: "capo_s3.types.suffix.Suffix"
    """<p>A suffix that is appended to a request that is for a directory on the website endpoint. (For example, if the suffix is <code>index.html</code> and you make a request to <code>samplebucket/images/</code>, the data that is returned will be for the object with the key name <code>images/index.html</code>.) The suffix must not be empty and must not include a slash character.</p> <important> <p>Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints"> XML related object key constraints</a>.</p> </important>"""


# --- restXml ser/de ---
def serialize_xml(value: IndexDocument, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Suffix").text = str(value["suffix"])


def deserialize_xml(el: Element) -> IndexDocument:
    out: IndexDocument = {}  # type: ignore[typeddict-item]
    child_suffix = el.find("Suffix")
    if child_suffix is not None:
        out["suffix"] = str(child_suffix.text or "")
    else:
        raise DeserializationError("IndexDocument.suffix required")
    return out
