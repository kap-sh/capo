"""Generated from Smithy shape ``com.amazonaws.kms#SignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.ciphertext_type
    import capo_kms.types.key_id_type
    import capo_kms.types.signing_algorithm_spec


class SignResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) of the asymmetric KMS key that was used to sign the message.</p>"""
    signature: NotRequired["capo_kms.types.ciphertext_type.CiphertextType"]
    """<p>The cryptographic signature that was generated for the message. </p> <ul> <li> <p>When used with the supported RSA signing algorithms, the encoding of this value is defined by <a href="https://tools.ietf.org/html/rfc8017">PKCS #1 in RFC 8017</a>.</p> </li> <li> <p>When used with the <code>ECDSA_SHA_256</code>, <code>ECDSA_SHA_384</code>, or <code>ECDSA_SHA_512</code> signing algorithms, this value is a DER-encoded object as defined by ANSI X9.62–2005 and <a href="https://tools.ietf.org/html/rfc3279#section-2.2.3">RFC 3279 Section 2.2.3</a>. This is the most commonly used signature format and is appropriate for most uses. </p> </li> </ul> <p>When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    signing_algorithm: NotRequired[
        "capo_kms.types.signing_algorithm_spec.SigningAlgorithmSpec"
    ]
    """<p>The signing algorithm that was used to sign the message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "signature" in value:
        import capo_kms.types.ciphertext_type

        out["Signature"] = capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
            value["signature"]
        )
    if "signing_algorithm" in value:
        import capo_kms.types.signing_algorithm_spec

        out["SigningAlgorithm"] = (
            capo_kms.types.signing_algorithm_spec.serialize_aws_json_1_1(
                value["signing_algorithm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SignResponse:
    out: SignResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("Signature") is not None:
        import capo_kms.types.ciphertext_type

        out["signature"] = capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
            data["Signature"]
        )
    if data.get("SigningAlgorithm") is not None:
        import capo_kms.types.signing_algorithm_spec

        out["signing_algorithm"] = (
            capo_kms.types.signing_algorithm_spec.deserialize_aws_json_1_1(
                data["SigningAlgorithm"]
            )
        )
    return out
