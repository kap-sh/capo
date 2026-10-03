"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessGrantsInstanceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.access_grants_instance_arn
    import capo_s3_control.types.access_grants_instance_id
    import capo_s3_control.types.creation_timestamp
    import capo_s3_control.types.identity_center_application_arn
    import capo_s3_control.types.identity_center_arn


class CreateAccessGrantsInstanceResult(TypedDict, closed=True):
    created_at: NotRequired[
        "capo_s3_control.types.creation_timestamp.CreationTimestamp"
    ]
    """<p>The date and time when you created the S3 Access Grants instance. </p>"""
    access_grants_instance_id: NotRequired[
        "capo_s3_control.types.access_grants_instance_id.AccessGrantsInstanceId"
    ]
    """<p>The ID of the S3 Access Grants instance. The ID is <code>default</code>. You can have one S3 Access Grants instance per Region per account. </p>"""
    access_grants_instance_arn: NotRequired[
        "capo_s3_control.types.access_grants_instance_arn.AccessGrantsInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services IAM Identity Center instance that you are associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate identity directory that you added to the IAM Identity Center. You can use the <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html">ListInstances</a> API operation to retrieve a list of your Identity Center instances and their ARNs.</p>"""
    identity_center_arn: NotRequired[
        "capo_s3_control.types.identity_center_arn.IdentityCenterArn"
    ]
    """<p>If you associated your S3 Access Grants instance with an Amazon Web Services IAM Identity Center instance, this field returns the Amazon Resource Name (ARN) of the IAM Identity Center instance application; a subresource of the original Identity Center instance. S3 Access Grants creates this Identity Center application for the specific S3 Access Grants instance. </p>"""
    identity_center_instance_arn: NotRequired[
        "capo_s3_control.types.identity_center_arn.IdentityCenterArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services IAM Identity Center instance that you are associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate identity directory that you added to the IAM Identity Center. You can use the <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html">ListInstances</a> API operation to retrieve a list of your Identity Center instances and their ARNs.</p>"""
    identity_center_application_arn: NotRequired[
        "capo_s3_control.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>If you associated your S3 Access Grants instance with an Amazon Web Services IAM Identity Center instance, this field returns the Amazon Resource Name (ARN) of the IAM Identity Center instance application; a subresource of the original Identity Center instance. S3 Access Grants creates this Identity Center application for the specific S3 Access Grants instance. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateAccessGrantsInstanceResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "created_at" in value:
        import capo_s3_control.types.creation_timestamp

        capo_s3_control.types.creation_timestamp.serialize_xml(
            value["created_at"], el, "CreatedAt"
        )
    if "access_grants_instance_id" in value:
        SubElement(el, "AccessGrantsInstanceId").text = str(
            value["access_grants_instance_id"]
        )
    if "access_grants_instance_arn" in value:
        SubElement(el, "AccessGrantsInstanceArn").text = str(
            value["access_grants_instance_arn"]
        )
    if "identity_center_arn" in value:
        SubElement(el, "IdentityCenterArn").text = str(value["identity_center_arn"])
    if "identity_center_instance_arn" in value:
        SubElement(el, "IdentityCenterInstanceArn").text = str(
            value["identity_center_instance_arn"]
        )
    if "identity_center_application_arn" in value:
        SubElement(el, "IdentityCenterApplicationArn").text = str(
            value["identity_center_application_arn"]
        )


def deserialize_xml(el: Element) -> CreateAccessGrantsInstanceResult:
    out: CreateAccessGrantsInstanceResult = {}  # type: ignore[typeddict-item]
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import capo_s3_control.types.creation_timestamp

        out["created_at"] = capo_s3_control.types.creation_timestamp.deserialize_xml(
            child_created_at
        )
    child_access_grants_instance_id = el.find("AccessGrantsInstanceId")
    if child_access_grants_instance_id is not None:
        out["access_grants_instance_id"] = str(
            child_access_grants_instance_id.text or ""
        )
    child_access_grants_instance_arn = el.find("AccessGrantsInstanceArn")
    if child_access_grants_instance_arn is not None:
        out["access_grants_instance_arn"] = str(
            child_access_grants_instance_arn.text or ""
        )
    child_identity_center_arn = el.find("IdentityCenterArn")
    if child_identity_center_arn is not None:
        out["identity_center_arn"] = str(child_identity_center_arn.text or "")
    child_identity_center_instance_arn = el.find("IdentityCenterInstanceArn")
    if child_identity_center_instance_arn is not None:
        out["identity_center_instance_arn"] = str(
            child_identity_center_instance_arn.text or ""
        )
    child_identity_center_application_arn = el.find("IdentityCenterApplicationArn")
    if child_identity_center_application_arn is not None:
        out["identity_center_application_arn"] = str(
            child_identity_center_application_arn.text or ""
        )
    return out
