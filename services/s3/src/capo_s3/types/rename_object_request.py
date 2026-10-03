"""Generated from Smithy shape ``com.amazonaws.s3#RenameObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_name
    import capo_s3.types.client_token
    import capo_s3.types.if_match
    import capo_s3.types.if_modified_since
    import capo_s3.types.if_none_match
    import capo_s3.types.if_unmodified_since
    import capo_s3.types.object_key
    import capo_s3.types.rename_source
    import capo_s3.types.rename_source_if_match
    import capo_s3.types.rename_source_if_modified_since
    import capo_s3.types.rename_source_if_none_match
    import capo_s3.types.rename_source_if_unmodified_since


class RenameObjectRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The bucket name of the directory bucket containing the object.</p> <p> You must use virtual-hosted-style requests in the format <code>Bucket-name.s3express-zone-id.region-code.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Availability Zone. Bucket names must follow the format <code>bucket-base-name--zone-id--x-s3 </code> (for example, <code>amzn-s3-demo-bucket--usw2-az1--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>Key name of the object to rename.</p>"""
    rename_source: "capo_s3.types.rename_source.RenameSource"
    """<p>Specifies the source for the rename operation. The value must be URL encoded.</p>"""
    destination_if_match: NotRequired["capo_s3.types.if_match.IfMatch"]
    """<p>Renames the object only if the ETag (entity tag) value provided during the operation matches the ETag of the object in S3. The <code>If-Match</code> header field makes the request method conditional on ETags. If the ETag values do not match, the operation returns a <code>412 Precondition Failed</code> error.</p> <p>Expects the ETag value as a string.</p>"""
    destination_if_none_match: NotRequired["capo_s3.types.if_none_match.IfNoneMatch"]
    """<p> Renames the object only if the destination does not already exist in the specified directory bucket. If the object does exist when you send a request with <code>If-None-Match:*</code>, the S3 API will return a <code>412 Precondition Failed</code> error, preventing an overwrite. The <code>If-None-Match</code> header prevents overwrites of existing data by validating that there's not an object with the same key name already in your directory bucket.</p> <p> Expects the <code>*</code> character (asterisk).</p>"""
    destination_if_modified_since: NotRequired[
        "capo_s3.types.if_modified_since.IfModifiedSince"
    ]
    """<p>Renames the object if the destination exists and if it has been modified since the specified time.</p>"""
    destination_if_unmodified_since: NotRequired[
        "capo_s3.types.if_unmodified_since.IfUnmodifiedSince"
    ]
    """<p>Renames the object if it hasn't been modified since the specified time.</p>"""
    source_if_match: NotRequired[
        "capo_s3.types.rename_source_if_match.RenameSourceIfMatch"
    ]
    """<p>Renames the object if the source exists and if its entity tag (ETag) matches the specified ETag. </p>"""
    source_if_none_match: NotRequired[
        "capo_s3.types.rename_source_if_none_match.RenameSourceIfNoneMatch"
    ]
    """<p>Renames the object if the source exists and if its entity tag (ETag) is different than the specified ETag. If an asterisk (<code>*</code>) character is provided, the operation will fail and return a <code>412 Precondition Failed</code> error. </p>"""
    source_if_modified_since: NotRequired[
        "capo_s3.types.rename_source_if_modified_since.RenameSourceIfModifiedSince"
    ]
    """<p>Renames the object if the source exists and if it has been modified since the specified time.</p>"""
    source_if_unmodified_since: NotRequired[
        "capo_s3.types.rename_source_if_unmodified_since.RenameSourceIfUnmodifiedSince"
    ]
    """<p>Renames the object if the source exists and hasn't been modified since the specified time.</p>"""
    client_token: NotRequired["capo_s3.types.client_token.ClientToken"]
    """<p> A unique string with a max of 64 ASCII characters in the ASCII range of 33 - 126.</p> <note> <p> <code>RenameObject</code> supports idempotency using a client token. To make an idempotent API request using <code>RenameObject</code>, specify a client token in the request. You should not reuse the same client token for other API requests. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, the retry fails and an <code>IdempotentParameterMismatch</code> error is returned. </p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: RenameObjectRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> RenameObjectRequest:
    out: RenameObjectRequest = {}  # type: ignore[typeddict-item]
    return out
