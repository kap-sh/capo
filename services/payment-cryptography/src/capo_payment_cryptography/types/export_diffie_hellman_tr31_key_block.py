"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportDiffieHellmanTr31KeyBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_type
    import capo_payment_cryptography.types.diffie_hellman_derivation_data
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.key_block_headers
    import capo_payment_cryptography.types.key_derivation_function
    import capo_payment_cryptography.types.key_derivation_hash_algorithm
    import capo_payment_cryptography.types.symmetric_key_algorithm


class ExportDiffieHellmanTr31KeyBlock(TypedDict, closed=True):
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
    key_block_headers: NotRequired[
        "capo_payment_cryptography.types.key_block_headers.KeyBlockHeaders"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportDiffieHellmanTr31KeyBlock) -> dict:
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
    if "key_block_headers" in value:
        import capo_payment_cryptography.types.key_block_headers

        out["KeyBlockHeaders"] = (
            capo_payment_cryptography.types.key_block_headers.serialize_aws_json_1_0(
                value["key_block_headers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportDiffieHellmanTr31KeyBlock:
    out: ExportDiffieHellmanTr31KeyBlock = {}  # type: ignore[typeddict-item]
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
        import capo_payment_cryptography.types.symmetric_key_algorithm

        out["derive_key_algorithm"] = (
            capo_payment_cryptography.types.symmetric_key_algorithm.deserialize_aws_json_1_0(
                data["DeriveKeyAlgorithm"]
            )
        )
    else:
        import typing

        out["derive_key_algorithm"] = typing.cast(
            "capo_payment_cryptography.types.symmetric_key_algorithm.SymmetricKeyAlgorithm",
            "",
        )
    if data.get("KeyDerivationFunction") is not None:
        import capo_payment_cryptography.types.key_derivation_function

        out["key_derivation_function"] = (
            capo_payment_cryptography.types.key_derivation_function.deserialize_aws_json_1_0(
                data["KeyDerivationFunction"]
            )
        )
    else:
        import typing

        out["key_derivation_function"] = typing.cast(
            "capo_payment_cryptography.types.key_derivation_function.KeyDerivationFunction",
            "",
        )
    if data.get("KeyDerivationHashAlgorithm") is not None:
        import capo_payment_cryptography.types.key_derivation_hash_algorithm

        out["key_derivation_hash_algorithm"] = (
            capo_payment_cryptography.types.key_derivation_hash_algorithm.deserialize_aws_json_1_0(
                data["KeyDerivationHashAlgorithm"]
            )
        )
    else:
        import typing

        out["key_derivation_hash_algorithm"] = typing.cast(
            "capo_payment_cryptography.types.key_derivation_hash_algorithm.KeyDerivationHashAlgorithm",
            "",
        )
    if data.get("DerivationData") is not None:
        import capo_payment_cryptography.types.diffie_hellman_derivation_data

        out["derivation_data"] = (
            capo_payment_cryptography.types.diffie_hellman_derivation_data.deserialize_aws_json_1_0(
                data["DerivationData"]
            )
        )
    else:
        out["derivation_data"] = {"$unknown": {"name": ""}}
    if data.get("KeyBlockHeaders") is not None:
        import capo_payment_cryptography.types.key_block_headers

        out["key_block_headers"] = (
            capo_payment_cryptography.types.key_block_headers.deserialize_aws_json_1_0(
                data["KeyBlockHeaders"]
            )
        )
    return out


def redact_sensitive(value: ExportDiffieHellmanTr31KeyBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key_block_headers" in value:
        import capo_payment_cryptography.types.key_block_headers

        out["key_block_headers"] = (
            capo_payment_cryptography.types.key_block_headers.redact_sensitive(
                value["key_block_headers"]
            )
        )
    return out
