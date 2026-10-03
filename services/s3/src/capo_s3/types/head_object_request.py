"""Generated from Smithy shape ``com.amazonaws.s3#HeadObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_mode
    import capo_s3.types.if_match
    import capo_s3.types.if_modified_since
    import capo_s3.types.if_none_match
    import capo_s3.types.if_unmodified_since
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id
    import capo_s3.types.part_number
    import capo_s3.types.range
    import capo_s3.types.request_payer
    import capo_s3.types.response_cache_control
    import capo_s3.types.response_content_disposition
    import capo_s3.types.response_content_encoding
    import capo_s3.types.response_content_language
    import capo_s3.types.response_content_type
    import capo_s3.types.response_expires
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key
    import capo_s3.types.sse_customer_key_md5


class HeadObjectRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket that contains the object.</p> <p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    if_match: NotRequired["capo_s3.types.if_match.IfMatch"]
    """<p>Return the object only if its entity tag (ETag) is the same as the one specified; otherwise, return a 412 (precondition failed) error.</p> <p>If both of the <code>If-Match</code> and <code>If-Unmodified-Since</code> headers are present in the request as follows:</p> <ul> <li> <p> <code>If-Match</code> condition evaluates to <code>true</code>, and;</p> </li> <li> <p> <code>If-Unmodified-Since</code> condition evaluates to <code>false</code>;</p> </li> </ul> <p>Then Amazon S3 returns <code>200 OK</code> and the data requested.</p> <p>For more information about conditional requests, see <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>.</p>"""
    if_modified_since: NotRequired["capo_s3.types.if_modified_since.IfModifiedSince"]
    """<p>Return the object only if it has been modified since the specified time; otherwise, return a 304 (not modified) error.</p> <p>If both of the <code>If-None-Match</code> and <code>If-Modified-Since</code> headers are present in the request as follows:</p> <ul> <li> <p> <code>If-None-Match</code> condition evaluates to <code>false</code>, and;</p> </li> <li> <p> <code>If-Modified-Since</code> condition evaluates to <code>true</code>;</p> </li> </ul> <p>Then Amazon S3 returns the <code>304 Not Modified</code> response code.</p> <p>For more information about conditional requests, see <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>.</p>"""
    if_none_match: NotRequired["capo_s3.types.if_none_match.IfNoneMatch"]
    """<p>Return the object only if its entity tag (ETag) is different from the one specified; otherwise, return a 304 (not modified) error.</p> <p>If both of the <code>If-None-Match</code> and <code>If-Modified-Since</code> headers are present in the request as follows:</p> <ul> <li> <p> <code>If-None-Match</code> condition evaluates to <code>false</code>, and;</p> </li> <li> <p> <code>If-Modified-Since</code> condition evaluates to <code>true</code>;</p> </li> </ul> <p>Then Amazon S3 returns the <code>304 Not Modified</code> response code.</p> <p>For more information about conditional requests, see <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>.</p>"""
    if_unmodified_since: NotRequired[
        "capo_s3.types.if_unmodified_since.IfUnmodifiedSince"
    ]
    """<p>Return the object only if it has not been modified since the specified time; otherwise, return a 412 (precondition failed) error.</p> <p>If both of the <code>If-Match</code> and <code>If-Unmodified-Since</code> headers are present in the request as follows:</p> <ul> <li> <p> <code>If-Match</code> condition evaluates to <code>true</code>, and;</p> </li> <li> <p> <code>If-Unmodified-Since</code> condition evaluates to <code>false</code>;</p> </li> </ul> <p>Then Amazon S3 returns <code>200 OK</code> and the data requested.</p> <p>For more information about conditional requests, see <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>The object key.</p>"""
    range: NotRequired["capo_s3.types.range.Range"]
    """<p>HeadObject returns only the metadata for an object. If the Range is satisfiable, only the <code>ContentLength</code> is affected in the response. If the Range is not satisfiable, S3 returns a <code>416 - Requested Range Not Satisfiable</code> error.</p>"""
    response_cache_control: NotRequired[
        "capo_s3.types.response_cache_control.ResponseCacheControl"
    ]
    """<p>Sets the <code>Cache-Control</code> header of the response.</p>"""
    response_content_disposition: NotRequired[
        "capo_s3.types.response_content_disposition.ResponseContentDisposition"
    ]
    """<p>Sets the <code>Content-Disposition</code> header of the response.</p>"""
    response_content_encoding: NotRequired[
        "capo_s3.types.response_content_encoding.ResponseContentEncoding"
    ]
    """<p>Sets the <code>Content-Encoding</code> header of the response.</p>"""
    response_content_language: NotRequired[
        "capo_s3.types.response_content_language.ResponseContentLanguage"
    ]
    """<p>Sets the <code>Content-Language</code> header of the response.</p>"""
    response_content_type: NotRequired[
        "capo_s3.types.response_content_type.ResponseContentType"
    ]
    """<p>Sets the <code>Content-Type</code> header of the response.</p>"""
    response_expires: NotRequired["capo_s3.types.response_expires.ResponseExpires"]
    """<p>Sets the <code>Expires</code> header of the response.</p>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>Version ID used to reference a specific version of the object.</p> <note> <p>For directory buckets in this API operation, only the <code>null</code> value of the version ID is supported.</p> </note>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>Specifies the algorithm to use when encrypting the object (for example, AES256).</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key: NotRequired["capo_s3.types.sse_customer_key.SSECustomerKey"]
    """<p>Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the <code>x-amz-server-side-encryption-customer-algorithm</code> header.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    part_number: NotRequired["capo_s3.types.part_number.PartNumber"]
    """<p>Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a 'ranged' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    checksum_mode: NotRequired["capo_s3.types.checksum_mode.ChecksumMode"]
    """<p>To retrieve the checksum, this parameter must be enabled.</p> <p> <b>General purpose buckets</b> - If you enable checksum mode and the object is uploaded with a <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_Checksum.html">checksum</a> and encrypted with an Key Management Service (KMS) key, you must have permission to use the <code>kms:Decrypt</code> action to retrieve the checksum.</p> <p> <b>Directory buckets</b> - If you enable <code>ChecksumMode</code> and the object is encrypted with Amazon Web Services Key Management Service (Amazon Web Services KMS), you must also have the <code>kms:GenerateDataKey</code> and <code>kms:Decrypt</code> permissions in IAM identity-based policies and KMS key policies for the KMS key to retrieve the checksum of the object.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HeadObjectRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> HeadObjectRequest:
    out: HeadObjectRequest = {}  # type: ignore[typeddict-item]
    return out
