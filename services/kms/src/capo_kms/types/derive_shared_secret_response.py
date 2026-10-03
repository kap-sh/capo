"""Generated from Smithy shape ``com.amazonaws.kms#DeriveSharedSecretResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.ciphertext_type
    import capo_kms.types.key_agreement_algorithm_spec
    import capo_kms.types.key_id_type
    import capo_kms.types.origin_type
    import capo_kms.types.plaintext_type


class DeriveSharedSecretResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>Identifies the KMS key used to derive the shared secret.</p>"""
    shared_secret: NotRequired["capo_kms.types.plaintext_type.PlaintextType"]
    """<p>The raw secret derived from the specified key agreement algorithm, private key in the asymmetric KMS key, and your peer's public key.</p> <p>If the response includes the <code>CiphertextForRecipient</code> field, the <code>SharedSecret</code> field is null or empty.</p>"""
    ciphertext_for_recipient: NotRequired[
        "capo_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The plaintext shared secret encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment. </p> <p>This field is included in the response only when the <code>Recipient</code> parameter in the request includes a valid attestation document from an Amazon Web Services Nitro enclave or NitroTPM. For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    key_agreement_algorithm: NotRequired[
        "capo_kms.types.key_agreement_algorithm_spec.KeyAgreementAlgorithmSpec"
    ]
    """<p>Identifies the key agreement algorithm used to derive the shared secret.</p>"""
    key_origin: NotRequired["capo_kms.types.origin_type.OriginType"]
    """<p>The source of the key material for the specified KMS key.</p> <p>When this value is <code>AWS_KMS</code>, KMS created the key material. When this value is <code>EXTERNAL</code>, the key material was imported or the KMS key doesn't have any key material.</p> <p>The only valid values for DeriveSharedSecret are <code>AWS_KMS</code> and <code>EXTERNAL</code>. DeriveSharedSecret does not support KMS keys with a <code>KeyOrigin</code> value of <code>AWS_CLOUDHSM</code> or <code>EXTERNAL_KEY_STORE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeriveSharedSecretResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "shared_secret" in value:
        import capo_kms.types.plaintext_type

        out["SharedSecret"] = capo_kms.types.plaintext_type.serialize_aws_json_1_1(
            value["shared_secret"]
        )
    if "ciphertext_for_recipient" in value:
        import capo_kms.types.ciphertext_type

        out["CiphertextForRecipient"] = (
            capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["ciphertext_for_recipient"]
            )
        )
    if "key_agreement_algorithm" in value:
        import capo_kms.types.key_agreement_algorithm_spec

        out["KeyAgreementAlgorithm"] = (
            capo_kms.types.key_agreement_algorithm_spec.serialize_aws_json_1_1(
                value["key_agreement_algorithm"]
            )
        )
    if "key_origin" in value:
        import capo_kms.types.origin_type

        out["KeyOrigin"] = capo_kms.types.origin_type.serialize_aws_json_1_1(
            value["key_origin"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeriveSharedSecretResponse:
    out: DeriveSharedSecretResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("SharedSecret") is not None:
        import capo_kms.types.plaintext_type

        out["shared_secret"] = capo_kms.types.plaintext_type.deserialize_aws_json_1_1(
            data["SharedSecret"]
        )
    if data.get("CiphertextForRecipient") is not None:
        import capo_kms.types.ciphertext_type

        out["ciphertext_for_recipient"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextForRecipient"]
            )
        )
    if data.get("KeyAgreementAlgorithm") is not None:
        import capo_kms.types.key_agreement_algorithm_spec

        out["key_agreement_algorithm"] = (
            capo_kms.types.key_agreement_algorithm_spec.deserialize_aws_json_1_1(
                data["KeyAgreementAlgorithm"]
            )
        )
    if data.get("KeyOrigin") is not None:
        import capo_kms.types.origin_type

        out["key_origin"] = capo_kms.types.origin_type.deserialize_aws_json_1_1(
            data["KeyOrigin"]
        )
    return out
