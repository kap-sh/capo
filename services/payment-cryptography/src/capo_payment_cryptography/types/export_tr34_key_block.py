"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportTr34KeyBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_type
    import capo_payment_cryptography.types.even_hex_length_between16_and32
    import capo_payment_cryptography.types.export_token_id
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.key_block_headers
    import capo_payment_cryptography.types.tr34_key_block_format


class ExportTr34KeyBlock(TypedDict, closed=True):
    certificate_authority_public_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The <code>KeyARN</code> of the certificate chain that signs the wrapping key certificate during TR-34 key export.</p>"""
    wrapping_key_certificate: (
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The <code>KeyARN</code> of the wrapping key certificate. Amazon Web Services Payment Cryptography uses this certificate to wrap the key under export.</p>"""
    export_token: "capo_payment_cryptography.types.export_token_id.ExportTokenId"
    """<p>The export token to initiate key export from Amazon Web Services Payment Cryptography. It also contains the signing key certificate that will sign the wrapped key during TR-34 key block generation. Call <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html">GetParametersForExport</a> to receive an export token. It expires after 30 days. You can use the same export token to export multiple keys from the same service account.</p>"""
    signing_key_identifier: NotRequired[
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    ]
    """<p>Key Identifier used for signing the export key</p>"""
    signing_key_certificate: NotRequired[
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    ]
    """<p>The certificate used to sign the TR-34 key block.</p>"""
    key_block_format: (
        "capo_payment_cryptography.types.tr34_key_block_format.Tr34KeyBlockFormat"
    )
    """<p>The format of key block that Amazon Web Services Payment Cryptography will use during key export.</p>"""
    random_nonce: NotRequired[
        "capo_payment_cryptography.types.even_hex_length_between16_and32.EvenHexLengthBetween16And32"
    ]
    """<p>A random number value that is unique to the TR-34 key block generated using 2 pass. The operation will fail, if a random nonce value is not provided for a TR-34 key block generated using 2 pass.</p>"""
    key_block_headers: NotRequired[
        "capo_payment_cryptography.types.key_block_headers.KeyBlockHeaders"
    ]
    """<p>Optional metadata for export associated with the key material. This data is signed but transmitted in clear text.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportTr34KeyBlock) -> dict:
    out: dict = {}
    out["CertificateAuthorityPublicKeyIdentifier"] = value[
        "certificate_authority_public_key_identifier"
    ]
    out["WrappingKeyCertificate"] = value["wrapping_key_certificate"]
    out["ExportToken"] = value.get("export_token", "")
    if "signing_key_identifier" in value:
        out["SigningKeyIdentifier"] = value["signing_key_identifier"]
    if "signing_key_certificate" in value:
        out["SigningKeyCertificate"] = value["signing_key_certificate"]
    out["KeyBlockFormat"] = value["key_block_format"]
    if "random_nonce" in value:
        out["RandomNonce"] = value["random_nonce"]
    if "key_block_headers" in value:
        import capo_payment_cryptography.types.key_block_headers

        out["KeyBlockHeaders"] = (
            capo_payment_cryptography.types.key_block_headers.serialize_aws_json_1_0(
                value["key_block_headers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportTr34KeyBlock:
    out: ExportTr34KeyBlock = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityPublicKeyIdentifier") is not None:
        out["certificate_authority_public_key_identifier"] = data[
            "CertificateAuthorityPublicKeyIdentifier"
        ]
    else:
        raise DeserializationError(
            "ExportTr34KeyBlock.certificate_authority_public_key_identifier required"
        )
    if data.get("WrappingKeyCertificate") is not None:
        out["wrapping_key_certificate"] = data["WrappingKeyCertificate"]
    else:
        raise DeserializationError(
            "ExportTr34KeyBlock.wrapping_key_certificate required"
        )
    if data.get("ExportToken") is not None:
        out["export_token"] = data["ExportToken"]
    else:
        out["export_token"] = ""
    if data.get("SigningKeyIdentifier") is not None:
        out["signing_key_identifier"] = data["SigningKeyIdentifier"]
    if data.get("SigningKeyCertificate") is not None:
        out["signing_key_certificate"] = data["SigningKeyCertificate"]
    if data.get("KeyBlockFormat") is not None:
        out["key_block_format"] = data["KeyBlockFormat"]
    else:
        raise DeserializationError("ExportTr34KeyBlock.key_block_format required")
    if data.get("RandomNonce") is not None:
        out["random_nonce"] = data["RandomNonce"]
    if data.get("KeyBlockHeaders") is not None:
        import capo_payment_cryptography.types.key_block_headers

        out["key_block_headers"] = (
            capo_payment_cryptography.types.key_block_headers.deserialize_aws_json_1_0(
                data["KeyBlockHeaders"]
            )
        )
    return out
