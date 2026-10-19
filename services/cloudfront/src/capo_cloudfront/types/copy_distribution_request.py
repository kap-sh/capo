"""Generated from Smithy shape ``com.amazonaws.cloudfront#CopyDistributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.string


class CopyDistributionRequest(TypedDict, closed=True):
    primary_distribution_id: "capo_cloudfront.types.string.string"
    """<p>The identifier of the primary distribution whose configuration you are copying. To get a distribution ID, use <code>ListDistributions</code>.</p>"""
    staging: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>The type of distribution that your primary distribution will be copied to. The only valid value is <code>True</code>, indicating that you are copying to a staging distribution.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The version identifier of the primary distribution whose configuration you are copying. This is the <code>ETag</code> value returned in the response to <code>GetDistribution</code> and <code>GetDistributionConfig</code>.</p>"""
    caller_reference: "capo_cloudfront.types.string.string"
    """<p>A value that uniquely identifies a request to create a resource. This helps to prevent CloudFront from creating a duplicate resource if you accidentally resubmit an identical request.</p>"""
    enabled: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>A Boolean flag to specify the state of the staging distribution when it's created. When you set this value to <code>True</code>, the staging distribution is enabled. When you set this value to <code>False</code>, the staging distribution is disabled.</p> <p>If you omit this field, the default value is <code>True</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CopyDistributionRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    if "enabled" in value:
        SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"


def deserialize_xml(el: Element) -> CopyDistributionRequest:
    out: CopyDistributionRequest = {}  # type: ignore[typeddict-item]
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        out["caller_reference"] = ""
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
