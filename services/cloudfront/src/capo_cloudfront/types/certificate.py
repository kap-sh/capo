"""Generated from Smithy shape ``com.amazonaws.cloudfront#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class Certificate(TypedDict, closed=True):
    arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the ACM certificate.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Certificate, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Arn").text = str(value["arn"])


def deserialize_xml(el: Element) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        out["arn"] = ""
    return out
