"""Generated from Smithy shape ``com.amazonaws.kms#GenerateDataKeyPairWithoutPlaintextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.backing_key_id_type
    import capo_kms.types.ciphertext_type
    import capo_kms.types.data_key_pair_spec
    import capo_kms.types.key_id_type
    import capo_kms.types.public_key_type


class GenerateDataKeyPairWithoutPlaintextResponse(TypedDict, closed=True):
    private_key_ciphertext_blob: NotRequired[
        "capo_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The encrypted copy of the private key. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    public_key: NotRequired["capo_kms.types.public_key_type.PublicKeyType"]
    """<p>The public key (in plaintext). When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) of the KMS key that encrypted the private key.</p>"""
    key_pair_spec: NotRequired["capo_kms.types.data_key_pair_spec.DataKeyPairSpec"]
    """<p>The type of data key pair that was generated.</p>"""
    key_material_id: NotRequired["capo_kms.types.backing_key_id_type.BackingKeyIdType"]
    """<p>The identifier of the key material used to encrypt the private key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateDataKeyPairWithoutPlaintextResponse) -> dict:
    out: dict = {}
    if "private_key_ciphertext_blob" in value:
        import capo_kms.types.ciphertext_type

        out["PrivateKeyCiphertextBlob"] = (
            capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["private_key_ciphertext_blob"]
            )
        )
    if "public_key" in value:
        import capo_kms.types.public_key_type

        out["PublicKey"] = capo_kms.types.public_key_type.serialize_aws_json_1_1(
            value["public_key"]
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_pair_spec" in value:
        import capo_kms.types.data_key_pair_spec

        out["KeyPairSpec"] = capo_kms.types.data_key_pair_spec.serialize_aws_json_1_1(
            value["key_pair_spec"]
        )
    if "key_material_id" in value:
        out["KeyMaterialId"] = value["key_material_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateDataKeyPairWithoutPlaintextResponse:
    out: GenerateDataKeyPairWithoutPlaintextResponse = {}  # type: ignore[typeddict-item]
    if data.get("PrivateKeyCiphertextBlob") is not None:
        import capo_kms.types.ciphertext_type

        out["private_key_ciphertext_blob"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["PrivateKeyCiphertextBlob"]
            )
        )
    if data.get("PublicKey") is not None:
        import capo_kms.types.public_key_type

        out["public_key"] = capo_kms.types.public_key_type.deserialize_aws_json_1_1(
            data["PublicKey"]
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("KeyPairSpec") is not None:
        import capo_kms.types.data_key_pair_spec

        out["key_pair_spec"] = (
            capo_kms.types.data_key_pair_spec.deserialize_aws_json_1_1(
                data["KeyPairSpec"]
            )
        )
    if data.get("KeyMaterialId") is not None:
        out["key_material_id"] = data["KeyMaterialId"]
    return out
