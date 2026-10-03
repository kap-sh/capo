"""Generated from Smithy shape ``com.amazonaws.kms#GenerateDataKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.backing_key_id_type
    import capo_kms.types.ciphertext_type
    import capo_kms.types.key_id_type
    import capo_kms.types.plaintext_type


class GenerateDataKeyResponse(TypedDict, closed=True):
    ciphertext_blob: NotRequired["capo_kms.types.ciphertext_type.CiphertextType"]
    """<p>The encrypted copy of the data key. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    plaintext: NotRequired["capo_kms.types.plaintext_type.PlaintextType"]
    """<p>The plaintext data key. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded. Use this data key to encrypt your data outside of KMS. Then, remove it from memory as soon as possible.</p> <p>If the response includes the <code>CiphertextForRecipient</code> field, the <code>Plaintext</code> field is null or empty.</p>"""
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) of the KMS key that encrypted the data key.</p>"""
    ciphertext_for_recipient: NotRequired[
        "capo_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The plaintext data key encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment. </p> <p>This field is included in the response only when the <code>Recipient</code> parameter in the request includes a valid attestation document from an Amazon Web Services Nitro enclave or NitroTPM. For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    key_material_id: NotRequired["capo_kms.types.backing_key_id_type.BackingKeyIdType"]
    """<p>The identifier of the key material used to encrypt the data key. This field is omitted if the request includes the <code>Recipient</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateDataKeyResponse) -> dict:
    out: dict = {}
    if "ciphertext_blob" in value:
        import capo_kms.types.ciphertext_type

        out["CiphertextBlob"] = capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
            value["ciphertext_blob"]
        )
    if "plaintext" in value:
        import capo_kms.types.plaintext_type

        out["Plaintext"] = capo_kms.types.plaintext_type.serialize_aws_json_1_1(
            value["plaintext"]
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
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


def deserialize_aws_json_1_1(data: dict) -> GenerateDataKeyResponse:
    out: GenerateDataKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("CiphertextBlob") is not None:
        import capo_kms.types.ciphertext_type

        out["ciphertext_blob"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextBlob"]
            )
        )
    if data.get("Plaintext") is not None:
        import capo_kms.types.plaintext_type

        out["plaintext"] = capo_kms.types.plaintext_type.deserialize_aws_json_1_1(
            data["Plaintext"]
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
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
