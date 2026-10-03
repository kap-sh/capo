"""Generated from Smithy shape ``com.amazonaws.kms#GenerateDataKeyPairResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.backing_key_id_type
    import capo_kms.types.ciphertext_type
    import capo_kms.types.data_key_pair_spec
    import capo_kms.types.key_id_type
    import capo_kms.types.plaintext_type
    import capo_kms.types.public_key_type


class GenerateDataKeyPairResponse(TypedDict, closed=True):
    private_key_ciphertext_blob: NotRequired[
        "capo_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The encrypted copy of the private key. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    private_key_plaintext: NotRequired["capo_kms.types.plaintext_type.PlaintextType"]
    """<p>The plaintext copy of the private key. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p> <p>If the response includes the <code>CiphertextForRecipient</code> field, the <code>PrivateKeyPlaintext</code> field is null or empty.</p>"""
    public_key: NotRequired["capo_kms.types.public_key_type.PublicKeyType"]
    """<p>The public key (in plaintext). When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) of the KMS key that encrypted the private key.</p>"""
    key_pair_spec: NotRequired["capo_kms.types.data_key_pair_spec.DataKeyPairSpec"]
    """<p>The type of data key pair that was generated.</p>"""
    ciphertext_for_recipient: NotRequired[
        "capo_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The plaintext private data key encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment. </p> <p>This field is included in the response only when the <code>Recipient</code> parameter in the request includes a valid attestation document from an Amazon Web Services Nitro enclave or NitroTPM. For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    key_material_id: NotRequired["capo_kms.types.backing_key_id_type.BackingKeyIdType"]
    """<p>The identifier of the key material used to encrypt the private key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateDataKeyPairResponse) -> dict:
    out: dict = {}
    if "private_key_ciphertext_blob" in value:
        import capo_kms.types.ciphertext_type

        out["PrivateKeyCiphertextBlob"] = (
            capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["private_key_ciphertext_blob"]
            )
        )
    if "private_key_plaintext" in value:
        import capo_kms.types.plaintext_type

        out["PrivateKeyPlaintext"] = (
            capo_kms.types.plaintext_type.serialize_aws_json_1_1(
                value["private_key_plaintext"]
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
    if "ciphertext_for_recipient" in value:
        import capo_kms.types.ciphertext_type

        out["CiphertextForRecipient"] = (
            capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["ciphertext_for_recipient"]
            )
        )
    if "key_material_id" in value:
        out["KeyMaterialId"] = value["key_material_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateDataKeyPairResponse:
    out: GenerateDataKeyPairResponse = {}  # type: ignore[typeddict-item]
    if data.get("PrivateKeyCiphertextBlob") is not None:
        import capo_kms.types.ciphertext_type

        out["private_key_ciphertext_blob"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["PrivateKeyCiphertextBlob"]
            )
        )
    if data.get("PrivateKeyPlaintext") is not None:
        import capo_kms.types.plaintext_type

        out["private_key_plaintext"] = (
            capo_kms.types.plaintext_type.deserialize_aws_json_1_1(
                data["PrivateKeyPlaintext"]
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
    if data.get("CiphertextForRecipient") is not None:
        import capo_kms.types.ciphertext_type

        out["ciphertext_for_recipient"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextForRecipient"]
            )
        )
    if data.get("KeyMaterialId") is not None:
        out["key_material_id"] = data["KeyMaterialId"]
    return out
