"""Generated from Smithy shape ``com.amazonaws.acm#RequestCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm.types.certificate_managed_by
    import capo_acm.types.certificate_options
    import capo_acm.types.domain_list
    import capo_acm.types.domain_name_string
    import capo_acm.types.domain_validation_option_list
    import capo_acm.types.idempotency_token
    import capo_acm.types.key_algorithm
    import capo_acm.types.pca_arn
    import capo_acm.types.tag_list
    import capo_acm.types.validation_method


class RequestCertificateRequest(TypedDict, closed=True):
    domain_name: "capo_acm.types.domain_name_string.DomainNameString"
    """<p>Fully qualified domain name (FQDN), such as www.example.com, that you want to secure with an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, *.example.com protects www.example.com, site.example.com, and images.example.com. </p> <p>In compliance with <a href="https://datatracker.ietf.org/doc/html/rfc5280">RFC 5280</a>, the length of the domain name (technically, the Common Name) that you provide cannot exceed 64 octets (characters), including periods. To add a longer domain name, specify it in the Subject Alternative Name field, which supports names up to 253 octets in length. </p>"""
    validation_method: NotRequired["capo_acm.types.validation_method.ValidationMethod"]
    """<p>The method you want to use if you are requesting a public certificate to validate that you own or control domain. You can <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html">validate with DNS</a> or <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html">validate with email</a>. We recommend that you use DNS validation. </p>"""
    subject_alternative_names: NotRequired["capo_acm.types.domain_list.DomainList"]
    """<p>Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate. For example, add the name www.example.net to a certificate for which the <code>DomainName</code> field is www.example.com if users can reach your site by using either name. The maximum number of domain names that you can add to an ACM certificate is 100. However, the initial quota is 10 domain names. If you need more than 10 names, you must request a quota increase. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html">Quotas</a>.</p> <p> The maximum length of a SAN DNS name is 253 octets. The name is made up of multiple labels separated by periods. No label can be longer than 63 octets. Consider the following examples: </p> <ul> <li> <p> <code>(63 octets).(63 octets).(63 octets).(61 octets)</code> is legal because the total length is 253 octets (63+1+63+1+63+1+61) and no label exceeds 63 octets.</p> </li> <li> <p> <code>(64 octets).(63 octets).(63 octets).(61 octets)</code> is not legal because the total length exceeds 253 octets (64+1+63+1+63+1+61) and the first label exceeds 63 octets.</p> </li> <li> <p> <code>(63 octets).(63 octets).(63 octets).(62 octets)</code> is not legal because the total length of the DNS name (63+1+63+1+63+1+62) exceeds 253 octets.</p> </li> </ul>"""
    idempotency_token: NotRequired["capo_acm.types.idempotency_token.IdempotencyToken"]
    """<p>Customer chosen string that can be used to distinguish between calls to <code>RequestCertificate</code>. Idempotency tokens time out after one hour. Therefore, if you call <code>RequestCertificate</code> multiple times with the same idempotency token within one hour, ACM recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, ACM recognizes that you are requesting multiple certificates.</p>"""
    domain_validation_options: NotRequired[
        "capo_acm.types.domain_validation_option_list.DomainValidationOptionList"
    ]
    """<p>The domain name that you want ACM to use to send you emails so that you can validate domain ownership.</p>"""
    options: NotRequired["capo_acm.types.certificate_options.CertificateOptions"]
    """<p>You can use this parameter to specify whether to export your certificate.</p> <p>Certificate transparency logging opt-out is no longer available. All public certificates are recorded in a certificate transparency log. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency">Certificate Transparency Logging</a>.</p> <p>You can export public ACM certificates to use with Amazon Web Services services as well as outside the Amazon Web Services Cloud. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html">Certificate Manager exportable public certificate</a>.</p>"""
    certificate_authority_arn: NotRequired["capo_acm.types.pca_arn.PcaArn"]
    """<p>The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used to issue the certificate. If you do not provide an ARN and you are trying to request a private certificate, ACM will attempt to issue a public certificate. For more information about private CAs, see the <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html">Amazon Web Services Private Certificate Authority</a> user guide. The ARN must have the following form: </p> <p> <code>arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012</code> </p>"""
    tags: NotRequired["capo_acm.types.tag_list.TagList"]
    """<p>One or more resource tags to associate with the certificate.</p>"""
    key_algorithm: NotRequired["capo_acm.types.key_algorithm.KeyAlgorithm"]
    """<p>Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. RSA is the default key algorithm for ACM certificates. Elliptic Curve Digital Signature Algorithm (ECDSA) keys are smaller, offering security comparable to RSA keys but with greater computing efficiency. However, ECDSA is not supported by all network clients. Some Amazon Web Services services may require RSA keys, or only support ECDSA keys of a particular size, while others allow the use of either RSA and ECDSA keys to ensure that compatibility is not broken. Check the requirements for the Amazon Web Services service where you plan to deploy your certificate. For more information about selecting an algorithm, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate-characteristics.html#algorithms-term">Key algorithms</a>.</p> <note> <p>Algorithms supported for an ACM certificate request include: </p> <ul> <li> <p> <code>RSA_2048</code> </p> </li> <li> <p> <code>EC_prime256v1</code> </p> </li> <li> <p> <code>EC_secp384r1</code> </p> </li> </ul> <p>Other listed algorithms are for imported certificates only. </p> </note> <note> <p>When you request a private PKI certificate signed by a CA from Amazon Web Services Private CA, the specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.</p> </note> <p>Default: RSA_2048</p>"""
    managed_by: NotRequired[
        "capo_acm.types.certificate_managed_by.CertificateManagedBy"
    ]
    """<p>Identifies the Amazon Web Services service that manages the certificate issued by ACM.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestCertificateRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "validation_method" in value:
        import capo_acm.types.validation_method

        out["ValidationMethod"] = (
            capo_acm.types.validation_method.serialize_aws_json_1_1(
                value["validation_method"]
            )
        )
    if "subject_alternative_names" in value:
        import capo_acm.types.domain_list

        out["SubjectAlternativeNames"] = (
            capo_acm.types.domain_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "domain_validation_options" in value:
        import capo_acm.types.domain_validation_option_list

        out["DomainValidationOptions"] = (
            capo_acm.types.domain_validation_option_list.serialize_aws_json_1_1(
                value["domain_validation_options"]
            )
        )
    if "options" in value:
        import capo_acm.types.certificate_options

        out["Options"] = capo_acm.types.certificate_options.serialize_aws_json_1_1(
            value["options"]
        )
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "tags" in value:
        import capo_acm.types.tag_list

        out["Tags"] = capo_acm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "key_algorithm" in value:
        import capo_acm.types.key_algorithm

        out["KeyAlgorithm"] = capo_acm.types.key_algorithm.serialize_aws_json_1_1(
            value["key_algorithm"]
        )
    if "managed_by" in value:
        import capo_acm.types.certificate_managed_by

        out["ManagedBy"] = capo_acm.types.certificate_managed_by.serialize_aws_json_1_1(
            value["managed_by"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestCertificateRequest:
    out: RequestCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("RequestCertificateRequest.domain_name required")
    if data.get("ValidationMethod") is not None:
        import capo_acm.types.validation_method

        out["validation_method"] = (
            capo_acm.types.validation_method.deserialize_aws_json_1_1(
                data["ValidationMethod"]
            )
        )
    if data.get("SubjectAlternativeNames") is not None:
        import capo_acm.types.domain_list

        out["subject_alternative_names"] = (
            capo_acm.types.domain_list.deserialize_aws_json_1_1(
                data["SubjectAlternativeNames"]
            )
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("DomainValidationOptions") is not None:
        import capo_acm.types.domain_validation_option_list

        out["domain_validation_options"] = (
            capo_acm.types.domain_validation_option_list.deserialize_aws_json_1_1(
                data["DomainValidationOptions"]
            )
        )
    if data.get("Options") is not None:
        import capo_acm.types.certificate_options

        out["options"] = capo_acm.types.certificate_options.deserialize_aws_json_1_1(
            data["Options"]
        )
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if data.get("Tags") is not None:
        import capo_acm.types.tag_list

        out["tags"] = capo_acm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("KeyAlgorithm") is not None:
        import capo_acm.types.key_algorithm

        out["key_algorithm"] = capo_acm.types.key_algorithm.deserialize_aws_json_1_1(
            data["KeyAlgorithm"]
        )
    if data.get("ManagedBy") is not None:
        import capo_acm.types.certificate_managed_by

        out["managed_by"] = (
            capo_acm.types.certificate_managed_by.deserialize_aws_json_1_1(
                data["ManagedBy"]
            )
        )
    return out
