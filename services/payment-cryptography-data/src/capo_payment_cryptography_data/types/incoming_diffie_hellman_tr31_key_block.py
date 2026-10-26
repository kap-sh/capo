"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#IncomingDiffieHellmanTr31KeyBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.certificate_type
    import capo_payment_cryptography_data.types.diffie_hellman_derivation_data
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.key_derivation_function
    import capo_payment_cryptography_data.types.key_derivation_hash_algorithm
    import capo_payment_cryptography_data.types.symmetric_key_algorithm
    import capo_payment_cryptography_data.types.tr31_wrapped_key_block


class IncomingDiffieHellmanTr31KeyBlock(TypedDict, closed=True):
    private_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the asymmetric ECC key pair.</p>"""
    certificate_authority_public_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyArn</code> of the certificate that signed the client's <code>PublicKeyCertificate</code>.</p>"""
    public_key_certificate: (
        "capo_payment_cryptography_data.types.certificate_type.CertificateType"
    )
    """<p>The client's public key certificate in PEM format (base64 encoded) to use for ECDH key derivation.</p>"""
    derive_key_algorithm: "capo_payment_cryptography_data.types.symmetric_key_algorithm.SymmetricKeyAlgorithm"
    """<p>The key algorithm of the derived ECDH key.</p>"""
    key_derivation_function: "capo_payment_cryptography_data.types.key_derivation_function.KeyDerivationFunction"
    """<p>The key derivation function to use for deriving a key using ECDH.</p>"""
    key_derivation_hash_algorithm: "capo_payment_cryptography_data.types.key_derivation_hash_algorithm.KeyDerivationHashAlgorithm"
    """<p>The hash type to use for deriving a key using ECDH.</p>"""
    derivation_data: "capo_payment_cryptography_data.types.diffie_hellman_derivation_data.DiffieHellmanDerivationData"
    wrapped_key_block: "capo_payment_cryptography_data.types.tr31_wrapped_key_block.Tr31WrappedKeyBlock"
    """<p>The WrappedKeyBlock containing the transaction key wrapped using an ECDH dervied key. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncomingDiffieHellmanTr31KeyBlock) -> dict:
    out: dict = {}
    out["PrivateKeyIdentifier"] = value["private_key_identifier"]
    out["CertificateAuthorityPublicKeyIdentifier"] = value[
        "certificate_authority_public_key_identifier"
    ]
    out["PublicKeyCertificate"] = value["public_key_certificate"]
    import capo_payment_cryptography_data.types.symmetric_key_algorithm

    out["DeriveKeyAlgorithm"] = (
        capo_payment_cryptography_data.types.symmetric_key_algorithm.serialize_json(
            value["derive_key_algorithm"]
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
    import capo_payment_cryptography_data.types.diffie_hellman_derivation_data

    out["DerivationData"] = (
        capo_payment_cryptography_data.types.diffie_hellman_derivation_data.serialize_json(
            value["derivation_data"]
        )
    )
    out["WrappedKeyBlock"] = value["wrapped_key_block"]
    return out


def deserialize_json(data: dict) -> IncomingDiffieHellmanTr31KeyBlock:
    out: IncomingDiffieHellmanTr31KeyBlock = {}  # type: ignore[typeddict-item]
    if data.get("PrivateKeyIdentifier") is not None:
        out["private_key_identifier"] = data["PrivateKeyIdentifier"]
    else:
        out["private_key_identifier"] = ""
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
    if data.get("DeriveKeyAlgorithm") is not None:
        import capo_payment_cryptography_data.types.symmetric_key_algorithm

        out["derive_key_algorithm"] = (
            capo_payment_cryptography_data.types.symmetric_key_algorithm.deserialize_json(
                data["DeriveKeyAlgorithm"]
            )
        )
    else:
        import typing

        out["derive_key_algorithm"] = typing.cast(
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
    if data.get("DerivationData") is not None:
        import capo_payment_cryptography_data.types.diffie_hellman_derivation_data

        out["derivation_data"] = (
            capo_payment_cryptography_data.types.diffie_hellman_derivation_data.deserialize_json(
                data["DerivationData"]
            )
        )
    else:
        out["derivation_data"] = {"$unknown": {"name": ""}}
    if data.get("WrappedKeyBlock") is not None:
        out["wrapped_key_block"] = data["WrappedKeyBlock"]
    else:
        out["wrapped_key_block"] = ""
    return out


def redact_sensitive(value: IncomingDiffieHellmanTr31KeyBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "wrapped_key_block" in value:
        out["wrapped_key_block"] = "*** Sensitive Data Redacted ***"
    return out
