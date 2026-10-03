"""Generated from Smithy shape ``com.amazonaws.acmpca#RevokeCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.revocation_reason
    import capo_acm_pca.types.string128


class RevokeCertificateRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>"""
    certificate_serial: "capo_acm_pca.types.string128.String128"
    """<p>Serial number of the certificate to be revoked. This must be in hexadecimal format. You can retrieve the serial number by calling <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html">GetCertificate</a> with the Amazon Resource Name (ARN) of the certificate you want and the ARN of your private CA. The <b>GetCertificate</b> action retrieves the certificate in the PEM format. You can use the following OpenSSL command to list the certificate in text format and copy the hexadecimal serial number. </p> <p> <code>openssl x509 -in <i>file_path</i> -text -noout</code> </p> <p>You can also copy the serial number from the console or use the <a href="https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html">DescribeCertificate</a> action in the <i>Certificate Manager API Reference</i>. </p>"""
    revocation_reason: "capo_acm_pca.types.revocation_reason.RevocationReason"
    """<p>Specifies why you revoked the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    out["CertificateSerial"] = value["certificate_serial"]
    import capo_acm_pca.types.revocation_reason

    out["RevocationReason"] = (
        capo_acm_pca.types.revocation_reason.serialize_aws_json_1_1(
            value["revocation_reason"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeCertificateRequest:
    out: RevokeCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "RevokeCertificateRequest.certificate_authority_arn required"
        )
    if data.get("CertificateSerial") is not None:
        out["certificate_serial"] = data["CertificateSerial"]
    else:
        raise DeserializationError(
            "RevokeCertificateRequest.certificate_serial required"
        )
    if data.get("RevocationReason") is not None:
        import capo_acm_pca.types.revocation_reason

        out["revocation_reason"] = (
            capo_acm_pca.types.revocation_reason.deserialize_aws_json_1_1(
                data["RevocationReason"]
            )
        )
    else:
        raise DeserializationError(
            "RevokeCertificateRequest.revocation_reason required"
        )
    return out
