"""Generated from Smithy shape ``com.amazonaws.s3control#PutAccessGrantsInstanceResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.organization
    import capo_s3_control.types.policy_document


class PutAccessGrantsInstanceResourcePolicyRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    policy: "capo_s3_control.types.policy_document.PolicyDocument"
    """<p>The resource policy of the S3 Access Grants instance that you are updating.</p>"""
    organization: NotRequired["capo_s3_control.types.organization.Organization"]
    """<p>The Organization of the resource policy of the S3 Access Grants instance.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutAccessGrantsInstanceResourcePolicyRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Policy").text = str(value["policy"])
    if "organization" in value:
        SubElement(el, "Organization").text = str(value["organization"])


def deserialize_xml(el: Element) -> PutAccessGrantsInstanceResourcePolicyRequest:
    out: PutAccessGrantsInstanceResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    else:
        out["policy"] = ""
    child_organization = el.find("Organization")
    if child_organization is not None:
        out["organization"] = str(child_organization.text or "")
    return out
