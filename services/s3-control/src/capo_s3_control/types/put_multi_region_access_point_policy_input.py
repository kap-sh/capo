"""Generated from Smithy shape ``com.amazonaws.s3control#PutMultiRegionAccessPointPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.multi_region_access_point_name
    import capo_s3_control.types.policy


class PutMultiRegionAccessPointPolicyInput(TypedDict, closed=True):
    name: "capo_s3_control.types.multi_region_access_point_name.MultiRegionAccessPointName"
    """<p>The name of the Multi-Region Access Point associated with the request.</p>"""
    policy: "capo_s3_control.types.policy.Policy"
    """<p>The policy details for the <code>PutMultiRegionAccessPoint</code> request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutMultiRegionAccessPointPolicyInput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Policy").text = str(value["policy"])


def deserialize_xml(el: Element) -> PutMultiRegionAccessPointPolicyInput:
    out: PutMultiRegionAccessPointPolicyInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    else:
        out["policy"] = ""
    return out
