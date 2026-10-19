"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeyAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_algorithm
    import capo_payment_cryptography.types.key_class
    import capo_payment_cryptography.types.key_modes_of_use
    import capo_payment_cryptography.types.key_usage


class KeyAttributes(TypedDict, closed=True):
    key_usage: "capo_payment_cryptography.types.key_usage.KeyUsage"
    """<p>The cryptographic usage of an Amazon Web Services Payment Cryptography key as deﬁned in section A.5.2 of the TR-31 spec.</p>"""
    key_class: "capo_payment_cryptography.types.key_class.KeyClass"
    """<p>The type of Amazon Web Services Payment Cryptography key to create, which determines the classiﬁcation of the cryptographic method and whether Amazon Web Services Payment Cryptography key contains a symmetric key or an asymmetric key pair.</p>"""
    key_algorithm: "capo_payment_cryptography.types.key_algorithm.KeyAlgorithm"
    """<p>The key algorithm to be use during creation of an Amazon Web Services Payment Cryptography key.</p> <p>For symmetric keys, Amazon Web Services Payment Cryptography supports <code>AES</code> and <code>TDES</code> algorithms. For asymmetric keys, Amazon Web Services Payment Cryptography supports <code>RSA</code> and <code>ECC_NIST</code> algorithms.</p>"""
    key_modes_of_use: "capo_payment_cryptography.types.key_modes_of_use.KeyModesOfUse"
    """<p>The list of cryptographic operations that you can perform using the key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyAttributes) -> dict:
    out: dict = {}
    out["KeyUsage"] = value["key_usage"]
    out["KeyClass"] = value["key_class"]
    out["KeyAlgorithm"] = value["key_algorithm"]
    import capo_payment_cryptography.types.key_modes_of_use

    out["KeyModesOfUse"] = (
        capo_payment_cryptography.types.key_modes_of_use.serialize_aws_json_1_0(
            value["key_modes_of_use"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyAttributes:
    out: KeyAttributes = {}  # type: ignore[typeddict-item]
    if data.get("KeyUsage") is not None:
        out["key_usage"] = data["KeyUsage"]
    else:
        out["key_usage"] = ""
    if data.get("KeyClass") is not None:
        out["key_class"] = data["KeyClass"]
    else:
        out["key_class"] = ""
    if data.get("KeyAlgorithm") is not None:
        out["key_algorithm"] = data["KeyAlgorithm"]
    else:
        out["key_algorithm"] = ""
    if data.get("KeyModesOfUse") is not None:
        import capo_payment_cryptography.types.key_modes_of_use

        out["key_modes_of_use"] = (
            capo_payment_cryptography.types.key_modes_of_use.deserialize_aws_json_1_0(
                data["KeyModesOfUse"]
            )
        )
    else:
        raise DeserializationError("KeyAttributes.key_modes_of_use required")
    return out
