"""Generated from Smithy shape ``com.amazonaws.cloudfront#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the CloudFront resource for which the policy is being created.</p>"""
    policy_document: "capo_cloudfront.types.string.string"
    """<p>The JSON-formatted resource policy to create.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutResourcePolicyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ResourceArn").text = str(value["resource_arn"])
    SubElement(el, "PolicyDocument").text = str(value["policy_document"])


def deserialize_xml(el: Element) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        out["resource_arn"] = ""
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    else:
        out["policy_document"] = ""
    return out
