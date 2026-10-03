"""Generated from Smithy shape ``com.amazonaws.acmpca#IssueCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.api_passthrough
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.csr_blob
    import capo_acm_pca.types.idempotency_token
    import capo_acm_pca.types.signing_algorithm
    import capo_acm_pca.types.validity


class IssueCertificateRequest(TypedDict, closed=True):
    api_passthrough: NotRequired["capo_acm_pca.types.api_passthrough.ApiPassthrough"]
    """<p>Specifies X.509 certificate information to be included in the issued certificate. An <code>APIPassthrough</code> or <code>APICSRPassthrough</code> template variant must be selected, or else this parameter is ignored. For more information about using these templates, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html">Understanding Certificate Templates</a>.</p> <p>If conflicting or duplicate certificate information is supplied during certificate issuance, Amazon Web Services Private CA applies <a href="https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations">order of operation rules</a> to determine what information is used.</p>"""
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>"""
    csr: "capo_acm_pca.types.csr_blob.CsrBlob"
    """<p>The certificate signing request (CSR) for the certificate you want to issue. As an example, you can use the following OpenSSL command to create the CSR and a 2048 bit RSA private key. </p> <p> <code>openssl req -new -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr</code> </p> <p>If you have a configuration file, you can then use the following OpenSSL command. The <code>usr_cert</code> block in the configuration file contains your X509 version 3 extensions. </p> <p> <code>openssl req -new -config openssl_rsa.cnf -extensions usr_cert -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr</code> </p> <p>Note: A CSR must provide either a <i>subject name</i> or a <i>subject alternative name</i> or the request will be rejected. </p>"""
    signing_algorithm: "capo_acm_pca.types.signing_algorithm.SigningAlgorithm"
    """<p>The name of the algorithm that will be used to sign the certificate to be issued. </p> <p>This parameter should not be confused with the <code>SigningAlgorithm</code> parameter used to sign a CSR in the <code>CreateCertificateAuthority</code> action.</p> <note> <p>The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.</p> </note>"""
    template_arn: NotRequired["capo_acm_pca.types.arn.Arn"]
    """<p>Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, Amazon Web Services Private CA defaults to the <code>EndEntityCertificate/V1</code> template. For CA certificates, you should choose the shortest path length that meets your needs. The path length is indicated by the PathLen<i>N</i> portion of the ARN, where <i>N</i> is the <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PcaTerms.html#terms-cadepth">CA depth</a>.</p> <p>Note: The CA depth configured on a subordinate CA certificate must not exceed the limit set by its parents in the CA hierarchy.</p> <p>For a list of <code>TemplateArn</code> values supported by Amazon Web Services Private CA, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html">Understanding Certificate Templates</a>.</p>"""
    validity: "capo_acm_pca.types.validity.Validity"
    """<p>Information describing the end of the validity period of the certificate. This parameter sets the “Not After” date for the certificate.</p> <p>Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see <a href="https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.5">Validity</a> in RFC 5280. </p> <p>This value is unaffected when <code>ValidityNotBefore</code> is also specified. For example, if <code>Validity</code> is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the <code>ValidityNotBefore</code> value.</p> <p>The end of the validity period configured on a certificate must not exceed the limit set on its parents in the CA hierarchy.</p>"""
    validity_not_before: NotRequired["capo_acm_pca.types.validity.Validity"]
    """<p>Information describing the start of the validity period of the certificate. This parameter sets the “Not Before" date for the certificate.</p> <p>By default, when issuing a certificate, Amazon Web Services Private CA sets the "Not Before" date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The <code>ValidityNotBefore</code> parameter can be used to customize the “Not Before” value. </p> <p>Unlike the <code>Validity</code> parameter, the <code>ValidityNotBefore</code> parameter is optional.</p> <p>The <code>ValidityNotBefore</code> value is expressed as an explicit date and time, using the <code>Validity</code> type value <code>ABSOLUTE</code>. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_Validity.html">Validity</a> in this API reference and <a href="https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.5">Validity</a> in RFC 5280.</p>"""
    idempotency_token: NotRequired[
        "capo_acm_pca.types.idempotency_token.IdempotencyToken"
    ]
    """<p>Alphanumeric string that can be used to distinguish between calls to the <b>IssueCertificate</b> action. Idempotency tokens for <b>IssueCertificate</b> time out after five minutes. Therefore, if you call <b>IssueCertificate</b> multiple times with the same idempotency token within five minutes, Amazon Web Services Private CA recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, Amazon Web Services Private CA recognizes that you are requesting multiple certificates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IssueCertificateRequest) -> dict:
    out: dict = {}
    if "api_passthrough" in value:
        import capo_acm_pca.types.api_passthrough

        out["ApiPassthrough"] = (
            capo_acm_pca.types.api_passthrough.serialize_aws_json_1_1(
                value["api_passthrough"]
            )
        )
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    import capo_acm_pca.types.csr_blob

    out["Csr"] = capo_acm_pca.types.csr_blob.serialize_aws_json_1_1(value["csr"])
    import capo_acm_pca.types.signing_algorithm

    out["SigningAlgorithm"] = (
        capo_acm_pca.types.signing_algorithm.serialize_aws_json_1_1(
            value["signing_algorithm"]
        )
    )
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    import capo_acm_pca.types.validity

    out["Validity"] = capo_acm_pca.types.validity.serialize_aws_json_1_1(
        value["validity"]
    )
    if "validity_not_before" in value:
        import capo_acm_pca.types.validity

        out["ValidityNotBefore"] = capo_acm_pca.types.validity.serialize_aws_json_1_1(
            value["validity_not_before"]
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IssueCertificateRequest:
    out: IssueCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApiPassthrough") is not None:
        import capo_acm_pca.types.api_passthrough

        out["api_passthrough"] = (
            capo_acm_pca.types.api_passthrough.deserialize_aws_json_1_1(
                data["ApiPassthrough"]
            )
        )
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "IssueCertificateRequest.certificate_authority_arn required"
        )
    if data.get("Csr") is not None:
        import capo_acm_pca.types.csr_blob

        out["csr"] = capo_acm_pca.types.csr_blob.deserialize_aws_json_1_1(data["Csr"])
    else:
        raise DeserializationError("IssueCertificateRequest.csr required")
    if data.get("SigningAlgorithm") is not None:
        import capo_acm_pca.types.signing_algorithm

        out["signing_algorithm"] = (
            capo_acm_pca.types.signing_algorithm.deserialize_aws_json_1_1(
                data["SigningAlgorithm"]
            )
        )
    else:
        raise DeserializationError("IssueCertificateRequest.signing_algorithm required")
    if data.get("TemplateArn") is not None:
        out["template_arn"] = data["TemplateArn"]
    if data.get("Validity") is not None:
        import capo_acm_pca.types.validity

        out["validity"] = capo_acm_pca.types.validity.deserialize_aws_json_1_1(
            data["Validity"]
        )
    else:
        raise DeserializationError("IssueCertificateRequest.validity required")
    if data.get("ValidityNotBefore") is not None:
        import capo_acm_pca.types.validity

        out["validity_not_before"] = (
            capo_acm_pca.types.validity.deserialize_aws_json_1_1(
                data["ValidityNotBefore"]
            )
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
