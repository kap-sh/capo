"""Generated from Smithy shape ``com.amazonaws.s3control#GetDataAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.audit_context
    import capo_s3_control.types.duration_seconds
    import capo_s3_control.types.instance_scope
    import capo_s3_control.types.permission
    import capo_s3_control.types.privilege
    import capo_s3_control.types.s3_prefix
    import capo_s3_control.types.s3_prefix_type


class GetDataAccessRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    target: "capo_s3_control.types.s3_prefix.S3Prefix"
    """<p>The S3 URI path of the data to which you are requesting temporary access credentials. If the requesting account has an access grant for this data, S3 Access Grants vends temporary access credentials in the response.</p>"""
    permission: "capo_s3_control.types.permission.Permission"
    """<p>The type of permission granted to your S3 data, which can be set to one of the following values:</p> <ul> <li> <p> <code>READ</code> – Grant read-only access to the S3 data.</p> </li> <li> <p> <code>WRITE</code> – Grant write-only access to the S3 data.</p> </li> <li> <p> <code>READWRITE</code> – Grant both read and write access to the S3 data.</p> </li> </ul>"""
    duration_seconds: NotRequired[
        "capo_s3_control.types.duration_seconds.DurationSeconds"
    ]
    """<p>The session duration, in seconds, of the temporary access credential that S3 Access Grants vends to the grantee or client application. The default value is 1 hour, but the grantee can specify a range from 900 seconds (15 minutes) up to 43200 seconds (12 hours). If the grantee requests a value higher than this maximum, the operation fails. </p>"""
    privilege: NotRequired["capo_s3_control.types.privilege.Privilege"]
    """<p>The scope of the temporary access credential that S3 Access Grants vends to the grantee or client application. </p> <ul> <li> <p> <code>Default</code> – The scope of the returned temporary access token is the scope of the grant that is closest to the target scope.</p> </li> <li> <p> <code>Minimal</code> – The scope of the returned temporary access token is the same as the requested target scope as long as the requested scope is the same as or a subset of the grant scope. </p> </li> </ul>"""
    target_type: NotRequired["capo_s3_control.types.s3_prefix_type.S3PrefixType"]
    """<p>The type of <code>Target</code>. The only possible value is <code>Object</code>. Pass this value if the target data that you would like to access is a path to an object. Do not pass this value if the target data is a bucket or a bucket and a prefix. </p>"""
    audit_context: NotRequired["capo_s3_control.types.audit_context.AuditContext"]
    """<p>The context to identify the job or query associated with the credential request. This information will be displayed in CloudTrail log in your account.</p>"""
    instance_scope: NotRequired["capo_s3_control.types.instance_scope.InstanceScope"]
    """<p>The scope of S3 Access Grants instances to search for a grant matching the requested S3 URI path.</p> <ul> <li> <p> <code>SELF</code> – Searches only the instance of the Amazon Web Services account ID in the request.</p> </li> <li> <p> <code>ALL</code> – Searches the instance of the Amazon Web Services account ID in the request and all instances shared with the caller's account through Amazon Web Services Resource Access Manager (RAM).</p> </li> </ul>"""


# --- restXml ser/de ---
def serialize_xml(value: GetDataAccessRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetDataAccessRequest:
    out: GetDataAccessRequest = {}  # type: ignore[typeddict-item]
    return out
