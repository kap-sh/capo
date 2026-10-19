"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessGrantsLocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.iam_role_arn
    import capo_s3_control.types.s3_prefix
    import capo_s3_control.types.tag_list


class CreateAccessGrantsLocationRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    location_scope: "capo_s3_control.types.s3_prefix.S3Prefix"
    """<p>The S3 path to the location that you are registering. The location scope can be the default S3 location <code>s3://</code>, the S3 path to a bucket <code>s3://<bucket></code>, or the S3 path to a bucket and prefix <code>s3://<bucket>/<prefix></code>. A prefix in S3 is a string of characters at the beginning of an object key name used to organize the objects that you store in your S3 buckets. For example, object key names that start with the <code>engineering/</code> prefix or object key names that start with the <code>marketing/campaigns/</code> prefix.</p>"""
    iam_role_arn: "capo_s3_control.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants assumes this role to manage access to the registered location. </p>"""
    tags: NotRequired["capo_s3_control.types.tag_list.TagList"]
    """<p>The Amazon Web Services resource tags that you are adding to the S3 Access Grants location. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateAccessGrantsLocationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "LocationScope").text = str(value["location_scope"])
    SubElement(el, "IAMRoleArn").text = str(value["iam_role_arn"])
    if "tags" in value:
        import capo_s3_control.types.tag_list

        capo_s3_control.types.tag_list.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateAccessGrantsLocationRequest:
    out: CreateAccessGrantsLocationRequest = {}  # type: ignore[typeddict-item]
    child_location_scope = el.find("LocationScope")
    if child_location_scope is not None:
        out["location_scope"] = str(child_location_scope.text or "")
    else:
        out["location_scope"] = ""
    child_iam_role_arn = el.find("IAMRoleArn")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    else:
        out["iam_role_arn"] = ""
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.tag_list

        out["tags"] = capo_s3_control.types.tag_list.deserialize_xml(child_tags)
    return out
