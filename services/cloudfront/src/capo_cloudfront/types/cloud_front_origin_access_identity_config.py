"""Generated from Smithy shape ``com.amazonaws.cloudfront#CloudFrontOriginAccessIdentityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class CloudFrontOriginAccessIdentityConfig(TypedDict, closed=True):
    caller_reference: "capo_cloudfront.types.string.string"
    """<p>A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.</p> <p>If the value of <code>CallerReference</code> is new (regardless of the content of the <code>CloudFrontOriginAccessIdentityConfig</code> object), a new origin access identity is created.</p> <p>If the <code>CallerReference</code> is a value already sent in a previous identity request, and the content of the <code>CloudFrontOriginAccessIdentityConfig</code> is identical to the original request (ignoring white space), the response includes the same information returned to the original request.</p> <p>If the <code>CallerReference</code> is a value you already sent in a previous request to create an identity, but the content of the <code>CloudFrontOriginAccessIdentityConfig</code> is different from the original request, CloudFront returns a <code>CloudFrontOriginAccessIdentityAlreadyExists</code> error. </p>"""
    comment: "capo_cloudfront.types.string.string"
    """<p>A comment to describe the origin access identity. The comment cannot be longer than 128 characters.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CloudFrontOriginAccessIdentityConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> CloudFrontOriginAccessIdentityConfig:
    out: CloudFrontOriginAccessIdentityConfig = {}  # type: ignore[typeddict-item]
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        out["caller_reference"] = ""
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        out["comment"] = ""
    return out
