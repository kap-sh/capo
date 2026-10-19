"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the CloudFront resource that is associated with the resource policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetResourcePolicyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ResourceArn").text = str(value["resource_arn"])


def deserialize_xml(el: Element) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        out["resource_arn"] = ""
    return out
