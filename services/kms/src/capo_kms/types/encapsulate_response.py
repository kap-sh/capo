"""Generated from Smithy shape ``com.amazonaws.kms#EncapsulateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.ciphertext_type
    import capo_kms.types.encapsulation_algorithm_spec
    import capo_kms.types.key_id_type
    import capo_kms.types.plaintext_type


class EncapsulateResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The identifier of the ML-KEM KMS key used to encapsulate the shared secret.</p>"""
    shared_secret: NotRequired["capo_kms.types.plaintext_type.PlaintextType"]
    """<p>The plaintext shared secret. It is a 32-byte cryptographically random value that both parties can use directly as key material or pass through a key derivation function to generate multiple keys and nonces. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    shared_secret_ciphertext_blob: NotRequired[
        "capo_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The encapsulated form of the shared secret. Pass this value to the <a>Decapsulate</a> operation to recover the shared secret. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded. The length of <code>SharedSecretCiphertextBlob</code> depends on the ML-KEM key spec. Before Base64 encoding, the encapsulated shared secret is 768 bytes for <code>ML_KEM_512</code>, 1088 bytes for <code>ML_KEM_768</code>, and 1568 bytes for <code>ML_KEM_1024</code>. </p>"""
    encapsulation_algorithm: NotRequired[
        "capo_kms.types.encapsulation_algorithm_spec.EncapsulationAlgorithmSpec"
    ]
    """<p>The key encapsulation algorithm used to generate the shared secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncapsulateResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "shared_secret" in value:
        import capo_kms.types.plaintext_type

        out["SharedSecret"] = capo_kms.types.plaintext_type.serialize_aws_json_1_1(
            value["shared_secret"]
        )
    if "shared_secret_ciphertext_blob" in value:
        import capo_kms.types.ciphertext_type

        out["SharedSecretCiphertextBlob"] = (
            capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["shared_secret_ciphertext_blob"]
            )
        )
    if "encapsulation_algorithm" in value:
        import capo_kms.types.encapsulation_algorithm_spec

        out["EncapsulationAlgorithm"] = (
            capo_kms.types.encapsulation_algorithm_spec.serialize_aws_json_1_1(
                value["encapsulation_algorithm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EncapsulateResponse:
    out: EncapsulateResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("SharedSecret") is not None:
        import capo_kms.types.plaintext_type

        out["shared_secret"] = capo_kms.types.plaintext_type.deserialize_aws_json_1_1(
            data["SharedSecret"]
        )
    if data.get("SharedSecretCiphertextBlob") is not None:
        import capo_kms.types.ciphertext_type

        out["shared_secret_ciphertext_blob"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["SharedSecretCiphertextBlob"]
            )
        )
    if data.get("EncapsulationAlgorithm") is not None:
        import capo_kms.types.encapsulation_algorithm_spec

        out["encapsulation_algorithm"] = (
            capo_kms.types.encapsulation_algorithm_spec.deserialize_aws_json_1_1(
                data["EncapsulationAlgorithm"]
            )
        )
    return out


def redact_sensitive(value: EncapsulateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "shared_secret" in value:
        out["shared_secret"] = "*** Sensitive Data Redacted ***"
    return out
