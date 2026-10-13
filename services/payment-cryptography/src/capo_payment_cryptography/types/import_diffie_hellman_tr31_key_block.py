"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ImportDiffieHellmanTr31KeyBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_type
    import capo_payment_cryptography.types.diffie_hellman_derivation_data
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.key_derivation_function
    import capo_payment_cryptography.types.key_derivation_hash_algorithm
    import capo_payment_cryptography.types.symmetric_key_algorithm
    import capo_payment_cryptography.types.tr31_wrapped_key_block


class ImportDiffieHellmanTr31KeyBlock(TypedDict, closed=True):
    private_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The <code>keyARN</code> of the asymmetric ECC key created within Amazon Web Services Payment Cryptography.</p>"""
    certificate_authority_public_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The <code>keyARN</code> of the CA that signed the <code>PublicKeyCertificate</code> for the client's receiving ECC key pair.</p>"""
    public_key_certificate: (
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The public key certificate of the client's receiving ECC key pair, in PEM format (base64 encoded), to use for ECDH key derivation.</p>"""
    derive_key_algorithm: (
        "capo_payment_cryptography.types.symmetric_key_algorithm.SymmetricKeyAlgorithm"
    )
    """<p>The key algorithm of the shared derived ECDH key.</p>"""
    key_derivation_function: (
        "capo_payment_cryptography.types.key_derivation_function.KeyDerivationFunction"
    )
    """<p>The key derivation function to use when deriving a key using ECDH.</p>"""
    key_derivation_hash_algorithm: "capo_payment_cryptography.types.key_derivation_hash_algorithm.KeyDerivationHashAlgorithm"
    """<p>The hash type to use when deriving a key using ECDH.</p>"""
    derivation_data: "capo_payment_cryptography.types.diffie_hellman_derivation_data.DiffieHellmanDerivationData"
    """<p>The shared information used when deriving a key using ECDH.</p>"""
    wrapped_key_block: (
        "capo_payment_cryptography.types.tr31_wrapped_key_block.Tr31WrappedKeyBlock"
    )
    """<p>The ECDH wrapped key block to import.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportDiffieHellmanTr31KeyBlock) -> dict:
    out: dict = {}
    out["PrivateKeyIdentifier"] = value["private_key_identifier"]
    out["CertificateAuthorityPublicKeyIdentifier"] = value[
        "certificate_authority_public_key_identifier"
    ]
    out["PublicKeyCertificate"] = value["public_key_certificate"]
    import capo_payment_cryptography.types.symmetric_key_algorithm

    out["DeriveKeyAlgorithm"] = (
        capo_payment_cryptography.types.symmetric_key_algorithm.serialize_aws_json_1_0(
            value["derive_key_algorithm"]
        )
    )
    import capo_payment_cryptography.types.key_derivation_function

    out["KeyDerivationFunction"] = (
        capo_payment_cryptography.types.key_derivation_function.serialize_aws_json_1_0(
            value["key_derivation_function"]
        )
    )
    import capo_payment_cryptography.types.key_derivation_hash_algorithm

    out["KeyDerivationHashAlgorithm"] = (
        capo_payment_cryptography.types.key_derivation_hash_algorithm.serialize_aws_json_1_0(
            value["key_derivation_hash_algorithm"]
        )
    )
    import capo_payment_cryptography.types.diffie_hellman_derivation_data

    out["DerivationData"] = (
        capo_payment_cryptography.types.diffie_hellman_derivation_data.serialize_aws_json_1_0(
            value["derivation_data"]
        )
    )
    out["WrappedKeyBlock"] = value["wrapped_key_block"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportDiffieHellmanTr31KeyBlock:
    out: ImportDiffieHellmanTr31KeyBlock = {}  # type: ignore[typeddict-item]
    if data.get("PrivateKeyIdentifier") is not None:
        out["private_key_identifier"] = data["PrivateKeyIdentifier"]
    else:
        raise DeserializationError(
            "ImportDiffieHellmanTr31KeyBlock.private_key_identifier required"
        )
    if data.get("CertificateAuthorityPublicKeyIdentifier") is not None:
        out["certificate_authority_public_key_identifier"] = data[
            "CertificateAuthorityPublicKeyIdentifier"
        ]
    else:
        raise DeserializationError(
            "ImportDiffieHellmanTr31KeyBlock.certificate_authority_public_key_identifier required"
        )
    if data.get("PublicKeyCertificate") is not None:
        out["public_key_certificate"] = data["PublicKeyCertificate"]
    else:
        raise DeserializationError(
            "ImportDiffieHellmanTr31KeyBlock.public_key_certificate required"
        )
    if data.get("DeriveKeyAlgorithm") is not None:
        import capo_payment_cryptography.types.symmetric_key_algorithm

        out["derive_key_algorithm"] = (
            capo_payment_cryptography.types.symmetric_key_algorithm.deserialize_aws_json_1_0(
                data["DeriveKeyAlgorithm"]
            )
        )
    else:
        raise DeserializationError(
            "ImportDiffieHellmanTr31KeyBlock.derive_key_algorithm required"
        )
    if data.get("KeyDerivationFunction") is not None:
        import capo_payment_cryptography.types.key_derivation_function

        out["key_derivation_function"] = (
            capo_payment_cryptography.types.key_derivation_function.deserialize_aws_json_1_0(
                data["KeyDerivationFunction"]
            )
        )
    else:
        raise DeserializationError(
            "ImportDiffieHellmanTr31KeyBlock.key_derivation_function required"
        )
    if data.get("KeyDerivationHashAlgorithm") is not None:
        import capo_payment_cryptography.types.key_derivation_hash_algorithm

        out["key_derivation_hash_algorithm"] = (
            capo_payment_cryptography.types.key_derivation_hash_algorithm.deserialize_aws_json_1_0(
                data["KeyDerivationHashAlgorithm"]
            )
        )
    else:
        raise DeserializationError(
            "ImportDiffieHellmanTr31KeyBlock.key_derivation_hash_algorithm required"
        )
    if data.get("DerivationData") is not None:
        import capo_payment_cryptography.types.diffie_hellman_derivation_data

        out["derivation_data"] = (
            capo_payment_cryptography.types.diffie_hellman_derivation_data.deserialize_aws_json_1_0(
                data["DerivationData"]
            )
        )
    else:
        raise DeserializationError(
            "ImportDiffieHellmanTr31KeyBlock.derivation_data required"
        )
    if data.get("WrappedKeyBlock") is not None:
        out["wrapped_key_block"] = data["WrappedKeyBlock"]
    else:
        raise DeserializationError(
            "ImportDiffieHellmanTr31KeyBlock.wrapped_key_block required"
        )
    return out


def redact_sensitive(value: ImportDiffieHellmanTr31KeyBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "wrapped_key_block" in value:
        out["wrapped_key_block"] = "*** Sensitive Data Redacted ***"
    return out
