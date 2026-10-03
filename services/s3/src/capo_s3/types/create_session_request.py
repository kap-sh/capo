"""Generated from Smithy shape ``com.amazonaws.s3#CreateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_key_enabled
    import capo_s3.types.bucket_name
    import capo_s3.types.server_side_encryption
    import capo_s3.types.session_mode
    import capo_s3.types.ssekms_encryption_context
    import capo_s3.types.ssekms_key_id


class CreateSessionRequest(TypedDict, closed=True):
    session_mode: NotRequired["capo_s3.types.session_mode.SessionMode"]
    """<p>Specifies the mode of the session that will be created, either <code>ReadWrite</code> or <code>ReadOnly</code>. If no session mode is specified, the default behavior attempts to create a session with the maximum allowable privilege. It will first attempt to create a <code>ReadWrite</code> session, and if that is not allowed by permissions, it will attempt to create a <code>ReadOnly</code> session. If neither session type is allowed, the request will return an Access Denied error. A <code>ReadWrite</code> session is capable of executing all the Zonal endpoint API operations on a directory bucket. A <code>ReadOnly</code> session is constrained to execute the following Zonal endpoint API operations: <code>GetObject</code>, <code>HeadObject</code>, <code>ListObjectsV2</code>, <code>GetObjectAttributes</code>, <code>ListParts</code>, and <code>ListMultipartUploads</code>.</p>"""
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket that you create a session for.</p>"""
    server_side_encryption: NotRequired[
        "capo_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm to use when you store objects in the directory bucket.</p> <p>For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (<code>AES256</code>) and server-side encryption with KMS keys (SSE-KMS) (<code>aws:kms</code>). By default, Amazon S3 encrypts data with SSE-S3. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html">Protecting data with server-side encryption</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>S3 access points for Amazon FSx </b> - When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side encryption option is <code>aws:fsx</code>. All Amazon FSx file systems have encryption configured by default and are encrypted at rest. Data is automatically encrypted before being written to the file system, and automatically decrypted as it is read. These processes are handled transparently by Amazon FSx.</p>"""
    ssekms_key_id: NotRequired["capo_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>If you specify <code>x-amz-server-side-encryption</code> with <code>aws:kms</code>, you must specify the <code> x-amz-server-side-encryption-aws-kms-key-id</code> header with the ID (Key ID or Key ARN) of the KMS symmetric encryption customer managed key to use. Otherwise, you get an HTTP <code>400 Bad Request</code> error. Only use the key ID or key ARN. The key alias format of the KMS key isn't supported. Also, if the KMS key doesn't exist in the same account that't issuing the command, you must use the full Key ARN not the Key ID. </p> <p>Your SSE-KMS configuration can only support 1 <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">customer managed key</a> per directory bucket's lifetime. The <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk">Amazon Web Services managed key</a> (<code>aws/s3</code>) isn't supported. </p>"""
    ssekms_encryption_context: NotRequired[
        "capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext"
    ]
    """<p>Specifies the Amazon Web Services KMS Encryption Context as an additional encryption context to use for object encryption. The value of this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs. This value is stored as object metadata and automatically gets passed on to Amazon Web Services KMS for future <code>GetObject</code> operations on this object.</p> <p> <b>General purpose buckets</b> - This value must be explicitly added during <code>CopyObject</code> operations if you want an additional encryption context for your object. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#encryption-context">Encryption context</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Directory buckets</b> - You can optionally provide an explicit encryption context value. The value must match the default encryption context - the bucket Amazon Resource Name (ARN). An additional encryption context value is not supported. </p>"""
    bucket_key_enabled: NotRequired["capo_s3.types.bucket_key_enabled.BucketKeyEnabled"]
    """<p>Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using KMS keys (SSE-KMS).</p> <p>S3 Bucket Keys are always enabled for <code>GET</code> and <code>PUT</code> operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html">CopyObject</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html">UploadPartCopy</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops">the Copy operation in Batch Operations</a>, or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job">the import jobs</a>. In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateSessionRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> CreateSessionRequest:
    out: CreateSessionRequest = {}  # type: ignore[typeddict-item]
    return out
