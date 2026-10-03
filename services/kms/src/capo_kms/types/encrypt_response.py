"""Generated from Smithy shape ``com.amazonaws.kms#EncryptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.ciphertext_type
    import capo_kms.types.encryption_algorithm_spec
    import capo_kms.types.key_id_type


class EncryptResponse(TypedDict, closed=True):
    ciphertext_blob: NotRequired["capo_kms.types.ciphertext_type.CiphertextType"]
    """<p>The encrypted plaintext. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) of the KMS key that was used to encrypt the plaintext.</p>"""
    encryption_algorithm: NotRequired[
        "capo_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>The encryption algorithm that was used to encrypt the plaintext.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptResponse) -> dict:
    out: dict = {}
    if "ciphertext_blob" in value:
        import capo_kms.types.ciphertext_type

        out["CiphertextBlob"] = capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
            value["ciphertext_blob"]
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "encryption_algorithm" in value:
        import capo_kms.types.encryption_algorithm_spec

        out["EncryptionAlgorithm"] = (
            capo_kms.types.encryption_algorithm_spec.serialize_aws_json_1_1(
                value["encryption_algorithm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptResponse:
    out: EncryptResponse = {}  # type: ignore[typeddict-item]
    if data.get("CiphertextBlob") is not None:
        import capo_kms.types.ciphertext_type

        out["ciphertext_blob"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextBlob"]
            )
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("EncryptionAlgorithm") is not None:
        import capo_kms.types.encryption_algorithm_spec

        out["encryption_algorithm"] = (
            capo_kms.types.encryption_algorithm_spec.deserialize_aws_json_1_1(
                data["EncryptionAlgorithm"]
            )
        )
    return out
