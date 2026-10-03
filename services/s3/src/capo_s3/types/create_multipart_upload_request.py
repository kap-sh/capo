"""Generated from Smithy shape ``com.amazonaws.s3#CreateMultipartUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_key_enabled
    import capo_s3.types.bucket_name
    import capo_s3.types.cache_control
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.checksum_type
    import capo_s3.types.content_disposition
    import capo_s3.types.content_encoding
    import capo_s3.types.content_language
    import capo_s3.types.content_type
    import capo_s3.types.expires
    import capo_s3.types.grant_full_control
    import capo_s3.types.grant_read
    import capo_s3.types.grant_read_acp
    import capo_s3.types.grant_write_acp
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
    import capo_s3.types.tagging_header
    import capo_s3.types.website_redirect_location


class CreateMultipartUploadRequest(TypedDict, closed=True):
    acl: NotRequired["capo_s3.types.object_canned_acl.ObjectCannedACL"]
    """<p>The canned ACL to apply to the object. Amazon S3 supports a set of predefined ACLs, known as <i>canned ACLs</i>. Each canned ACL has a predefined set of grantees and permissions. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL">Canned ACL</a> in the <i>Amazon S3 User Guide</i>.</p> <p>By default, all objects are private. Only the owner has full access control. When uploading an object, you can grant access permissions to individual Amazon Web Services accounts or to predefined groups defined by Amazon S3. These permissions are then added to the access control list (ACL) on the new object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html">Using ACLs</a>. One way to grant the permissions using the request headers is to specify a canned ACL with the <code>x-amz-acl</code> request header.</p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket where the multipart upload is initiated and where the object is uploaded.</p> <p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    cache_control: NotRequired["capo_s3.types.cache_control.CacheControl"]
    """<p>Specifies caching behavior along the request/reply chain.</p>"""
    content_disposition: NotRequired[
        "capo_s3.types.content_disposition.ContentDisposition"
    ]
    """<p>Specifies presentational information for the object.</p>"""
    content_encoding: NotRequired["capo_s3.types.content_encoding.ContentEncoding"]
    """<p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.</p> <note> <p>For directory buckets, only the <code>aws-chunked</code> value is supported in this header field.</p> </note>"""
    content_language: NotRequired["capo_s3.types.content_language.ContentLanguage"]
    """<p>The language that the content is in.</p>"""
    content_type: NotRequired["capo_s3.types.content_type.ContentType"]
    """<p>A standard MIME type describing the format of the object data.</p>"""
    expires: NotRequired["capo_s3.types.expires.Expires"]
    """<p>The date and time at which the object is no longer cacheable.</p>"""
    grant_full_control: NotRequired["capo_s3.types.grant_full_control.GrantFullControl"]
    """<p>Specify access permissions explicitly to give the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.</p> <p>By default, all objects are private. Only the owner has full access control. When uploading an object, you can use this header to explicitly grant access permissions to specific Amazon Web Services accounts or groups. This header maps to specific permissions that Amazon S3 supports in an ACL. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html">Access Control List (ACL) Overview</a> in the <i>Amazon S3 User Guide</i>.</p> <p>You specify each grantee as a type=value pair, where the type is one of the following:</p> <ul> <li> <p> <code>id</code> – if the value specified is the canonical user ID of an Amazon Web Services account</p> </li> <li> <p> <code>uri</code> – if you are granting permissions to a predefined group</p> </li> <li> <p> <code>emailAddress</code> – if the value specified is the email address of an Amazon Web Services account</p> <note> <p>Using email addresses to specify a grantee is only supported in the following Amazon Web Services Regions: </p> <ul> <li> <p>US East (N. Virginia)</p> </li> <li> <p>US West (N. California)</p> </li> <li> <p> US West (Oregon)</p> </li> <li> <p> Asia Pacific (Singapore)</p> </li> <li> <p>Asia Pacific (Sydney)</p> </li> <li> <p>Asia Pacific (Tokyo)</p> </li> <li> <p>Europe (Ireland)</p> </li> <li> <p>South America (São Paulo)</p> </li> </ul> <p>For a list of all the Amazon S3 supported Regions and endpoints, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">Regions and Endpoints</a> in the Amazon Web Services General Reference.</p> </note> </li> </ul> <p>For example, the following <code>x-amz-grant-read</code> header grants the Amazon Web Services accounts identified by account IDs permissions to read object data and its metadata:</p> <p> <code>x-amz-grant-read: id="11112222333", id="444455556666" </code> </p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    grant_read: NotRequired["capo_s3.types.grant_read.GrantRead"]
    """<p>Specify access permissions explicitly to allow grantee to read the object data and its metadata.</p> <p>By default, all objects are private. Only the owner has full access control. When uploading an object, you can use this header to explicitly grant access permissions to specific Amazon Web Services accounts or groups. This header maps to specific permissions that Amazon S3 supports in an ACL. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html">Access Control List (ACL) Overview</a> in the <i>Amazon S3 User Guide</i>.</p> <p>You specify each grantee as a type=value pair, where the type is one of the following:</p> <ul> <li> <p> <code>id</code> – if the value specified is the canonical user ID of an Amazon Web Services account</p> </li> <li> <p> <code>uri</code> – if you are granting permissions to a predefined group</p> </li> <li> <p> <code>emailAddress</code> – if the value specified is the email address of an Amazon Web Services account</p> <note> <p>Using email addresses to specify a grantee is only supported in the following Amazon Web Services Regions: </p> <ul> <li> <p>US East (N. Virginia)</p> </li> <li> <p>US West (N. California)</p> </li> <li> <p> US West (Oregon)</p> </li> <li> <p> Asia Pacific (Singapore)</p> </li> <li> <p>Asia Pacific (Sydney)</p> </li> <li> <p>Asia Pacific (Tokyo)</p> </li> <li> <p>Europe (Ireland)</p> </li> <li> <p>South America (São Paulo)</p> </li> </ul> <p>For a list of all the Amazon S3 supported Regions and endpoints, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">Regions and Endpoints</a> in the Amazon Web Services General Reference.</p> </note> </li> </ul> <p>For example, the following <code>x-amz-grant-read</code> header grants the Amazon Web Services accounts identified by account IDs permissions to read object data and its metadata:</p> <p> <code>x-amz-grant-read: id="11112222333", id="444455556666" </code> </p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    grant_read_acp: NotRequired["capo_s3.types.grant_read_acp.GrantReadACP"]
    """<p>Specify access permissions explicitly to allows grantee to read the object ACL.</p> <p>By default, all objects are private. Only the owner has full access control. When uploading an object, you can use this header to explicitly grant access permissions to specific Amazon Web Services accounts or groups. This header maps to specific permissions that Amazon S3 supports in an ACL. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html">Access Control List (ACL) Overview</a> in the <i>Amazon S3 User Guide</i>.</p> <p>You specify each grantee as a type=value pair, where the type is one of the following:</p> <ul> <li> <p> <code>id</code> – if the value specified is the canonical user ID of an Amazon Web Services account</p> </li> <li> <p> <code>uri</code> – if you are granting permissions to a predefined group</p> </li> <li> <p> <code>emailAddress</code> – if the value specified is the email address of an Amazon Web Services account</p> <note> <p>Using email addresses to specify a grantee is only supported in the following Amazon Web Services Regions: </p> <ul> <li> <p>US East (N. Virginia)</p> </li> <li> <p>US West (N. California)</p> </li> <li> <p> US West (Oregon)</p> </li> <li> <p> Asia Pacific (Singapore)</p> </li> <li> <p>Asia Pacific (Sydney)</p> </li> <li> <p>Asia Pacific (Tokyo)</p> </li> <li> <p>Europe (Ireland)</p> </li> <li> <p>South America (São Paulo)</p> </li> </ul> <p>For a list of all the Amazon S3 supported Regions and endpoints, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">Regions and Endpoints</a> in the Amazon Web Services General Reference.</p> </note> </li> </ul> <p>For example, the following <code>x-amz-grant-read</code> header grants the Amazon Web Services accounts identified by account IDs permissions to read object data and its metadata:</p> <p> <code>x-amz-grant-read: id="11112222333", id="444455556666" </code> </p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    grant_write_acp: NotRequired["capo_s3.types.grant_write_acp.GrantWriteACP"]
    """<p>Specify access permissions explicitly to allows grantee to allow grantee to write the ACL for the applicable object.</p> <p>By default, all objects are private. Only the owner has full access control. When uploading an object, you can use this header to explicitly grant access permissions to specific Amazon Web Services accounts or groups. This header maps to specific permissions that Amazon S3 supports in an ACL. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html">Access Control List (ACL) Overview</a> in the <i>Amazon S3 User Guide</i>.</p> <p>You specify each grantee as a type=value pair, where the type is one of the following:</p> <ul> <li> <p> <code>id</code> – if the value specified is the canonical user ID of an Amazon Web Services account</p> </li> <li> <p> <code>uri</code> – if you are granting permissions to a predefined group</p> </li> <li> <p> <code>emailAddress</code> – if the value specified is the email address of an Amazon Web Services account</p> <note> <p>Using email addresses to specify a grantee is only supported in the following Amazon Web Services Regions: </p> <ul> <li> <p>US East (N. Virginia)</p> </li> <li> <p>US West (N. California)</p> </li> <li> <p> US West (Oregon)</p> </li> <li> <p> Asia Pacific (Singapore)</p> </li> <li> <p>Asia Pacific (Sydney)</p> </li> <li> <p>Asia Pacific (Tokyo)</p> </li> <li> <p>Europe (Ireland)</p> </li> <li> <p>South America (São Paulo)</p> </li> </ul> <p>For a list of all the Amazon S3 supported Regions and endpoints, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">Regions and Endpoints</a> in the Amazon Web Services General Reference.</p> </note> </li> </ul> <p>For example, the following <code>x-amz-grant-read</code> header grants the Amazon Web Services accounts identified by account IDs permissions to read object data and its metadata:</p> <p> <code>x-amz-grant-read: id="11112222333", id="444455556666" </code> </p> <note> <ul> <li> <p>This functionality is not supported for directory buckets.</p> </li> <li> <p>This functionality is not supported for Amazon S3 on Outposts.</p> </li> </ul> </note>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>Object key for which the multipart upload is to be initiated.</p>"""
    metadata: NotRequired["capo_s3.types.metadata.Metadata"]
    """<p>A map of metadata to store with the object in S3.</p>"""
    server_side_encryption: NotRequired[
        "capo_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.</p> <ul> <li> <p> <b>Directory buckets </b> - For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (<code>AES256</code>) and server-side encryption with KMS keys (SSE-KMS) (<code>aws:kms</code>). We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your <code>CreateSession</code> requests or <code>PUT</code> object requests. Then, new objects are automatically encrypted with the desired encryption settings. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html">Protecting data with server-side encryption</a> in the <i>Amazon S3 User Guide</i>. For more information about the encryption overriding behaviors in directory buckets, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-specifying-kms-encryption.html">Specifying server-side encryption with KMS for new object uploads</a>. </p> <p>In the Zonal endpoint API calls (except <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html">CopyObject</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html">UploadPartCopy</a>) using the REST API, the encryption request headers must match the encryption settings that are specified in the <code>CreateSession</code> request. You can't override the values of the encryption settings (<code>x-amz-server-side-encryption</code>, <code>x-amz-server-side-encryption-aws-kms-key-id</code>, <code>x-amz-server-side-encryption-context</code>, and <code>x-amz-server-side-encryption-bucket-key-enabled</code>) that are specified in the <code>CreateSession</code> request. You don't need to explicitly specify these encryption settings values in Zonal endpoint API calls, and Amazon S3 will use the encryption settings values from the <code>CreateSession</code> request to protect new objects in the directory bucket. </p> <note> <p>When you use the CLI or the Amazon Web Services SDKs, for <code>CreateSession</code>, the session token refreshes automatically to avoid service interruptions when a session expires. The CLI or the Amazon Web Services SDKs use the bucket's default encryption configuration for the <code>CreateSession</code> request. It's not supported to override the encryption settings values in the <code>CreateSession</code> request. So in the Zonal endpoint API calls (except <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html">CopyObject</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html">UploadPartCopy</a>), the encryption request headers must match the default encryption configuration of the directory bucket. </p> </note> </li> <li> <p> <b>S3 access points for Amazon FSx </b> - When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side encryption option is <code>aws:fsx</code>. All Amazon FSx file systems have encryption configured by default and are encrypted at rest. Data is automatically encrypted before being written to the file system, and automatically decrypted as it is read. These processes are handled transparently by Amazon FSx.</p> </li> </ul>"""
    storage_class: NotRequired["capo_s3.types.storage_class.StorageClass"]
    """<p>By default, Amazon S3 uses the STANDARD Storage Class to store newly created objects. The STANDARD storage class provides high durability and high availability. Depending on performance needs, you can specify a different Storage Class. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage Classes</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <ul> <li> <p>Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </li> <li> <p>Amazon S3 on Outposts only uses the OUTPOSTS Storage Class.</p> </li> </ul> </note>"""
    website_redirect_location: NotRequired[
        "capo_s3.types.website_redirect_location.WebsiteRedirectLocation"
    ]
    """<p>If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>Specifies the algorithm to use when encrypting the object (for example, AES256).</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key: NotRequired["capo_s3.types.sse_customer_key.SSECustomerKey"]
    """<p>Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the <code>x-amz-server-side-encryption-customer-algorithm</code> header.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>Specifies the 128-bit MD5 digest of the customer-provided encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    ssekms_key_id: NotRequired["capo_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>Specifies the KMS key ID (Key ID, Key ARN, or Key Alias) to use for object encryption. If the KMS key doesn't exist in the same account that's issuing the command, you must use the full Key ARN not the Key ID.</p> <p> <b>General purpose buckets</b> - If you specify <code>x-amz-server-side-encryption</code> with <code>aws:kms</code> or <code>aws:kms:dsse</code>, this header specifies the ID (Key ID, Key ARN, or Key Alias) of the KMS key to use. If you specify <code>x-amz-server-side-encryption:aws:kms</code> or <code>x-amz-server-side-encryption:aws:kms:dsse</code>, but do not provide <code>x-amz-server-side-encryption-aws-kms-key-id</code>, Amazon S3 uses the Amazon Web Services managed key (<code>aws/s3</code>) to protect the data.</p> <p> <b>Directory buckets</b> - To encrypt data using SSE-KMS, it's recommended to specify the <code>x-amz-server-side-encryption</code> header to <code>aws:kms</code>. Then, the <code>x-amz-server-side-encryption-aws-kms-key-id</code> header implicitly uses the bucket's default KMS customer managed key ID. If you want to explicitly set the <code> x-amz-server-side-encryption-aws-kms-key-id</code> header, it must match the bucket's default customer managed key (using key ID or ARN, not alias). Your SSE-KMS configuration can only support 1 <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">customer managed key</a> per directory bucket's lifetime. The <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk">Amazon Web Services managed key</a> (<code>aws/s3</code>) isn't supported. Incorrect key specification results in an HTTP <code>400 Bad Request</code> error. </p>"""
    ssekms_encryption_context: NotRequired[
        "capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext"
    ]
    """<p>Specifies the Amazon Web Services KMS Encryption Context to use for object encryption. The value of this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs.</p> <p> <b>Directory buckets</b> - You can optionally provide an explicit encryption context value. The value must match the default encryption context - the bucket Amazon Resource Name (ARN). An additional encryption context value is not supported. </p>"""
    bucket_key_enabled: NotRequired["capo_s3.types.bucket_key_enabled.BucketKeyEnabled"]
    """<p>Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using Key Management Service (KMS) keys (SSE-KMS).</p> <p> <b>General purpose buckets</b> - Setting this header to <code>true</code> causes Amazon S3 to use an S3 Bucket Key for object encryption with SSE-KMS. Also, specifying this header with a PUT action doesn't affect bucket-level settings for S3 Bucket Key.</p> <p> <b>Directory buckets</b> - S3 Bucket Keys are always enabled for <code>GET</code> and <code>PUT</code> operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html">CopyObject</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html">UploadPartCopy</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops">the Copy operation in Batch Operations</a>, or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job">the import jobs</a>. In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.</p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    tagging: NotRequired["capo_s3.types.tagging_header.TaggingHeader"]
    """<p>The tag-set for the object. The tag-set must be encoded as URL Query parameters.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_mode: NotRequired["capo_s3.types.object_lock_mode.ObjectLockMode"]
    """<p>Specifies the Object Lock mode that you want to apply to the uploaded object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_retain_until_date: NotRequired[
        "capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate"
    ]
    """<p>Specifies the date and time when you want the Object Lock to expire.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_legal_hold_status: NotRequired[
        "capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus"
    ]
    """<p>Specifies whether you want to apply a legal hold to the uploaded object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_event_hold: NotRequired[
        "capo_s3.types.object_lock_event_hold.ObjectLockEventHold"
    ]
    """<p>Specifies the event hold status to apply to the uploaded object. Set to <code>ON</code> to enable or <code>OFF</code> to disable.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_event_hold_duration_days: NotRequired[
        "capo_s3.types.object_lock_event_hold_duration_days.ObjectLockEventHoldDurationDays"
    ]
    """<p>Specifies the event hold duration in days to apply to the uploaded object. You cannot specify a duration in both days and years.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_event_hold_duration_years: NotRequired[
        "capo_s3.types.object_lock_event_hold_duration_years.ObjectLockEventHoldDurationYears"
    ]
    """<p>Specifies the event hold duration in years to apply to the uploaded object. You cannot specify a duration in both days and years.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm that you want Amazon S3 to use to create the checksum for the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_type: NotRequired["capo_s3.types.checksum_type.ChecksumType"]
    """<p>Indicates the checksum type that you want Amazon S3 to use to calculate the object’s checksum value. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateMultipartUploadRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> CreateMultipartUploadRequest:
    out: CreateMultipartUploadRequest = {}  # type: ignore[typeddict-item]
    return out
