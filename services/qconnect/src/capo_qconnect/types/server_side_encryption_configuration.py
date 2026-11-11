"""Generated from Smithy shape ``com.amazonaws.qconnect#ServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.replica_kms_key_list


class ServerSideEncryptionConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The customer managed key used for encryption. For more information about setting up a customer managed key for Amazon Q in Connect, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html">Enable Amazon Q in Connect for your instance</a>. For information about valid ID values, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id">Key identifiers (KeyId)</a>.</p>"""
    replica_kms_keys: NotRequired[
        "capo_qconnect.types.replica_kms_key_list.ReplicaKmsKeyList"
    ]
    """<p>The list of KMS keys used to encrypt data for this resource's replicas in other Amazon Web Services Regions. Each entry corresponds to a Region where a replica is configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerSideEncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "replica_kms_keys" in value:
        import capo_qconnect.types.replica_kms_key_list

        out["replicaKmsKeys"] = capo_qconnect.types.replica_kms_key_list.serialize_json(
            value["replica_kms_keys"]
        )
    return out


def deserialize_json(data: dict) -> ServerSideEncryptionConfiguration:
    out: ServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("replicaKmsKeys") is not None:
        import capo_qconnect.types.replica_kms_key_list

        out["replica_kms_keys"] = (
            capo_qconnect.types.replica_kms_key_list.deserialize_json(
                data["replicaKmsKeys"]
            )
        )
    return out
