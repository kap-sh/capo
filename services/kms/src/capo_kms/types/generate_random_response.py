"""Generated from Smithy shape ``com.amazonaws.kms#GenerateRandomResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.ciphertext_type
    import capo_kms.types.plaintext_type


class GenerateRandomResponse(TypedDict, closed=True):
    plaintext: NotRequired["capo_kms.types.plaintext_type.PlaintextType"]
    """<p>The random byte string. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p> <p>If the response includes the <code>CiphertextForRecipient</code> field, the <code>Plaintext</code> field is null or empty.</p>"""
    ciphertext_for_recipient: NotRequired[
        "capo_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The plaintext random bytes encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment. </p> <p>This field is included in the response only when the <code>Recipient</code> parameter in the request includes a valid attestation document from an Amazon Web Services Nitro enclave or NitroTPM. For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateRandomResponse) -> dict:
    out: dict = {}
    if "plaintext" in value:
        import capo_kms.types.plaintext_type

        out["Plaintext"] = capo_kms.types.plaintext_type.serialize_aws_json_1_1(
            value["plaintext"]
        )
    if "ciphertext_for_recipient" in value:
        import capo_kms.types.ciphertext_type

        out["CiphertextForRecipient"] = (
            capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["ciphertext_for_recipient"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateRandomResponse:
    out: GenerateRandomResponse = {}  # type: ignore[typeddict-item]
    if data.get("Plaintext") is not None:
        import capo_kms.types.plaintext_type

        out["plaintext"] = capo_kms.types.plaintext_type.deserialize_aws_json_1_1(
            data["Plaintext"]
        )
    if data.get("CiphertextForRecipient") is not None:
        import capo_kms.types.ciphertext_type

        out["ciphertext_for_recipient"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextForRecipient"]
            )
        )
    return out
