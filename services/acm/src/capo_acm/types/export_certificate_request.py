"""Generated from Smithy shape ``com.amazonaws.acm#ExportCertificateRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.passphrase_blob


class ExportCertificateRequest(TypedDict, closed=True):
    certificate_arn: "capo_acm.types.arn.Arn"
    """<p>An Amazon Resource Name (ARN) of the issued certificate. This must be of the form:</p> <p> <code>arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012</code> </p>"""
    passphrase: "capo_acm.types.passphrase_blob.PassphraseBlob"
    """<p>Passphrase to associate with the encrypted exported private key. </p> <note> <p>When creating your passphrase, you can use any ASCII character except #, $, or %.</p> </note> <p>If you want to later decrypt the private key, you must have the passphrase. You can use the following OpenSSL command to decrypt a private key. After entering the command, you are prompted for the passphrase.</p> <p> <code>openssl rsa -in encrypted_key.pem -out decrypted_key.pem</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    import capo_acm.types.passphrase_blob

    out["Passphrase"] = capo_acm.types.passphrase_blob.serialize_aws_json_1_1(
        value["passphrase"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportCertificateRequest:
    out: ExportCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        out["certificate_arn"] = ""
    if data.get("Passphrase") is not None:
        import capo_acm.types.passphrase_blob

        out["passphrase"] = capo_acm.types.passphrase_blob.deserialize_aws_json_1_1(
            data["Passphrase"]
        )
    else:
        out["passphrase"] = b""
    return out


def redact_sensitive(value: ExportCertificateRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "passphrase" in value:
        out["passphrase"] = "*** Sensitive Data Redacted ***"
    return out
