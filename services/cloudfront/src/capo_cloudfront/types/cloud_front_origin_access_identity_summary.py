"""Generated from Smithy shape ``com.amazonaws.cloudfront#CloudFrontOriginAccessIdentitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class CloudFrontOriginAccessIdentitySummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The ID for the origin access identity. For example: <code>E74FTE3AJFJ256A</code>.</p>"""
    s3_canonical_user_id: "capo_cloudfront.types.string.string"
    """<p>The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.</p>"""
    comment: "capo_cloudfront.types.string.string"
    """<p>The comment for this origin access identity, as originally specified when created.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CloudFrontOriginAccessIdentitySummary, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "S3CanonicalUserId").text = str(value["s3_canonical_user_id"])
    SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> CloudFrontOriginAccessIdentitySummary:
    out: CloudFrontOriginAccessIdentitySummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_s3_canonical_user_id = el.find("S3CanonicalUserId")
    if child_s3_canonical_user_id is not None:
        out["s3_canonical_user_id"] = str(child_s3_canonical_user_id.text or "")
    else:
        out["s3_canonical_user_id"] = ""
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        out["comment"] = ""
    return out
