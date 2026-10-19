"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EcdhDerivationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.certificate_type
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.key_derivation_function
    import capo_payment_cryptography_data.types.key_derivation_hash_algorithm
    import capo_payment_cryptography_data.types.shared_information
    import capo_payment_cryptography_data.types.symmetric_key_algorithm


class EcdhDerivationAttributes(TypedDict, closed=True):
    certificate_authority_public_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyArn</code> of the certificate that signed the client's <code>PublicKeyCertificate</code>.</p>"""
    public_key_certificate: (
        "capo_payment_cryptography_data.types.certificate_type.CertificateType"
    )
    """<p>The client's public key certificate in PEM format (base64 encoded) to use for ECDH key derivation.</p>"""
    key_algorithm: "capo_payment_cryptography_data.types.symmetric_key_algorithm.SymmetricKeyAlgorithm"
    """<p>The key algorithm of the derived ECDH key.</p>"""
    key_derivation_function: "capo_payment_cryptography_data.types.key_derivation_function.KeyDerivationFunction"
    """<p>The key derivation function to use for deriving a key using ECDH.</p>"""
    key_derivation_hash_algorithm: "capo_payment_cryptography_data.types.key_derivation_hash_algorithm.KeyDerivationHashAlgorithm"
    """<p>The hash type to use for deriving a key using ECDH.</p>"""
    shared_information: (
        "capo_payment_cryptography_data.types.shared_information.SharedInformation"
    )
    """<p>A byte string containing information that binds the ECDH derived key to the two parties involved or to the context of the key.</p> <p>It may include details like identities of the two parties deriving the key, context of the operation, session IDs, and optionally a nonce. It must not contain zero bytes, and re-using shared information for multiple ECDH key derivations is not recommended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcdhDerivationAttributes) -> dict:
    out: dict = {}
    out["CertificateAuthorityPublicKeyIdentifier"] = value[
        "certificate_authority_public_key_identifier"
    ]
    out["PublicKeyCertificate"] = value["public_key_certificate"]
    import capo_payment_cryptography_data.types.symmetric_key_algorithm

    out["KeyAlgorithm"] = (
        capo_payment_cryptography_data.types.symmetric_key_algorithm.serialize_json(
            value["key_algorithm"]
        )
    )
    import capo_payment_cryptography_data.types.key_derivation_function

    out["KeyDerivationFunction"] = (
        capo_payment_cryptography_data.types.key_derivation_function.serialize_json(
            value["key_derivation_function"]
        )
    )
    import capo_payment_cryptography_data.types.key_derivation_hash_algorithm

    out["KeyDerivationHashAlgorithm"] = (
        capo_payment_cryptography_data.types.key_derivation_hash_algorithm.serialize_json(
            value["key_derivation_hash_algorithm"]
        )
    )
    out["SharedInformation"] = value["shared_information"]
    return out


def deserialize_json(data: dict) -> EcdhDerivationAttributes:
    out: EcdhDerivationAttributes = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityPublicKeyIdentifier") is not None:
        out["certificate_authority_public_key_identifier"] = data[
            "CertificateAuthorityPublicKeyIdentifier"
        ]
    else:
        out["certificate_authority_public_key_identifier"] = ""
    if data.get("PublicKeyCertificate") is not None:
        out["public_key_certificate"] = data["PublicKeyCertificate"]
    else:
        out["public_key_certificate"] = ""
    if data.get("KeyAlgorithm") is not None:
        import capo_payment_cryptography_data.types.symmetric_key_algorithm

        out["key_algorithm"] = (
            capo_payment_cryptography_data.types.symmetric_key_algorithm.deserialize_json(
                data["KeyAlgorithm"]
            )
        )
    else:
        import typing

        out["key_algorithm"] = typing.cast(
            "capo_payment_cryptography_data.types.symmetric_key_algorithm.SymmetricKeyAlgorithm",
            "",
        )
    if data.get("KeyDerivationFunction") is not None:
        import capo_payment_cryptography_data.types.key_derivation_function

        out["key_derivation_function"] = (
            capo_payment_cryptography_data.types.key_derivation_function.deserialize_json(
                data["KeyDerivationFunction"]
            )
        )
    else:
        import typing

        out["key_derivation_function"] = typing.cast(
            "capo_payment_cryptography_data.types.key_derivation_function.KeyDerivationFunction",
            "",
        )
    if data.get("KeyDerivationHashAlgorithm") is not None:
        import capo_payment_cryptography_data.types.key_derivation_hash_algorithm

        out["key_derivation_hash_algorithm"] = (
            capo_payment_cryptography_data.types.key_derivation_hash_algorithm.deserialize_json(
                data["KeyDerivationHashAlgorithm"]
            )
        )
    else:
        import typing

        out["key_derivation_hash_algorithm"] = typing.cast(
            "capo_payment_cryptography_data.types.key_derivation_hash_algorithm.KeyDerivationHashAlgorithm",
            "",
        )
    if data.get("SharedInformation") is not None:
        out["shared_information"] = data["SharedInformation"]
    else:
        out["shared_information"] = ""
    return out
