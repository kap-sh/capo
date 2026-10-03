"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessGrantsInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.identity_center_arn
    import capo_s3_control.types.tag_list


class CreateAccessGrantsInstanceRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    identity_center_arn: NotRequired[
        "capo_s3_control.types.identity_center_arn.IdentityCenterArn"
    ]
    """<p>If you would like to associate your S3 Access Grants instance with an Amazon Web Services IAM Identity Center instance, use this field to pass the Amazon Resource Name (ARN) of the Amazon Web Services IAM Identity Center instance that you are associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate identity directory that you added to the IAM Identity Center. You can use the <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html">ListInstances</a> API operation to retrieve a list of your Identity Center instances and their ARNs. </p>"""
    tags: NotRequired["capo_s3_control.types.tag_list.TagList"]
    """<p>The Amazon Web Services resource tags that you are adding to the S3 Access Grants instance. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateAccessGrantsInstanceRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "identity_center_arn" in value:
        SubElement(el, "IdentityCenterArn").text = str(value["identity_center_arn"])
    if "tags" in value:
        import capo_s3_control.types.tag_list

        capo_s3_control.types.tag_list.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateAccessGrantsInstanceRequest:
    out: CreateAccessGrantsInstanceRequest = {}  # type: ignore[typeddict-item]
    child_identity_center_arn = el.find("IdentityCenterArn")
    if child_identity_center_arn is not None:
        out["identity_center_arn"] = str(child_identity_center_arn.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.tag_list

        out["tags"] = capo_s3_control.types.tag_list.deserialize_xml(child_tags)
    return out
