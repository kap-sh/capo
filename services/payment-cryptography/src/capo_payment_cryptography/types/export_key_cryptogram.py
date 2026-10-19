"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportKeyCryptogram``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_type
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.wrapping_key_spec


class ExportKeyCryptogram(TypedDict, closed=True):
    certificate_authority_public_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The <code>KeyARN</code> of the certificate chain that signs the wrapping key certificate during RSA wrap and unwrap key export.</p>"""
    wrapping_key_certificate: (
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The wrapping key certificate in PEM format (base64 encoded). Amazon Web Services Payment Cryptography uses this certificate to wrap the key under export.</p>"""
    wrapping_spec: NotRequired[
        "capo_payment_cryptography.types.wrapping_key_spec.WrappingKeySpec"
    ]
    """<p>The wrapping spec for the key under export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportKeyCryptogram) -> dict:
    out: dict = {}
    out["CertificateAuthorityPublicKeyIdentifier"] = value[
        "certificate_authority_public_key_identifier"
    ]
    out["WrappingKeyCertificate"] = value["wrapping_key_certificate"]
    if "wrapping_spec" in value:
        out["WrappingSpec"] = value["wrapping_spec"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportKeyCryptogram:
    out: ExportKeyCryptogram = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityPublicKeyIdentifier") is not None:
        out["certificate_authority_public_key_identifier"] = data[
            "CertificateAuthorityPublicKeyIdentifier"
        ]
    else:
        out["certificate_authority_public_key_identifier"] = ""
    if data.get("WrappingKeyCertificate") is not None:
        out["wrapping_key_certificate"] = data["WrappingKeyCertificate"]
    else:
        out["wrapping_key_certificate"] = ""
    if data.get("WrappingSpec") is not None:
        out["wrapping_spec"] = data["WrappingSpec"]
    return out
