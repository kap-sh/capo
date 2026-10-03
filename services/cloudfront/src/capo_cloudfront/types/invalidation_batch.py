"""Generated from Smithy shape ``com.amazonaws.cloudfront#InvalidationBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.paths
    import capo_cloudfront.types.string


class InvalidationBatch(TypedDict, closed=True):
    paths: "capo_cloudfront.types.paths.Paths"
    """<p>A complex type that contains information about the objects that you want to invalidate. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects">Specifying the Objects to Invalidate</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    caller_reference: "capo_cloudfront.types.string.string"
    """<p>A value that you specify to uniquely identify an invalidation request. CloudFront uses the value to prevent you from accidentally resubmitting an identical request. Whenever you create a new invalidation request, you must specify a new value for <code>CallerReference</code> and change other values in the request as applicable. One way to ensure that the value of <code>CallerReference</code> is unique is to use a <code>timestamp</code>, for example, <code>20120301090000</code>.</p> <p>If you make a second invalidation request with the same value for <code>CallerReference</code>, and if the rest of the request is the same, CloudFront doesn't create a new invalidation request. Instead, CloudFront returns information about the invalidation request that you previously created with the same <code>CallerReference</code>.</p> <p>If <code>CallerReference</code> is a value you already sent in a previous invalidation batch request but the content of any <code>Path</code> is different from the original request, CloudFront returns an <code>InvalidationBatchAlreadyExists</code> error.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InvalidationBatch, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.paths

    capo_cloudfront.types.paths.serialize_xml(value["paths"], el, "Paths")
    SubElement(el, "CallerReference").text = str(value["caller_reference"])


def deserialize_xml(el: Element) -> InvalidationBatch:
    out: InvalidationBatch = {}  # type: ignore[typeddict-item]
    child_paths = el.find("Paths")
    if child_paths is not None:
        import capo_cloudfront.types.paths

        out["paths"] = capo_cloudfront.types.paths.deserialize_xml(child_paths)
    else:
        raise DeserializationError("InvalidationBatch.paths required")
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        raise DeserializationError("InvalidationBatch.caller_reference required")
    return out
