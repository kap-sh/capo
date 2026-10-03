"""Generated from Smithy shape ``com.amazonaws.s3#WriteGetObjectResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3.types.accept_ranges
    import capo_s3.types.bucket_key_enabled
    import capo_s3.types.cache_control
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
    import capo_s3.types.content_range
    import capo_s3.types.content_type
    import capo_s3.types.delete_marker
    import capo_s3.types.e_tag
    import capo_s3.types.error_code
    import capo_s3.types.error_message
    import capo_s3.types.expiration
    import capo_s3.types.expires
    import capo_s3.types.get_object_response_status_code
    import capo_s3.types.last_modified
    import capo_s3.types.metadata
    import capo_s3.types.missing_meta
    import capo_s3.types.object_lock_legal_hold_status
    import capo_s3.types.object_lock_mode
    import capo_s3.types.object_lock_retain_until_date
    import capo_s3.types.object_version_id
    import capo_s3.types.parts_count
    import capo_s3.types.replication_status
    import capo_s3.types.request_charged
    import capo_s3.types.request_route
    import capo_s3.types.request_token
    import capo_s3.types.restore
    import capo_s3.types.server_side_encryption
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key_md5
    import capo_s3.types.ssekms_key_id
    import capo_s3.types.storage_class
    import capo_s3.types.streaming_blob
    import capo_s3.types.tag_count


class WriteGetObjectResponseRequest(TypedDict, closed=True):
    request_route: "capo_s3.types.request_route.RequestRoute"
    """<p>Route prefix to the HTTP URL generated.</p>"""
    request_token: "capo_s3.types.request_token.RequestToken"
    """<p>A single use encrypted token that maps <code>WriteGetObjectResponse</code> to the end user <code>GetObject</code> request.</p>"""
    body: "capo_s3.types.streaming_blob.StreamingBlob"
    """<p>The object data.</p>"""
    status_code: NotRequired[
        "capo_s3.types.get_object_response_status_code.GetObjectResponseStatusCode"
    ]
    """<p>The integer status code for an HTTP response of a corresponding <code>GetObject</code> request. The following is a list of status codes.</p> <ul> <li> <p> <code>200 - OK</code> </p> </li> <li> <p> <code>206 - Partial Content</code> </p> </li> <li> <p> <code>304 - Not Modified</code> </p> </li> <li> <p> <code>400 - Bad Request</code> </p> </li> <li> <p> <code>401 - Unauthorized</code> </p> </li> <li> <p> <code>403 - Forbidden</code> </p> </li> <li> <p> <code>404 - Not Found</code> </p> </li> <li> <p> <code>405 - Method Not Allowed</code> </p> </li> <li> <p> <code>409 - Conflict</code> </p> </li> <li> <p> <code>411 - Length Required</code> </p> </li> <li> <p> <code>412 - Precondition Failed</code> </p> </li> <li> <p> <code>416 - Range Not Satisfiable</code> </p> </li> <li> <p> <code>500 - Internal Server Error</code> </p> </li> <li> <p> <code>503 - Service Unavailable</code> </p> </li> </ul>"""
    error_code: NotRequired["capo_s3.types.error_code.ErrorCode"]
    """<p>A string that uniquely identifies an error condition. Returned in the <Code> tag of the error XML response for a corresponding <code>GetObject</code> call. Cannot be used with a successful <code>StatusCode</code> header or when the transformed object is provided in the body. All error codes from S3 are sentence-cased. The regular expression (regex) value is <code>"^[A-Z][a-zA-Z]+$"</code>.</p>"""
    error_message: NotRequired["capo_s3.types.error_message.ErrorMessage"]
    """<p>Contains a generic description of the error condition. Returned in the <Message> tag of the error XML response for a corresponding <code>GetObject</code> call. Cannot be used with a successful <code>StatusCode</code> header or when the transformed object is provided in body.</p>"""
    accept_ranges: NotRequired["capo_s3.types.accept_ranges.AcceptRanges"]
    """<p>Indicates that a range of bytes was specified.</p>"""
    cache_control: NotRequired["capo_s3.types.cache_control.CacheControl"]
    """<p>Specifies caching behavior along the request/reply chain.</p>"""
    content_disposition: NotRequired[
        "capo_s3.types.content_disposition.ContentDisposition"
    ]
    """<p>Specifies presentational information for the object.</p>"""
    content_encoding: NotRequired["capo_s3.types.content_encoding.ContentEncoding"]
    """<p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.</p>"""
    content_language: NotRequired["capo_s3.types.content_language.ContentLanguage"]
    """<p>The language the content is in.</p>"""
    content_length: NotRequired["capo_s3.types.content_length.ContentLength"]
    """<p>The size of the content body in bytes.</p>"""
    content_range: NotRequired["capo_s3.types.content_range.ContentRange"]
    """<p>The portion of the object returned in the response.</p>"""
    content_type: NotRequired["capo_s3.types.content_type.ContentType"]
    """<p>A standard MIME type describing the format of the object data.</p>"""
    checksum_crc32: NotRequired["capo_s3.types.checksum_crc32.ChecksumCRC32"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This specifies the Base64 encoded, 32-bit <code>CRC32</code> checksum of the object returned by the Object Lambda function. This may not match the checksum for the object stored in Amazon S3. Amazon S3 will perform validation of the checksum values only when the original <code>GetObject</code> request required checksum validation. For more information about checksums, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>Only one checksum header can be specified at a time. If you supply multiple checksum headers, this request will fail.</p> <p></p>"""
    checksum_crc32_c: NotRequired["capo_s3.types.checksum_crc32_c.ChecksumCRC32C"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This specifies the Base64 encoded, 32-bit <code>CRC32C</code> checksum of the object returned by the Object Lambda function. This may not match the checksum for the object stored in Amazon S3. Amazon S3 will perform validation of the checksum values only when the original <code>GetObject</code> request required checksum validation. For more information about checksums, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>Only one checksum header can be specified at a time. If you supply multiple checksum headers, this request will fail.</p>"""
    checksum_crc64_nvme: NotRequired[
        "capo_s3.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 64-bit <code>CRC64NVME</code> checksum of the part. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha1: NotRequired["capo_s3.types.checksum_sha1.ChecksumSHA1"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This specifies the Base64 encoded, 160-bit <code>SHA1</code> digest of the object returned by the Object Lambda function. This may not match the checksum for the object stored in Amazon S3. Amazon S3 will perform validation of the checksum values only when the original <code>GetObject</code> request required checksum validation. For more information about checksums, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>Only one checksum header can be specified at a time. If you supply multiple checksum headers, this request will fail.</p>"""
    checksum_sha256: NotRequired["capo_s3.types.checksum_sha256.ChecksumSHA256"]
    """<p>This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This specifies the Base64 encoded, 256-bit <code>SHA256</code> digest of the object returned by the Object Lambda function. This may not match the checksum for the object stored in Amazon S3. Amazon S3 will perform validation of the checksum values only when the original <code>GetObject</code> request required checksum validation. For more information about checksums, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>Only one checksum header can be specified at a time. If you supply multiple checksum headers, this request will fail.</p>"""
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
    delete_marker: NotRequired["capo_s3.types.delete_marker.DeleteMarker"]
    """<p>Specifies whether an object stored in Amazon S3 is (<code>true</code>) or is not (<code>false</code>) a delete marker. To learn more about delete markers, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html">Working with delete markers</a>.</p>"""
    e_tag: NotRequired["capo_s3.types.e_tag.ETag"]
    """<p>An opaque identifier assigned by a web server to a specific version of a resource found at a URL. </p>"""
    expires: NotRequired["capo_s3.types.expires.Expires"]
    """<p>The date and time at which the object is no longer cacheable.</p>"""
    expiration: NotRequired["capo_s3.types.expiration.Expiration"]
    """<p>If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the <code>expiry-date</code> and <code>rule-id</code> key-value pairs that provide the object expiration information. The value of the <code>rule-id</code> is URL-encoded. </p>"""
    last_modified: NotRequired["capo_s3.types.last_modified.LastModified"]
    """<p>The date and time that the object was last modified.</p>"""
    missing_meta: NotRequired["capo_s3.types.missing_meta.MissingMeta"]
    """<p>Set to the number of metadata entries not returned in <code>x-amz-meta</code> headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.</p>"""
    metadata: NotRequired["capo_s3.types.metadata.Metadata"]
    """<p>A map of metadata to store with the object in S3.</p>"""
    object_lock_mode: NotRequired["capo_s3.types.object_lock_mode.ObjectLockMode"]
    """<p>Indicates whether an object stored in Amazon S3 has Object Lock enabled. For more information about S3 Object Lock, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html">Object Lock</a>.</p>"""
    object_lock_legal_hold_status: NotRequired[
        "capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus"
    ]
    """<p>Indicates whether an object stored in Amazon S3 has an active legal hold.</p>"""
    object_lock_retain_until_date: NotRequired[
        "capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate"
    ]
    """<p>The date and time when Object Lock is configured to expire.</p>"""
    parts_count: NotRequired["capo_s3.types.parts_count.PartsCount"]
    """<p>The count of parts this object has.</p>"""
    replication_status: NotRequired[
        "capo_s3.types.replication_status.ReplicationStatus"
    ]
    """<p>Indicates if request involves bucket that is either a source or destination in a Replication rule. For more information about S3 Replication, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html">Replication</a>.</p>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]
    restore: NotRequired["capo_s3.types.restore.Restore"]
    """<p>Provides information about object restoration operation and expiration time of the restored object copy.</p>"""
    server_side_encryption: NotRequired[
        "capo_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p> The server-side encryption algorithm used when storing requested object in Amazon S3 or Amazon FSx.</p> <note> <p>When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side encryption option is <code>aws:fsx</code>.</p> </note>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>Encryption algorithm used if server-side encryption with a customer-provided encryption key was specified for object stored in Amazon S3.</p>"""
    ssekms_key_id: NotRequired["capo_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p> If present, specifies the ID (Key ID, Key ARN, or Key Alias) of the Amazon Web Services Key Management Service (Amazon Web Services KMS) symmetric encryption customer managed key that was used for stored in Amazon S3 object. </p>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p> 128-bit MD5 digest of customer-provided encryption key used in Amazon S3 to encrypt data stored in S3. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html">Protecting data using server-side encryption with customer-provided encryption keys (SSE-C)</a>.</p>"""
    storage_class: NotRequired["capo_s3.types.storage_class.StorageClass"]
    """<p>Provides storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage Classes</a>.</p>"""
    tag_count: NotRequired["capo_s3.types.tag_count.TagCount"]
    """<p>The number of tags, if any, on the object.</p>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>An ID used to reference a specific version of the object.</p>"""
    bucket_key_enabled: NotRequired["capo_s3.types.bucket_key_enabled.BucketKeyEnabled"]
    """<p> Indicates whether the object stored in Amazon S3 uses an S3 bucket key for server-side encryption with Amazon Web Services KMS (SSE-KMS).</p>"""
