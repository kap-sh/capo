"""Generated from Smithy shape ``com.amazonaws.s3#UploadPartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.checksum_crc32
    import capo_s3.types.checksum_crc32_c
    import capo_s3.types.checksum_crc64_nvme
    import capo_s3.types.checksum_md5
    import capo_s3.types.checksum_sha1
    import capo_s3.types.checksum_sha256
    import capo_s3.types.checksum_sha512
    import capo_s3.types.checksum_xxhash3
    import capo_s3.types.checksum_xxhash64
    import capo_s3.types.checksum_xxhash128
    import capo_s3.types.content_length
    import capo_s3.types.content_md5
    import capo_s3.types.multipart_upload_id
    import capo_s3.types.object_key
    import capo_s3.types.part_number
    import capo_s3.types.request_payer
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key
    import capo_s3.types.sse_customer_key_md5
    import capo_s3.types.streaming_blob


class UploadPartRequest(TypedDict, closed=True):
    body: "capo_s3.types.streaming_blob.StreamingBlob"
    """<p>Object data.</p>"""
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket to which the multipart upload was initiated.</p> <p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    content_length: NotRequired["capo_s3.types.content_length.ContentLength"]
    """<p>Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>The Base64 encoded 128-bit MD5 digest of the part data. This parameter is auto-populated when using the command from the CLI. This parameter is required if object lock parameters are specified.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p> <p>This checksum algorithm must be the same for all parts and it match the checksum value supplied in the <code>CreateMultipartUpload</code> request.</p>"""
    checksum_crc32: NotRequired["capo_s3.types.checksum_crc32.ChecksumCRC32"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 32-bit <code>CRC32</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc32_c: NotRequired["capo_s3.types.checksum_crc32_c.ChecksumCRC32C"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 32-bit <code>CRC32C</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc64_nvme: NotRequired[
        "capo_s3.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 64-bit <code>CRC64NVME</code> checksum of the part. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha1: NotRequired["capo_s3.types.checksum_sha1.ChecksumSHA1"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 160-bit <code>SHA1</code> digest of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha256: NotRequired["capo_s3.types.checksum_sha256.ChecksumSHA256"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 256-bit <code>SHA256</code> digest of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha512: NotRequired["capo_s3.types.checksum_sha512.ChecksumSHA512"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 512-bit <code>SHA512</code> digest of the part. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_md5: NotRequired["capo_s3.types.checksum_md5.ChecksumMD5"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 128-bit <code>MD5</code> digest of the part. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_xxhash64: NotRequired["capo_s3.types.checksum_xxhash64.ChecksumXXHASH64"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 64-bit <code>XXHASH64</code> checksum of the part. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_xxhash3: NotRequired["capo_s3.types.checksum_xxhash3.ChecksumXXHASH3"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 64-bit <code>XXHASH3</code> checksum of the part. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_xxhash128: NotRequired[
        "capo_s3.types.checksum_xxhash128.ChecksumXXHASH128"
    ]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 128-bit <code>XXHASH128</code> checksum of the part. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>Object key for which the multipart upload was initiated.</p>"""
    part_number: "capo_s3.types.part_number.PartNumber"
    """<p>Part number of part being uploaded. This is a positive integer between 1 and 10,000.</p>"""
    upload_id: "capo_s3.types.multipart_upload_id.MultipartUploadId"
    """<p>Upload ID identifying the multipart upload whose part is being uploaded.</p>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>Specifies the algorithm to use when encrypting the object (for example, AES256).</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key: NotRequired["capo_s3.types.sse_customer_key.SSECustomerKey"]
    """<p>Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the <code>x-amz-server-side-encryption-customer-algorithm header</code>. This must be the same encryption key specified in the initiate multipart upload request.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
