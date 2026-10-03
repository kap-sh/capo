"""Generated from Smithy shape ``com.amazonaws.s3#Encryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.kms_context
    import capo_s3.types.server_side_encryption
    import capo_s3.types.ssekms_key_id


class Encryption(TypedDict, closed=True):
    encryption_type: "capo_s3.types.server_side_encryption.ServerSideEncryption"
    """<p>The server-side encryption algorithm used when storing job results in Amazon S3 (for example, AES256, <code>aws:kms</code>).</p>"""
    kms_key_id: NotRequired["capo_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>If the encryption type is <code>aws:kms</code>, this optional value specifies the ID of the symmetric encryption customer managed key to use for encryption of job results. Amazon S3 only supports symmetric encryption KMS keys. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">Asymmetric keys in KMS</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>"""
    kms_context: NotRequired["capo_s3.types.kms_context.KMSContext"]
    """<p>If the encryption type is <code>aws:kms</code>, this optional value can be used to specify the encryption context for the restore results.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Encryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.server_side_encryption

    capo_s3.types.server_side_encryption.serialize_xml(
        value["encryption_type"], el, "EncryptionType"
    )
    if "kms_key_id" in value:
        SubElement(el, "KMSKeyId").text = str(value["kms_key_id"])
    if "kms_context" in value:
        SubElement(el, "KMSContext").text = str(value["kms_context"])


def deserialize_xml(el: Element) -> Encryption:
    out: Encryption = {}  # type: ignore[typeddict-item]
    child_encryption_type = el.find("EncryptionType")
    if child_encryption_type is not None:
        import capo_s3.types.server_side_encryption

        out["encryption_type"] = capo_s3.types.server_side_encryption.deserialize_xml(
            child_encryption_type
        )
    else:
        raise DeserializationError("Encryption.encryption_type required")
    child_kms_key_id = el.find("KMSKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_kms_context = el.find("KMSContext")
    if child_kms_context is not None:
        out["kms_context"] = str(child_kms_context.text or "")
    return out
