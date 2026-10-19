"""Generated from Smithy shape ``com.amazonaws.s3control#UpdateAccessGrantsLocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.access_grants_location_id
    import capo_s3_control.types.account_id
    import capo_s3_control.types.iam_role_arn


class UpdateAccessGrantsLocationRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    access_grants_location_id: (
        "capo_s3_control.types.access_grants_location_id.AccessGrantsLocationId"
    )
    """<p>The ID of the registered location that you are updating. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p> <p>The ID of the registered location to which you are granting access. S3 Access Grants assigned this ID when you registered the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p> <p>If you are passing the <code>default</code> location, you cannot create an access grant for the entire default location. You must also specify a bucket or a bucket and prefix in the <code>Subprefix</code> field. </p>"""
    iam_role_arn: "capo_s3_control.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants assumes this role to manage access to the registered location. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateAccessGrantsLocationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "IAMRoleArn").text = str(value["iam_role_arn"])


def deserialize_xml(el: Element) -> UpdateAccessGrantsLocationRequest:
    out: UpdateAccessGrantsLocationRequest = {}  # type: ignore[typeddict-item]
    child_iam_role_arn = el.find("IAMRoleArn")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    else:
        out["iam_role_arn"] = ""
    return out
