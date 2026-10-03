"""Generated from Smithy shape ``com.amazonaws.s3#HeadObjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.accept_ranges
    import capo_s3.types.archive_status
    import capo_s3.types.bucket_key_enabled
    import capo_s3.types.cache_control
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
    import capo_s3.types.content_disposition
    import capo_s3.types.content_encoding
    import capo_s3.types.content_language
    import capo_s3.types.content_length
    import capo_s3.types.content_range
    import capo_s3.types.content_type
    import capo_s3.types.delete_marker
    import capo_s3.types.e_tag
    import capo_s3.types.expiration
    import capo_s3.types.expires
    import capo_s3.types.last_modified
    import capo_s3.types.metadata
    import capo_s3.types.missing_meta
    import capo_s3.types.object_lock_event_hold
    import capo_s3.types.object_lock_event_hold_duration_days
    import capo_s3.types.object_lock_event_hold_duration_years
    import capo_s3.types.object_lock_legal_hold_status
    import capo_s3.types.object_lock_mode
    import capo_s3.types.object_lock_retain_until_date
    import capo_s3.types.object_version_id
    import capo_s3.types.parts_count
    import capo_s3.types.replication_status
    import capo_s3.types.request_charged
    import capo_s3.types.restore
    import capo_s3.types.server_side_encryption
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key_md5
    import capo_s3.types.ssekms_key_id
    import capo_s3.types.storage_class
    import capo_s3.types.tag_count
    import capo_s3.types.website_redirect_location


class HeadObjectOutput(TypedDict, closed=True):
    delete_marker: NotRequired["capo_s3.types.delete_marker.DeleteMarker"]
    """<p>Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    accept_ranges: NotRequired["capo_s3.types.accept_ranges.AcceptRanges"]
    """<p>Indicates that a range of bytes was specified.</p>"""
    expiration: NotRequired["capo_s3.types.expiration.Expiration"]
    """<p>If the object expiration is configured (see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html"> <code>PutBucketLifecycleConfiguration</code> </a>), the response includes this header. It includes the <code>expiry-date</code> and <code>rule-id</code> key-value pairs providing object expiration information. The value of the <code>rule-id</code> is URL-encoded.</p> <note> <p>Object expiration information is not returned in directory buckets and this header returns the value "<code>NotImplemented</code>" in all responses for directory buckets.</p> </note>"""
    restore: NotRequired["capo_s3.types.restore.Restore"]
    """<p>If the object is an archived object (an object whose storage class is GLACIER), the response includes this header if either the archive restoration is in progress (see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html">RestoreObject</a> or an archive copy is already restored.</p> <p> If an archive copy is already restored, the header value indicates when Amazon S3 is scheduled to delete the object copy. For example:</p> <p> <code>x-amz-restore: ongoing-request="false", expiry-date="Fri, 21 Dec 2012 00:00:00 GMT"</code> </p> <p>If the object restoration is in progress, the header returns the value <code>ongoing-request="true"</code>.</p> <p>For more information about archiving objects, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html#lifecycle-transition-general-considerations">Transitioning Objects: General Considerations</a>.</p> <note> <p>This functionality is not supported for directory buckets. Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </note>"""
    archive_status: NotRequired["capo_s3.types.archive_status.ArchiveStatus"]
    """<p>The archive state of the head object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    last_modified: NotRequired["capo_s3.types.last_modified.LastModified"]
    """<p>Date and time when the object was last modified.</p>"""
    content_length: NotRequired["capo_s3.types.content_length.ContentLength"]
    """<p>Size of the body in bytes.</p>"""
    checksum_crc32: NotRequired["capo_s3.types.checksum_crc32.ChecksumCRC32"]
    """<p>The Base64 encoded, 32-bit <code>CRC32 checksum</code> of the object. This checksum is only present if the checksum was uploaded with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc32_c: NotRequired["capo_s3.types.checksum_crc32_c.ChecksumCRC32C"]
    """<p>The Base64 encoded, 32-bit <code>CRC32C</code> checksum of the object. This checksum is only present if the checksum was uploaded with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc64_nvme: NotRequired[
        "capo_s3.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>The Base64 encoded, 64-bit <code>CRC64NVME</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_sha1: NotRequired["capo_s3.types.checksum_sha1.ChecksumSHA1"]
    """<p>The Base64 encoded, 160-bit <code>SHA1</code> digest of the object. This checksum is only present if the checksum was uploaded with the object. When you use the API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha256: NotRequired["capo_s3.types.checksum_sha256.ChecksumSHA256"]
    """<p>The Base64 encoded, 256-bit <code>SHA256</code> digest of the object. This checksum is only present if the checksum was uploaded with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha512: NotRequired["capo_s3.types.checksum_sha512.ChecksumSHA512"]
    """<p>The Base64 encoded, 512-bit <code>SHA512</code> digest of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_md5: NotRequired["capo_s3.types.checksum_md5.ChecksumMD5"]
    """<p>The Base64 encoded, 128-bit <code>MD5</code> digest of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_xxhash64: NotRequired["capo_s3.types.checksum_xxhash64.ChecksumXXHASH64"]
    """<p>The Base64 encoded, 64-bit <code>XXHASH64</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_xxhash3: NotRequired["capo_s3.types.checksum_xxhash3.ChecksumXXHASH3"]
    """<p>The Base64 encoded, 64-bit <code>XXHASH3</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_xxhash128: NotRequired[
        "capo_s3.types.checksum_xxhash128.ChecksumXXHASH128"
    ]
    """<p>The Base64 encoded, 128-bit <code>XXHASH128</code> checksum of the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_type: NotRequired["capo_s3.types.checksum_type.ChecksumType"]
    """<p>The checksum type, which determines how part-level checksums are combined to create an object-level checksum for multipart objects. You can use this header response to verify that the checksum type that is received is the same checksum type that was specified in <code>CreateMultipartUpload</code> request. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    e_tag: NotRequired["capo_s3.types.e_tag.ETag"]
    """<p>An entity tag (ETag) is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.</p>"""
    missing_meta: NotRequired["capo_s3.types.missing_meta.MissingMeta"]
    """<p>This is set to the number of metadata entries not returned in <code>x-amz-meta</code> headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>Version ID of the object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    cache_control: NotRequired["capo_s3.types.cache_control.CacheControl"]
    """<p>Specifies caching behavior along the request/reply chain.</p>"""
    content_disposition: NotRequired[
        "capo_s3.types.content_disposition.ContentDisposition"
    ]
    """<p>Specifies presentational information for the object.</p>"""
    content_encoding: NotRequired["capo_s3.types.content_encoding.ContentEncoding"]
    """<p>Indicates what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.</p>"""
    content_language: NotRequired["capo_s3.types.content_language.ContentLanguage"]
    """<p>The language the content is in.</p>"""
    content_type: NotRequired["capo_s3.types.content_type.ContentType"]
    """<p>A standard MIME type describing the format of the object data.</p>"""
    content_range: NotRequired["capo_s3.types.content_range.ContentRange"]
    """<p>The portion of the object returned in the response for a <code>GET</code> request.</p>"""
    expires: NotRequired["capo_s3.types.expires.Expires"]
    """<p>The date and time at which the object is no longer cacheable.</p>"""
    website_redirect_location: NotRequired[
        "capo_s3.types.website_redirect_location.WebsiteRedirectLocation"
    ]
    """<p>If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    server_side_encryption: NotRequired[
        "capo_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.</p> <note> <p>When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side encryption option is <code>aws:fsx</code>.</p> </note>"""
    metadata: NotRequired["capo_s3.types.metadata.Metadata"]
    """<p>A map of metadata to store with the object in S3.</p>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>If server-side encryption with a customer-provided encryption key was requested, the response will include this header to confirm the encryption algorithm that's used.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide the round-trip message integrity verification of the customer-provided encryption key.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    ssekms_key_id: NotRequired["capo_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>If present, indicates the ID of the KMS key that was used for object encryption.</p>"""
    bucket_key_enabled: NotRequired["capo_s3.types.bucket_key_enabled.BucketKeyEnabled"]
    """<p>Indicates whether the object uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS) keys (SSE-KMS).</p>"""
    storage_class: NotRequired["capo_s3.types.storage_class.StorageClass"]
    """<p>Provides storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage Classes</a>.</p> <note> <p> <b>Directory buckets </b> - Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </note>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]
    replication_status: NotRequired[
        "capo_s3.types.replication_status.ReplicationStatus"
    ]
    """<p>Amazon S3 can return this header if your request involves a bucket that is either a source or a destination in a replication rule.</p> <p>In replication, you have a source bucket on which you configure replication and destination bucket or buckets where Amazon S3 stores object replicas. When you request an object (<code>GetObject</code>) or object metadata (<code>HeadObject</code>) from these buckets, Amazon S3 will return the <code>x-amz-replication-status</code> header in the response as follows:</p> <ul> <li> <p> <b>If requesting an object from the source bucket</b>, Amazon S3 will return the <code>x-amz-replication-status</code> header if the object in your request is eligible for replication.</p> <p> For example, suppose that in your replication configuration, you specify object prefix <code>TaxDocs</code> requesting Amazon S3 to replicate objects with key prefix <code>TaxDocs</code>. Any objects you upload with this key name prefix, for example <code>TaxDocs/document1.pdf</code>, are eligible for replication. For any object request with this key name prefix, Amazon S3 will return the <code>x-amz-replication-status</code> header with value PENDING, COMPLETED or FAILED indicating object replication status.</p> </li> <li> <p> <b>If requesting an object from a destination bucket</b>, Amazon S3 will return the <code>x-amz-replication-status</code> header with value REPLICA if the object in your request is a replica that Amazon S3 created and there is no replica modification replication in progress.</p> </li> <li> <p> <b>When replicating objects to multiple destination buckets</b>, the <code>x-amz-replication-status</code> header acts differently. The header of the source object will only return a value of COMPLETED when replication is successful to all destinations. The header will remain at value PENDING until replication has completed for all destinations. If one or more destinations fails replication the header will return FAILED. </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html">Replication</a>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    parts_count: NotRequired["capo_s3.types.parts_count.PartsCount"]
    """<p>The count of parts this object has. This value is only returned if you specify <code>partNumber</code> in your request and the object was uploaded as a multipart upload.</p>"""
    tag_count: NotRequired["capo_s3.types.tag_count.TagCount"]
    """<p>The number of tags, if any, on the object, when you have the relevant permission to read object tags.</p> <p>You can use <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html">GetObjectTagging</a> to retrieve the tag set associated with an object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_mode: NotRequired["capo_s3.types.object_lock_mode.ObjectLockMode"]
    """<p>The Object Lock mode, if any, that's in effect for this object. This header is only returned if the requester has the <code>s3:GetObjectRetention</code> permission. For more information about S3 Object Lock, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html">Object Lock</a>. </p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_retain_until_date: NotRequired[
        "capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate"
    ]
    """<p>The date and time when the Object Lock retention period expires. This header is only returned if the requester has the <code>s3:GetObjectRetention</code> permission.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_legal_hold_status: NotRequired[
        "capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus"
    ]
    """<p>Specifies whether a legal hold is in effect for this object. This header is only returned if the requester has the <code>s3:GetObjectLegalHold</code> permission. This header is not returned if the specified version of this object has never had a legal hold applied. For more information about S3 Object Lock, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html">Object Lock</a>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_event_hold: NotRequired[
        "capo_s3.types.object_lock_event_hold.ObjectLockEventHold"
    ]
    """<p>The event hold status for this object. This header is only returned if the requester has the <code>s3:GetObjectRetention</code> permission.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_event_hold_duration_days: NotRequired[
        "capo_s3.types.object_lock_event_hold_duration_days.ObjectLockEventHoldDurationDays"
    ]
    """<p>The event hold duration in days for this object. Only returned when the event hold is enabled.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_event_hold_duration_years: NotRequired[
        "capo_s3.types.object_lock_event_hold_duration_years.ObjectLockEventHoldDurationYears"
    ]
    """<p>The event hold duration in years for this object. Only returned when the event hold is enabled.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: HeadObjectOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> HeadObjectOutput:
    out: HeadObjectOutput = {}  # type: ignore[typeddict-item]
    return out
