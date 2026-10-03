"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_key_enabled
    import capo_s3.types.bucket_name
    import capo_s3.types.cache_control
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
    import capo_s3.types.content_disposition
    import capo_s3.types.content_encoding
    import capo_s3.types.content_language
    import capo_s3.types.content_length
    import capo_s3.types.content_md5
    import capo_s3.types.content_type
    import capo_s3.types.expires
    import capo_s3.types.grant_full_control
    import capo_s3.types.grant_read
    import capo_s3.types.grant_read_acp
    import capo_s3.types.grant_write_acp
    import capo_s3.types.if_match
    import capo_s3.types.if_none_match
    import capo_s3.types.metadata
    import capo_s3.types.object_canned_acl
    import capo_s3.types.object_key
    import capo_s3.types.object_lock_event_hold
    import capo_s3.types.object_lock_event_hold_duration_days
    import capo_s3.types.object_lock_event_hold_duration_years
    import capo_s3.types.object_lock_legal_hold_status
    import capo_s3.types.object_lock_mode
    import capo_s3.types.object_lock_retain_until_date
    import capo_s3.types.request_payer
    import capo_s3.types.server_side_encryption
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key
    import capo_s3.types.sse_customer_key_md5
    import capo_s3.types.ssekms_encryption_context
    import capo_s3.types.ssekms_key_id
    import capo_s3.types.storage_class
    import capo_s3.types.streaming_blob
    import capo_s3.types.tagging_header
    import capo_s3.types.website_redirect_location
    import capo_s3.types.write_offset_bytes


