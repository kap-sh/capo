"""Generated from Smithy shape ``com.amazonaws.s3#UploadPartCopyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.copy_source
    import capo_s3.types.copy_source_if_match
    import capo_s3.types.copy_source_if_modified_since
    import capo_s3.types.copy_source_if_none_match
    import capo_s3.types.copy_source_if_unmodified_since
    import capo_s3.types.copy_source_range
    import capo_s3.types.copy_source_sse_customer_algorithm
    import capo_s3.types.copy_source_sse_customer_key
    import capo_s3.types.copy_source_sse_customer_key_md5
    import capo_s3.types.multipart_upload_id
    import capo_s3.types.object_key
    import capo_s3.types.part_number
    import capo_s3.types.request_payer
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key
    import capo_s3.types.sse_customer_key_md5


class UploadPartCopyRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The bucket name.</p> <p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Copying objects across different Amazon Web Services Regions isn't supported when the source or destination bucket is in Amazon Web Services Local Zones. The source and destination buckets must have the same parent Amazon Web Services Region. Otherwise, you get an HTTP <code>400 Bad Request</code> error with the error code <code>InvalidRequest</code>.</p> </note> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    copy_source: "capo_s3.types.copy_source.CopySource"
    """<p>Specifies the source object for the copy operation. You specify the value in one of two formats, depending on whether you want to access the source object through an <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html">access point</a>:</p> <ul> <li> <p>For objects not accessed through an access point, specify the name of the source bucket and key of the source object, separated by a slash (/). For example, to copy the object <code>reports/january.pdf</code> from the bucket <code>awsexamplebucket</code>, use <code>awsexamplebucket/reports/january.pdf</code>. The value must be URL-encoded.</p> </li> <li> <p>For objects accessed through access points, specify the Amazon Resource Name (ARN) of the object as accessed through the access point, in the format <code>arn:aws:s3:<Region>:<account-id>:accesspoint/<access-point-name>/object/<key></code>. For example, to copy the object <code>reports/january.pdf</code> through access point <code>my-access-point</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3:us-west-2:123456789012:accesspoint/my-access-point/object/reports/january.pdf</code>. The value must be URL encoded.</p> <note> <ul> <li> <p>Amazon S3 supports copy operations using Access points only when the source and destination buckets are in the same Amazon Web Services Region.</p> </li> <li> <p>Access points are not supported by directory buckets.</p> </li> </ul> </note> <p>Alternatively, for objects accessed through Amazon S3 on Outposts, specify the ARN of the object as accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/object/<key></code>. For example, to copy the object <code>reports/january.pdf</code> through outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/object/reports/january.pdf</code>. The value must be URL-encoded. </p> </li> </ul> <p>If your bucket has versioning enabled, you could have multiple versions of the same object. By default, <code>x-amz-copy-source</code> identifies the current version of the source object to copy. To copy a specific version of the source object to copy, append <code>?versionId=<version-id></code> to the <code>x-amz-copy-source</code> request header (for example, <code>x-amz-copy-source: /awsexamplebucket/reports/january.pdf?versionId=QUpfdndhfd8438MNFDN93jdnJFkdmqnh893</code>). </p> <p>If the current version is a delete marker and you don't specify a versionId in the <code>x-amz-copy-source</code> request header, Amazon S3 returns a <code>404 Not Found</code> error, because the object does not exist. If you specify versionId in the <code>x-amz-copy-source</code> and the versionId is a delete marker, Amazon S3 returns an HTTP <code>400 Bad Request</code> error, because you are not allowed to specify a delete marker as a version for the <code>x-amz-copy-source</code>. </p> <note> <p> <b>Directory buckets</b> - S3 Versioning isn't enabled and supported for directory buckets.</p> </note>"""
    copy_source_if_match: NotRequired[
        "capo_s3.types.copy_source_if_match.CopySourceIfMatch"
    ]
    """<p>Copies the object if its entity tag (ETag) matches the specified tag.</p> <p>If both of the <code>x-amz-copy-source-if-match</code> and <code>x-amz-copy-source-if-unmodified-since</code> headers are present in the request as follows:</p> <p> <code>x-amz-copy-source-if-match</code> condition evaluates to <code>true</code>, and;</p> <p> <code>x-amz-copy-source-if-unmodified-since</code> condition evaluates to <code>false</code>;</p> <p>Amazon S3 returns <code>200 OK</code> and copies the data. </p>"""
    copy_source_if_modified_since: NotRequired[
        "capo_s3.types.copy_source_if_modified_since.CopySourceIfModifiedSince"
    ]
    """<p>Copies the object if it has been modified since the specified time.</p> <p>If both of the <code>x-amz-copy-source-if-none-match</code> and <code>x-amz-copy-source-if-modified-since</code> headers are present in the request as follows:</p> <p> <code>x-amz-copy-source-if-none-match</code> condition evaluates to <code>false</code>, and;</p> <p> <code>x-amz-copy-source-if-modified-since</code> condition evaluates to <code>true</code>;</p> <p>Amazon S3 returns <code>412 Precondition Failed</code> response code. </p>"""
    copy_source_if_none_match: NotRequired[
        "capo_s3.types.copy_source_if_none_match.CopySourceIfNoneMatch"
    ]
    """<p>Copies the object if its entity tag (ETag) is different than the specified ETag.</p> <p>If both of the <code>x-amz-copy-source-if-none-match</code> and <code>x-amz-copy-source-if-modified-since</code> headers are present in the request as follows:</p> <p> <code>x-amz-copy-source-if-none-match</code> condition evaluates to <code>false</code>, and;</p> <p> <code>x-amz-copy-source-if-modified-since</code> condition evaluates to <code>true</code>;</p> <p>Amazon S3 returns <code>412 Precondition Failed</code> response code. </p>"""
    copy_source_if_unmodified_since: NotRequired[
        "capo_s3.types.copy_source_if_unmodified_since.CopySourceIfUnmodifiedSince"
    ]
    """<p>Copies the object if it hasn't been modified since the specified time.</p> <p>If both of the <code>x-amz-copy-source-if-match</code> and <code>x-amz-copy-source-if-unmodified-since</code> headers are present in the request as follows:</p> <p> <code>x-amz-copy-source-if-match</code> condition evaluates to <code>true</code>, and;</p> <p> <code>x-amz-copy-source-if-unmodified-since</code> condition evaluates to <code>false</code>;</p> <p>Amazon S3 returns <code>200 OK</code> and copies the data. </p>"""
    copy_source_range: NotRequired["capo_s3.types.copy_source_range.CopySourceRange"]
    """<p>The range of bytes to copy from the source object. The range value must use the form bytes=first-last, where the first and last are the zero-based byte offsets to copy. For example, bytes=0-9 indicates that you want to copy the first 10 bytes of the source. You can copy a range only if the source object is greater than 5 MB.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>Object key for which the multipart upload was initiated.</p>"""
    part_number: "capo_s3.types.part_number.PartNumber"
    """<p>Part number of part being copied. This is a positive integer between 1 and 10,000.</p>"""
    upload_id: "capo_s3.types.multipart_upload_id.MultipartUploadId"
    """<p>Upload ID identifying the multipart upload whose part is being copied.</p>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>Specifies the algorithm to use when encrypting the object (for example, AES256).</p> <note> <p>This functionality is not supported when the destination bucket is a directory bucket.</p> </note>"""
    sse_customer_key: NotRequired["capo_s3.types.sse_customer_key.SSECustomerKey"]
    """<p>Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the <code>x-amz-server-side-encryption-customer-algorithm</code> header. This must be the same encryption key specified in the initiate multipart upload request.</p> <note> <p>This functionality is not supported when the destination bucket is a directory bucket.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.</p> <note> <p>This functionality is not supported when the destination bucket is a directory bucket.</p> </note>"""
    copy_source_sse_customer_algorithm: NotRequired[
        "capo_s3.types.copy_source_sse_customer_algorithm.CopySourceSSECustomerAlgorithm"
    ]
    """<p>Specifies the algorithm to use when decrypting the source object (for example, <code>AES256</code>).</p> <note> <p>This functionality is not supported when the source object is in a directory bucket.</p> </note>"""
    copy_source_sse_customer_key: NotRequired[
        "capo_s3.types.copy_source_sse_customer_key.CopySourceSSECustomerKey"
    ]
    """<p>Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.</p> <note> <p>This functionality is not supported when the source object is in a directory bucket.</p> </note>"""
    copy_source_sse_customer_key_md5: NotRequired[
        "capo_s3.types.copy_source_sse_customer_key_md5.CopySourceSSECustomerKeyMD5"
    ]
    """<p>Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.</p> <note> <p>This functionality is not supported when the source object is in a directory bucket.</p> </note>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected destination bucket owner. If the account ID that you provide does not match the actual owner of the destination bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    expected_source_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected source bucket owner. If the account ID that you provide does not match the actual owner of the source bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UploadPartCopyRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> UploadPartCopyRequest:
    out: UploadPartCopyRequest = {}  # type: ignore[typeddict-item]
    return out
