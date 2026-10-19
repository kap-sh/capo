"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ImportTr34KeyBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_type
    import capo_payment_cryptography.types.even_hex_length_between16_and32
    import capo_payment_cryptography.types.import_token_id
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.tr34_key_block_format
    import capo_payment_cryptography.types.tr34_wrapped_key_block


class ImportTr34KeyBlock(TypedDict, closed=True):
    certificate_authority_public_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The <code>KeyARN</code> of the certificate chain that signs the signing key certificate during TR-34 key import.</p>"""
    signing_key_certificate: (
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The public key component in PEM certificate format of the private key that signs the KDH TR-34 WrappedKeyBlock.</p>"""
    import_token: "capo_payment_cryptography.types.import_token_id.ImportTokenId"
    """<p>The import token that initiates key import using the asymmetric TR-34 key exchange method into Amazon Web Services Payment Cryptography. It expires after 30 days. You can use the same import token to import multiple keys to the same service account.</p>"""
    wrapping_key_identifier: NotRequired[
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    ]
    """<p>Key Identifier used for unwrapping the import key</p>"""
    wrapping_key_certificate: NotRequired[
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    ]
    """<p>The certificate used to wrap the TR-34 key block.</p>"""
    wrapped_key_block: (
        "capo_payment_cryptography.types.tr34_wrapped_key_block.Tr34WrappedKeyBlock"
    )
    """<p>The TR-34 wrapped key block to import.</p>"""
    key_block_format: (
        "capo_payment_cryptography.types.tr34_key_block_format.Tr34KeyBlockFormat"
    )
    """<p>The key block format to use during key import. The only value allowed is <code>X9_TR34_2012</code>.</p>"""
    random_nonce: NotRequired[
        "capo_payment_cryptography.types.even_hex_length_between16_and32.EvenHexLengthBetween16And32"
    ]
    """<p>A random number value that is unique to the TR-34 key block generated using 2 pass. The operation will fail, if a random nonce value is not provided for a TR-34 key block generated using 2 pass.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportTr34KeyBlock) -> dict:
    out: dict = {}
    out["CertificateAuthorityPublicKeyIdentifier"] = value[
        "certificate_authority_public_key_identifier"
    ]
    out["SigningKeyCertificate"] = value["signing_key_certificate"]
    out["ImportToken"] = value.get("import_token", "")
    if "wrapping_key_identifier" in value:
        out["WrappingKeyIdentifier"] = value["wrapping_key_identifier"]
    if "wrapping_key_certificate" in value:
        out["WrappingKeyCertificate"] = value["wrapping_key_certificate"]
    out["WrappedKeyBlock"] = value["wrapped_key_block"]
    out["KeyBlockFormat"] = value["key_block_format"]
    if "random_nonce" in value:
        out["RandomNonce"] = value["random_nonce"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportTr34KeyBlock:
    out: ImportTr34KeyBlock = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityPublicKeyIdentifier") is not None:
        out["certificate_authority_public_key_identifier"] = data[
            "CertificateAuthorityPublicKeyIdentifier"
        ]
    else:
        out["certificate_authority_public_key_identifier"] = ""
    if data.get("SigningKeyCertificate") is not None:
        out["signing_key_certificate"] = data["SigningKeyCertificate"]
    else:
        out["signing_key_certificate"] = ""
    if data.get("ImportToken") is not None:
        out["import_token"] = data["ImportToken"]
    else:
        out["import_token"] = ""
    if data.get("WrappingKeyIdentifier") is not None:
        out["wrapping_key_identifier"] = data["WrappingKeyIdentifier"]
    if data.get("WrappingKeyCertificate") is not None:
        out["wrapping_key_certificate"] = data["WrappingKeyCertificate"]
    if data.get("WrappedKeyBlock") is not None:
        out["wrapped_key_block"] = data["WrappedKeyBlock"]
    else:
        out["wrapped_key_block"] = ""
    if data.get("KeyBlockFormat") is not None:
        out["key_block_format"] = data["KeyBlockFormat"]
    else:
        out["key_block_format"] = ""
    if data.get("RandomNonce") is not None:
        out["random_nonce"] = data["RandomNonce"]
    return out


def redact_sensitive(value: ImportTr34KeyBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "wrapped_key_block" in value:
        out["wrapped_key_block"] = "*** Sensitive Data Redacted ***"
    return out
