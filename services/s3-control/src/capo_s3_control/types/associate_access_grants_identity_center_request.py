"""Generated from Smithy shape ``com.amazonaws.s3control#AssociateAccessGrantsIdentityCenterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.identity_center_arn


class AssociateAccessGrantsIdentityCenterRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    identity_center_arn: "capo_s3_control.types.identity_center_arn.IdentityCenterArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services IAM Identity Center instance that you are associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate identity directory that you added to the IAM Identity Center. You can use the <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html">ListInstances</a> API operation to retrieve a list of your Identity Center instances and their ARNs.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AssociateAccessGrantsIdentityCenterRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "IdentityCenterArn").text = str(value["identity_center_arn"])


def deserialize_xml(el: Element) -> AssociateAccessGrantsIdentityCenterRequest:
    out: AssociateAccessGrantsIdentityCenterRequest = {}  # type: ignore[typeddict-item]
    child_identity_center_arn = el.find("IdentityCenterArn")
    if child_identity_center_arn is not None:
        out["identity_center_arn"] = str(child_identity_center_arn.text or "")
    else:
        raise DeserializationError(
            "AssociateAccessGrantsIdentityCenterRequest.identity_center_arn required"
        )
    return out
