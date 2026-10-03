"""Generated from Smithy shape ``com.amazonaws.s3#ServerSideEncryptionByDefault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.server_side_encryption
    import capo_s3.types.ssekms_key_id


class ServerSideEncryptionByDefault(TypedDict, closed=True):
    sse_algorithm: "capo_s3.types.server_side_encryption.ServerSideEncryption"
    """<p>Server-side encryption algorithm to use for the default encryption.</p> <note> <p>For directory buckets, there are only two supported values for server-side encryption: <code>AES256</code> and <code>aws:kms</code>.</p> </note>"""
    kms_master_key_id: NotRequired["capo_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>Amazon Web Services Key Management Service (KMS) customer managed key ID to use for the default encryption. </p> <note> <ul> <li> <p> <b>General purpose buckets</b> - This parameter is allowed if and only if <code>SSEAlgorithm</code> is set to <code>aws:kms</code> or <code>aws:kms:dsse</code>.</p> </li> <li> <p> <b>Directory buckets</b> - This parameter is allowed if and only if <code>SSEAlgorithm</code> is set to <code>aws:kms</code>.</p> </li> </ul> </note> <p>You can specify the key ID, key alias, or the Amazon Resource Name (ARN) of the KMS key.</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key Alias: <code>alias/alias-name</code> </p> </li> </ul> <p>If you are using encryption with cross-account or Amazon Web Services service operations, you must use a fully qualified KMS key ARN. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html#bucket-encryption-update-bucket-policy">Using encryption for cross-account operations</a>.</p> <note> <ul> <li> <p> <b>General purpose buckets</b> - If you're specifying a customer managed KMS key, we recommend using a fully qualified KMS key ARN. If you use a KMS key alias instead, then KMS resolves the key within the requester’s account. This behavior can result in data that's encrypted with a KMS key that belongs to the requester, and not the bucket owner. Also, if you use a key ID, you can run into a LogDestination undeliverable error when creating a VPC flow log. </p> </li> <li> <p> <b>Directory buckets</b> - When you specify an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">KMS customer managed key</a> for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.</p> </li> </ul> </note> <important> <p>Amazon S3 only supports symmetric encryption KMS keys. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">Asymmetric keys in Amazon Web Services KMS</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p> </important>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ServerSideEncryptionByDefault, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.server_side_encryption

    capo_s3.types.server_side_encryption.serialize_xml(
        value["sse_algorithm"], el, "SSEAlgorithm"
    )
    if "kms_master_key_id" in value:
        SubElement(el, "KMSMasterKeyID").text = str(value["kms_master_key_id"])


def deserialize_xml(el: Element) -> ServerSideEncryptionByDefault:
    out: ServerSideEncryptionByDefault = {}  # type: ignore[typeddict-item]
    child_sse_algorithm = el.find("SSEAlgorithm")
    if child_sse_algorithm is not None:
        import capo_s3.types.server_side_encryption

        out["sse_algorithm"] = capo_s3.types.server_side_encryption.deserialize_xml(
            child_sse_algorithm
        )
    else:
        raise DeserializationError(
            "ServerSideEncryptionByDefault.sse_algorithm required"
        )
    child_kms_master_key_id = el.find("KMSMasterKeyID")
    if child_kms_master_key_id is not None:
        out["kms_master_key_id"] = str(child_kms_master_key_id.text or "")
    return out
