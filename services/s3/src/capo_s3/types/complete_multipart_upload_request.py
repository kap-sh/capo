"""Generated from Smithy shape ``com.amazonaws.s3#CompleteMultipartUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_crc32
    import capo_s3.types.checksum_crc32_c
    import capo_s3.types.checksum_crc64_nvme
    import capo_s3.types.checksum_md5
    import capo_s3.types.checksum_sha1
    import capo_s3.types.checksum_sha256
    import capo_s3.types.checksum_sha512
    import capo_s3.types.checksum_type
    import capo_s3.types.checksum_xxhash3
    import capo_s3.types.checksum_xxhash64
    import capo_s3.types.checksum_xxhash128
    import capo_s3.types.completed_multipart_upload
    import capo_s3.types.if_match
    import capo_s3.types.if_none_match
    import capo_s3.types.mpu_object_size
    import capo_s3.types.multipart_upload_id
    import capo_s3.types.object_key
    import capo_s3.types.request_payer
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key
    import capo_s3.types.sse_customer_key_md5


class CompleteMultipartUploadRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>Name of the bucket to which the multipart upload was initiated.</p> <p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>Object key for which the multipart upload was initiated.</p>"""
    multipart_upload: NotRequired[
        "capo_s3.types.completed_multipart_upload.CompletedMultipartUpload"
    ]
    """<p>The container for the multipart upload request information.</p>"""
    upload_id: "capo_s3.types.multipart_upload_id.MultipartUploadId"
    """<p>ID for the initiated multipart upload.</p>"""
    checksum_crc32: NotRequired["capo_s3.types.checksum_crc32.ChecksumCRC32"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 32-bit <code>CRC32</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc32_c: NotRequired["capo_s3.types.checksum_crc32_c.ChecksumCRC32C"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 32-bit <code>CRC32C</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc64_nvme: NotRequired[
        "capo_s3.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 64-bit <code>CRC64NVME</code> checksum of the object. The <code>CRC64NVME</code> checksum is always a full object checksum. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_sha1: NotRequired["capo_s3.types.checksum_sha1.ChecksumSHA1"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 160-bit <code>SHA1</code> digest of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha256: NotRequired["capo_s3.types.checksum_sha256.ChecksumSHA256"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 256-bit <code>SHA256</code> digest of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha512: NotRequired["capo_s3.types.checksum_sha512.ChecksumSHA512"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 512-bit <code>SHA512</code> digest of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_md5: NotRequired["capo_s3.types.checksum_md5.ChecksumMD5"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 128-bit <code>MD5</code> digest of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_xxhash64: NotRequired["capo_s3.types.checksum_xxhash64.ChecksumXXHASH64"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 64-bit <code>XXHASH64</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_xxhash3: NotRequired["capo_s3.types.checksum_xxhash3.ChecksumXXHASH3"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 64-bit <code>XXHASH3</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_xxhash128: NotRequired[
        "capo_s3.types.checksum_xxhash128.ChecksumXXHASH128"
    ]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 128-bit <code>XXHASH128</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_type: NotRequired["capo_s3.types.checksum_type.ChecksumType"]
    """<p>This header specifies the checksum type of the object, which determines how part-level checksums are combined to create an object-level checksum for multipart objects. You can use this header as a data integrity check to verify that the checksum type that is received is the same checksum that was specified. If the checksum type doesn’t match the checksum type that was specified for the object during the <code>CreateMultipartUpload</code> request, it’ll result in a <code>BadDigest</code> error. For more information, see Checking object integrity in the Amazon S3 User Guide. </p>"""
    mpu_object_size: NotRequired["capo_s3.types.mpu_object_size.MpuObjectSize"]
    """<p> The expected total object size of the multipart upload request. If there’s a mismatch between the specified object size value and the actual object size value, it results in an <code>HTTP 400 InvalidRequest</code> error. </p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    if_match: NotRequired["capo_s3.types.if_match.IfMatch"]
    """<p>Uploads the object only if the ETag (entity tag) value provided during the WRITE operation matches the ETag of the object in S3. If the ETag values do not match, the operation returns a <code>412 Precondition Failed</code> error.</p> <p>If a conflicting operation occurs during the upload S3 returns a <code>409 ConditionalRequestConflict</code> response. On a 409 failure you should fetch the object's ETag, re-initiate the multipart upload with <code>CreateMultipartUpload</code>, and re-upload each part.</p> <p>Expects the ETag value as a string.</p> <p>For more information about conditional requests, see <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>, or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html">Conditional requests</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    if_none_match: NotRequired["capo_s3.types.if_none_match.IfNoneMatch"]
    """<p>Uploads the object only if the object key name does not already exist in the bucket specified. Otherwise, Amazon S3 returns a <code>412 Precondition Failed</code> error.</p> <p>If a conflicting operation occurs during the upload S3 returns a <code>409 ConditionalRequestConflict</code> response. On a 409 failure you should re-initiate the multipart upload with <code>CreateMultipartUpload</code> and re-upload each part.</p> <p>Expects the '*' (asterisk) character.</p> <p>For more information about conditional requests, see <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>, or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html">Conditional requests</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is required only when the object was created using a checksum algorithm or if your bucket policy requires the use of SSE-C. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html#ssec-require-condition-key">Protecting data using SSE-C keys</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key: NotRequired["capo_s3.types.sse_customer_key.SSECustomerKey"]
    """<p>The server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html">Protecting data using SSE-C keys</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>The MD5 server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html">Protecting data using SSE-C keys</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CompleteMultipartUploadRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "multipart_upload" in value:
        import capo_s3.types.completed_multipart_upload

        capo_s3.types.completed_multipart_upload.serialize_xml(
            value["multipart_upload"], el, "CompleteMultipartUpload"
        )


def deserialize_xml(el: Element) -> CompleteMultipartUploadRequest:
    out: CompleteMultipartUploadRequest = {}  # type: ignore[typeddict-item]
    child_multipart_upload = el.find("CompleteMultipartUpload")
    if child_multipart_upload is not None:
        import capo_s3.types.completed_multipart_upload

        out["multipart_upload"] = (
            capo_s3.types.completed_multipart_upload.deserialize_xml(
                child_multipart_upload
            )
        )
    return out
