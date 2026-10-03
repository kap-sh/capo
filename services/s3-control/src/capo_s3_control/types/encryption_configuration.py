"""Generated from Smithy shape ``com.amazonaws.s3control#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.replica_kms_key_id


class EncryptionConfiguration(TypedDict, closed=True):
    replica_kms_key_id: NotRequired[
        "capo_s3_control.types.replica_kms_key_id.ReplicaKmsKeyID"
    ]
    """<p>Specifies the ID of the customer managed KMS key that's stored in Key Management Service (KMS) for the destination bucket. This ID is either the Amazon Resource Name (ARN) for the KMS key or the alias ARN for the KMS key. Amazon S3 uses this KMS key to encrypt replica objects. Amazon S3 supports only symmetric encryption KMS keys. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks">Symmetric encryption KMS keys</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: EncryptionConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "replica_kms_key_id" in value:
        SubElement(el, "ReplicaKmsKeyID").text = str(value["replica_kms_key_id"])


def deserialize_xml(el: Element) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    child_replica_kms_key_id = el.find("ReplicaKmsKeyID")
    if child_replica_kms_key_id is not None:
        out["replica_kms_key_id"] = str(child_replica_kms_key_id.text or "")
    return out
