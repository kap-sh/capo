"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.access_grants_location_configuration
    import capo_s3_control.types.access_grants_location_id
    import capo_s3_control.types.account_id
    import capo_s3_control.types.grantee
    import capo_s3_control.types.identity_center_application_arn
    import capo_s3_control.types.permission
    import capo_s3_control.types.s3_prefix_type
    import capo_s3_control.types.tag_list


class CreateAccessGrantRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    access_grants_location_id: (
        "capo_s3_control.types.access_grants_location_id.AccessGrantsLocationId"
    )
    """<p>The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p> <p>If you are passing the <code>default</code> location, you cannot create an access grant for the entire default location. You must also specify a bucket or a bucket and prefix in the <code>Subprefix</code> field. </p>"""
    access_grants_location_configuration: NotRequired[
        "capo_s3_control.types.access_grants_location_configuration.AccessGrantsLocationConfiguration"
    ]
    """<p>The configuration options of the grant location. The grant location is the S3 path to the data to which you are granting access. It contains the <code>S3SubPrefix</code> field. The grant scope is the result of appending the subprefix to the location scope of the registered location.</p>"""
    grantee: "capo_s3_control.types.grantee.Grantee"
    """<p>The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added your corporate directory to Amazon Web Services IAM Identity Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee can also be a corporate directory user or group.</p>"""
    permission: "capo_s3_control.types.permission.Permission"
    """<p>The type of access that you are granting to your S3 data, which can be set to one of the following values:</p> <ul> <li> <p> <code>READ</code> – Grant read-only access to the S3 data.</p> </li> <li> <p> <code>WRITE</code> – Grant write-only access to the S3 data.</p> </li> <li> <p> <code>READWRITE</code> – Grant both read and write access to the S3 data.</p> </li> </ul>"""
    application_arn: NotRequired[
        "capo_s3_control.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services IAM Identity Center application associated with your Identity Center instance. If an application ARN is included in the request to create an access grant, the grantee can only access the S3 data through this application. </p>"""
    s3_prefix_type: NotRequired["capo_s3_control.types.s3_prefix_type.S3PrefixType"]
    """<p>The type of <code>S3SubPrefix</code>. The only possible value is <code>Object</code>. Pass this value if the access grant scope is an object. Do not pass this value if the access grant scope is a bucket or a bucket and a prefix. </p>"""
    tags: NotRequired["capo_s3_control.types.tag_list.TagList"]
    """<p>The Amazon Web Services resource tags that you are adding to the access grant. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateAccessGrantRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "AccessGrantsLocationId").text = str(
        value["access_grants_location_id"]
    )
    if "access_grants_location_configuration" in value:
        import capo_s3_control.types.access_grants_location_configuration

        capo_s3_control.types.access_grants_location_configuration.serialize_xml(
            value["access_grants_location_configuration"],
            el,
            "AccessGrantsLocationConfiguration",
        )
    import capo_s3_control.types.grantee

    capo_s3_control.types.grantee.serialize_xml(value["grantee"], el, "Grantee")
    import capo_s3_control.types.permission

    capo_s3_control.types.permission.serialize_xml(
        value["permission"], el, "Permission"
    )
    if "application_arn" in value:
        SubElement(el, "ApplicationArn").text = str(value["application_arn"])
    if "s3_prefix_type" in value:
        import capo_s3_control.types.s3_prefix_type

        capo_s3_control.types.s3_prefix_type.serialize_xml(
            value["s3_prefix_type"], el, "S3PrefixType"
        )
    if "tags" in value:
        import capo_s3_control.types.tag_list

        capo_s3_control.types.tag_list.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateAccessGrantRequest:
    out: CreateAccessGrantRequest = {}  # type: ignore[typeddict-item]
    child_access_grants_location_id = el.find("AccessGrantsLocationId")
    if child_access_grants_location_id is not None:
        out["access_grants_location_id"] = str(
            child_access_grants_location_id.text or ""
        )
    else:
        out["access_grants_location_id"] = ""
    child_access_grants_location_configuration = el.find(
        "AccessGrantsLocationConfiguration"
    )
    if child_access_grants_location_configuration is not None:
        import capo_s3_control.types.access_grants_location_configuration

        out["access_grants_location_configuration"] = (
            capo_s3_control.types.access_grants_location_configuration.deserialize_xml(
                child_access_grants_location_configuration
            )
        )
    child_grantee = el.find("Grantee")
    if child_grantee is not None:
        import capo_s3_control.types.grantee

        out["grantee"] = capo_s3_control.types.grantee.deserialize_xml(child_grantee)
    else:
        raise DeserializationError("CreateAccessGrantRequest.grantee required")
    child_permission = el.find("Permission")
    if child_permission is not None:
        import capo_s3_control.types.permission

        out["permission"] = capo_s3_control.types.permission.deserialize_xml(
            child_permission
        )
    else:
        import typing

        out["permission"] = typing.cast(
            "capo_s3_control.types.permission.Permission", ""
        )
    child_application_arn = el.find("ApplicationArn")
    if child_application_arn is not None:
        out["application_arn"] = str(child_application_arn.text or "")
    child_s3_prefix_type = el.find("S3PrefixType")
    if child_s3_prefix_type is not None:
        import capo_s3_control.types.s3_prefix_type

        out["s3_prefix_type"] = capo_s3_control.types.s3_prefix_type.deserialize_xml(
            child_s3_prefix_type
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.tag_list

        out["tags"] = capo_s3_control.types.tag_list.deserialize_xml(child_tags)
    return out