class PutObjectRequest(TypedDict, closed=True):
    acl: NotRequired["capo_s3.types.object_canned_acl.ObjectCannedACL"]
    """<p>The canned ACL to apply to the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL">Canned ACL</a> in the <i>Amazon S3 User Guide</i>.</p> <p>When adding a new object, you can use headers to grant ACL-based permissions to individual Amazon Web Services accounts or to predefined groups defined by Amazon S3. These permissions are then added to the ACL on the object. By default, all objects are private. Only the owner has full access control. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html">Access Control List (ACL) Overview</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-using-rest-api.html">Managing ACLs Using the REST API</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If the bucket that you're uploading objects to uses the bucket owner enforced setting for S3 Object Ownership, ACLs are disabled and no longer affect permissions. Buckets that use this setting only accept PUT requests that don't specify an ACL or PUT requests that specify bucket owner full control ACLs, such as the <code>bucket-owner-full-control</code> canned ACL or an equivalent form of this ACL expressed in the XML format. PUT requests that contain other ACLs (for example, custom grants to certain Amazon Web Services accounts) fail and return a <code>400</code> error with the error code <code>AccessControlListNotSupported</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html"> Controlling ownership of objects and disabling ACLs</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    body: "capo_s3.types.streaming_blob.StreamingBlob"
    """<p>Object data.</p>"""
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The bucket name to which the PUT action was initiated. </p> <p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    cache_control: NotRequired["capo_s3.types.cache_control.CacheControl"]
    """<p>Can be used to specify caching behavior along the request/reply chain. For more information, see <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9</a>.</p>"""
    content_disposition: NotRequired[
        "capo_s3.types.content_disposition.ContentDisposition"
    ]
    """<p>Specifies presentational information for the object. For more information, see <a href="https://www.rfc-editor.org/rfc/rfc6266#section-4">https://www.rfc-editor.org/rfc/rfc6266#section-4</a>.</p>"""
    content_encoding: NotRequired["capo_s3.types.content_encoding.ContentEncoding"]
    """<p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. For more information, see <a href="https://www.rfc-editor.org/rfc/rfc9110.html#field.content-encoding">https://www.rfc-editor.org/rfc/rfc9110.html#field.content-encoding</a>.</p>"""
    content_language: NotRequired["capo_s3.types.content_language.ContentLanguage"]
    """<p>The language the content is in.</p>"""
    content_length: NotRequired["capo_s3.types.content_length.ContentLength"]
    """<p>Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically. For more information, see <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-content-length">https://www.rfc-editor.org/rfc/rfc9110.html#name-content-length</a>.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>The Base64 encoded 128-bit <code>MD5</code> digest of the message (without the headers) according to RFC 1864. This header can be used as a message integrity check to verify that the data is the same data that was originally sent. Although it is optional, we recommend using the Content-MD5 mechanism as an end-to-end integrity check. For more information about REST request authentication, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html">REST Authentication</a>.</p> <note> <p>The <code>Content-MD5</code> or <code>x-amz-sdk-checksum-algorithm</code> header is required for any request to upload an object with a retention period configured using Amazon S3 Object Lock. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-put-object">Uploading objects to an Object Lock enabled bucket </a> in the <i>Amazon S3 User Guide</i>.</p> </note> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    content_type: NotRequired["capo_s3.types.content_type.ContentType"]
    """<p>A standard MIME type describing the format of the contents. For more information, see <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-content-type">https://www.rfc-editor.org/rfc/rfc9110.html#name-content-type</a>.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum-<i>algorithm</i> </code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>.</p> <p>For the <code>x-amz-checksum-<i>algorithm</i> </code> header, replace <code> <i>algorithm</i> </code> with the supported algorithm from the following list: </p> <ul> <li> <p> <code>CRC32</code> </p> </li> <li> <p> <code>CRC32C</code> </p> </li> <li> <p> <code>CRC64NVME</code> </p> </li> <li> <p> <code>MD5</code> </p> </li> <li> <p> <code>SHA1</code> </p> </li> <li> <p> <code>SHA256</code> </p> </li> <li> <p> <code>SHA512</code> </p> </li> <li> <p> <code>XXHASH3</code> </p> </li> <li> <p> <code>XXHASH64</code> </p> </li> <li> <p> <code>XXHASH128</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If the individual checksum value you provide through <code>x-amz-checksum-<i>algorithm</i> </code> doesn't match the checksum algorithm you set through <code>x-amz-sdk-checksum-algorithm</code>, Amazon S3 fails the request with a <code>BadDigest</code> error.</p> <note> <p>The <code>Content-MD5</code> or <code>x-amz-sdk-checksum-algorithm</code> header is required for any request to upload an object with a retention period configured using Amazon S3 Object Lock. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-put-object">Uploading objects to an Object Lock enabled bucket </a> in the <i>Amazon S3 User Guide</i>.</p> </note> <p>For directory buckets, when you use Amazon Web Services SDKs, <code>CRC32</code> is the default checksum algorithm that's used for performance.</p>"""
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
    expires: NotRequired["capo_s3.types.expires.Expires"]
    """<p>The date and time at which the object is no longer cacheable. For more information, see <a href="https://www.rfc-editor.org/rfc/rfc7234#section-5.3">https://www.rfc-editor.org/rfc/rfc7234#section-5.3</a>.</p>"""
    if_match: NotRequired["capo_s3.types.if_match.IfMatch"]
    """<p>Uploads the object only if the ETag (entity tag) value provided during the WRITE operation matches the ETag of the object in S3. If the ETag values do not match, the operation returns a <code>412 Precondition Failed</code> error.</p> <p>If a conflicting operation occurs during the upload S3 returns a <code>409 ConditionalRequestConflict</code> response. On a 409 failure you should fetch the object's ETag and retry the upload.</p> <p>Expects the ETag value as a string.</p> <p>For more information about conditional requests, see <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>, or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html">Conditional requests</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    if_none_match: NotRequired["capo_s3.types.if_none_match.IfNoneMatch"]
    """<p>Uploads the object only if the object key name does not already exist in the bucket specified. Otherwise, Amazon S3 returns a <code>412 Precondition Failed</code> error.</p> <p>If a conflicting operation occurs during the upload S3 returns a <code>409 ConditionalRequestConflict</code> response. On a 409 failure you should retry the upload.</p> <p>Expects the '*' (asterisk) character.</p> <p>For more information about conditional requests, see <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>, or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html">Conditional requests</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    grant_full_control: NotRequired["capo_s3.types.grant_full_control.GrantFullControl"]
    """<p>Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.</p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    grant_read: NotRequired["capo_s3.types.grant_read.GrantRead"]
    """<p>Allows grantee to read the object data and its metadata.</p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    grant_read_acp: NotRequired["capo_s3.types.grant_read_acp.GrantReadACP"]
    """<p>Allows grantee to read the object ACL.</p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    grant_write_acp: NotRequired["capo_s3.types.grant_write_acp.GrantWriteACP"]
    """<p>Allows grantee to write the ACL for the applicable object.</p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>Object key for which the PUT action was initiated.</p>"""
    write_offset_bytes: NotRequired["capo_s3.types.write_offset_bytes.WriteOffsetBytes"]
    """<p> Specifies the offset for appending data to existing objects in bytes. The offset must be equal to the size of the existing object being appended to. If no object exists, setting this header to 0 will create a new object. </p> <note> <p>This functionality is only supported for objects in the Amazon S3 Express One Zone storage class in directory buckets.</p> </note>"""
    metadata: NotRequired["capo_s3.types.metadata.Metadata"]
    """<p>A map of metadata to store with the object in S3.</p>"""
    server_side_encryption: NotRequired[
        "capo_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm that was used when you store this object in Amazon S3 or Amazon FSx.</p> <ul> <li> <p> <b>General purpose buckets </b> - You have four mutually exclusive options to protect data using server-side encryption in Amazon S3, depending on how you choose to manage the encryption keys. Specifically, the encryption key options are Amazon S3 managed keys (SSE-S3), Amazon Web Services KMS keys (SSE-KMS or DSSE-KMS), and customer-provided keys (SSE-C). Amazon S3 encrypts data with server-side encryption by using Amazon S3 managed keys (SSE-S3) by default. You can optionally tell Amazon S3 to encrypt data at rest by using server-side encryption with other key options. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html">Using Server-Side Encryption</a> in the <i>Amazon S3 User Guide</i>.</p> </li> <li> <p> <b>Directory buckets </b> - For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (<code>AES256</code>) and server-side encryption with KMS keys (SSE-KMS) (<code>aws:kms</code>). We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your <code>CreateSession</code> requests or <code>PUT</code> object requests. Then, new objects are automatically encrypted with the desired encryption settings. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html">Protecting data with server-side encryption</a> in the <i>Amazon S3 User Guide</i>. For more information about the encryption overriding behaviors in directory buckets, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-specifying-kms-encryption.html">Specifying server-side encryption with KMS for new object uploads</a>. </p> <p>In the Zonal endpoint API calls (except <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html">CopyObject</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html">UploadPartCopy</a>) using the REST API, the encryption request headers must match the encryption settings that are specified in the <code>CreateSession</code> request. You can't override the values of the encryption settings (<code>x-amz-server-side-encryption</code>, <code>x-amz-server-side-encryption-aws-kms-key-id</code>, <code>x-amz-server-side-encryption-context</code>, and <code>x-amz-server-side-encryption-bucket-key-enabled</code>) that are specified in the <code>CreateSession</code> request. You don't need to explicitly specify these encryption settings values in Zonal endpoint API calls, and Amazon S3 will use the encryption settings values from the <code>CreateSession</code> request to protect new objects in the directory bucket. </p> <note> <p>When you use the CLI or the Amazon Web Services SDKs, for <code>CreateSession</code>, the session token refreshes automatically to avoid service interruptions when a session expires. The CLI or the Amazon Web Services SDKs use the bucket's default encryption configuration for the <code>CreateSession</code> request. It's not supported to override the encryption settings values in the <code>CreateSession</code> request. So in the Zonal endpoint API calls (except <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html">CopyObject</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html">UploadPartCopy</a>), the encryption request headers must match the default encryption configuration of the directory bucket. </p> </note> </li> <li> <p> <b>S3 access points for Amazon FSx </b> - When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side encryption option is <code>aws:fsx</code>. All Amazon FSx file systems have encryption configured by default and are encrypted at rest. Data is automatically encrypted before being written to the file system, and automatically decrypted as it is read. These processes are handled transparently by Amazon FSx.</p> </li> </ul>"""
    storage_class: NotRequired["capo_s3.types.storage_class.StorageClass"]
    """<p>By default, Amazon S3 uses the STANDARD Storage Class to store newly created objects. The STANDARD storage class provides high durability and high availability. Depending on performance needs, you can specify a different Storage Class. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage Classes</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <ul> <li> <p>Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </li> <li> <p>Amazon S3 on Outposts only uses the OUTPOSTS Storage Class.</p> </li> </ul> </note>"""
    website_redirect_location: NotRequired[
        "capo_s3.types.website_redirect_location.WebsiteRedirectLocation"
    ]
    """<p>If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata. For information about object metadata, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html">Object Key and Metadata</a> in the <i>Amazon S3 User Guide</i>.</p> <p>In the following example, the request header sets the redirect to an object (anotherPage.html) in the same bucket:</p> <p> <code>x-amz-website-redirect-location: /anotherPage.html</code> </p> <p>In the following example, the request header sets the object redirect to another website:</p> <p> <code>x-amz-website-redirect-location: http://www.example.com/</code> </p> <p>For more information about website hosting in Amazon S3, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html">Hosting Websites on Amazon S3</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html">How to Configure Website Page Redirects</a> in the <i>Amazon S3 User Guide</i>. </p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>Specifies the algorithm to use when encrypting the object (for example, <code>AES256</code>).</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key: NotRequired["capo_s3.types.sse_customer_key.SSECustomerKey"]
    """<p>Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the <code>x-amz-server-side-encryption-customer-algorithm</code> header.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    ssekms_key_id: NotRequired["capo_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>Specifies the KMS key ID (Key ID, Key ARN, or Key Alias) to use for object encryption. If the KMS key doesn't exist in the same account that's issuing the command, you must use the full Key ARN not the Key ID.</p> <p> <b>General purpose buckets</b> - If you specify <code>x-amz-server-side-encryption</code> with <code>aws:kms</code> or <code>aws:kms:dsse</code>, this header specifies the ID (Key ID, Key ARN, or Key Alias) of the KMS key to use. If you specify <code>x-amz-server-side-encryption:aws:kms</code> or <code>x-amz-server-side-encryption:aws:kms:dsse</code>, but do not provide <code>x-amz-server-side-encryption-aws-kms-key-id</code>, Amazon S3 uses the Amazon Web Services managed key (<code>aws/s3</code>) to protect the data.</p> <p> <b>Directory buckets</b> - To encrypt data using SSE-KMS, it's recommended to specify the <code>x-amz-server-side-encryption</code> header to <code>aws:kms</code>. Then, the <code>x-amz-server-side-encryption-aws-kms-key-id</code> header implicitly uses the bucket's default KMS customer managed key ID. If you want to explicitly set the <code> x-amz-server-side-encryption-aws-kms-key-id</code> header, it must match the bucket's default customer managed key (using key ID or ARN, not alias). Your SSE-KMS configuration can only support 1 <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">customer managed key</a> per directory bucket's lifetime. The <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk">Amazon Web Services managed key</a> (<code>aws/s3</code>) isn't supported. Incorrect key specification results in an HTTP <code>400 Bad Request</code> error. </p>"""
    ssekms_encryption_context: NotRequired[
        "capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext"
    ]
    """<p>Specifies the Amazon Web Services KMS Encryption Context as an additional encryption context to use for object encryption. The value of this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs. This value is stored as object metadata and automatically gets passed on to Amazon Web Services KMS for future <code>GetObject</code> operations on this object.</p> <p> <b>General purpose buckets</b> - This value must be explicitly added during <code>CopyObject</code> operations if you want an additional encryption context for your object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#encryption-context">Encryption context</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Directory buckets</b> - You can optionally provide an explicit encryption context value. The value must match the default encryption context - the bucket Amazon Resource Name (ARN). An additional encryption context value is not supported. </p>"""
    bucket_key_enabled: NotRequired["capo_s3.types.bucket_key_enabled.BucketKeyEnabled"]
    """<p>Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using Key Management Service (KMS) keys (SSE-KMS).</p> <p> <b>General purpose buckets</b> - Setting this header to <code>true</code> causes Amazon S3 to use an S3 Bucket Key for object encryption with SSE-KMS. Also, specifying this header with a PUT action doesn't affect bucket-level settings for S3 Bucket Key.</p> <p> <b>Directory buckets</b> - S3 Bucket Keys are always enabled for <code>GET</code> and <code>PUT</code> operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html">CopyObject</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html">UploadPartCopy</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops">the Copy operation in Batch Operations</a>, or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job">the import jobs</a>. In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.</p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    tagging: NotRequired["capo_s3.types.tagging_header.TaggingHeader"]
    """<p>The tag-set for the object. The tag-set must be encoded as URL Query parameters. (For example, "Key1=Value1")</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_mode: NotRequired["capo_s3.types.object_lock_mode.ObjectLockMode"]
    """<p>The Object Lock mode that you want to apply to this object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_retain_until_date: NotRequired[
        "capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate"
    ]
    """<p>The date and time when you want this object's Object Lock to expire. Must be formatted as a timestamp parameter.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_legal_hold_status: NotRequired[
        "capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus"
    ]
    """<p>Specifies whether a legal hold will be applied to this object. For more information about S3 Object Lock, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html">Object Lock</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_event_hold: NotRequired[
        "capo_s3.types.object_lock_event_hold.ObjectLockEventHold"
    ]
    """<p>Specifies the event hold status to apply to this object. Set to <code>ON</code> to enable or <code>OFF</code> to disable.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_event_hold_duration_days: NotRequired[
        "capo_s3.types.object_lock_event_hold_duration_days.ObjectLockEventHoldDurationDays"
    ]
    """<p>Specifies the event hold duration in days to apply to this object. You cannot specify a duration in both days and years.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_event_hold_duration_years: NotRequired[
        "capo_s3.types.object_lock_event_hold_duration_years.ObjectLockEventHoldDurationYears"
    ]
    """<p>Specifies the event hold duration in years to apply to this object. You cannot specify a duration in both days and years.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
