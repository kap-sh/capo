"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessGrantsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.continuation_token
    import capo_s3_control.types.grantee_identifier
    import capo_s3_control.types.grantee_type
    import capo_s3_control.types.identity_center_application_arn
    import capo_s3_control.types.max_results
    import capo_s3_control.types.permission
    import capo_s3_control.types.s3_prefix


class ListAccessGrantsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p>A pagination token to request the next page of results. Pass this value into a subsequent <code>List Access Grants</code> request in order to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p>The maximum number of access grants that you would like returned in the <code>List Access Grants</code> response. If the results include the pagination token <code>NextToken</code>, make another call using the <code>NextToken</code> to determine if there are more results.</p>"""
    grantee_type: NotRequired["capo_s3_control.types.grantee_type.GranteeType"]
    """<p>The type of the grantee to which access has been granted. It can be one of the following values:</p> <ul> <li> <p> <code>IAM</code> - An IAM user or role.</p> </li> <li> <p> <code>DIRECTORY_USER</code> - Your corporate directory user. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.</p> </li> <li> <p> <code>DIRECTORY_GROUP</code> - Your corporate directory group. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.</p> </li> </ul>"""
    grantee_identifier: NotRequired[
        "capo_s3_control.types.grantee_identifier.GranteeIdentifier"
    ]
    """<p>The unique identifer of the <code>Grantee</code>. If the grantee type is <code>IAM</code>, the identifier is the IAM Amazon Resource Name (ARN) of the user or role. If the grantee type is a directory user or group, the identifier is 128-bit universally unique identifier (UUID) in the format <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>. You can obtain this UUID from your Amazon Web Services IAM Identity Center instance.</p>"""
    permission: NotRequired["capo_s3_control.types.permission.Permission"]
    """<p>The type of permission granted to your S3 data, which can be set to one of the following values:</p> <ul> <li> <p> <code>READ</code> – Grant read-only access to the S3 data.</p> </li> <li> <p> <code>WRITE</code> – Grant write-only access to the S3 data.</p> </li> <li> <p> <code>READWRITE</code> – Grant both read and write access to the S3 data.</p> </li> </ul>"""
    grant_scope: NotRequired["capo_s3_control.types.s3_prefix.S3Prefix"]
    """<p>The S3 path of the data to which you are granting access. It is the result of appending the <code>Subprefix</code> to the location scope.</p>"""
    application_arn: NotRequired[
        "capo_s3_control.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListAccessGrantsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListAccessGrantsRequest:
    out: ListAccessGrantsRequest = {}  # type: ignore[typeddict-item]
    return out
