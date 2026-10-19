"""Generated from Smithy shape ``com.amazonaws.acm#ResendValidationEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.domain_name_string


class ResendValidationEmailRequest(TypedDict, closed=True):
    certificate_arn: "capo_acm.types.arn.Arn"
    """<p>String that contains the ARN of the requested certificate. The certificate ARN is generated and returned by the <a>RequestCertificate</a> action as soon as the request is made. By default, using this parameter causes email to be sent to all top-level domains you specified in the certificate request. The ARN must be of the form: </p> <p> <code>arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p>"""
    domain: "capo_acm.types.domain_name_string.DomainNameString"
    """<p>The fully qualified domain name (FQDN) of the certificate that needs to be validated.</p>"""
    validation_domain: "capo_acm.types.domain_name_string.DomainNameString"
    """<p>The base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the <code>Domain</code> value or a superdomain of the <code>Domain</code> value. For example, if you requested a certificate for <code>site.subdomain.example.com</code> and specify a <b>ValidationDomain</b> of <code>subdomain.example.com</code>, ACM sends email to the the following five addresses:</p> <ul> <li> <p>admin@subdomain.example.com</p> </li> <li> <p>administrator@subdomain.example.com</p> </li> <li> <p>hostmaster@subdomain.example.com</p> </li> <li> <p>postmaster@subdomain.example.com</p> </li> <li> <p>webmaster@subdomain.example.com</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResendValidationEmailRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    out["Domain"] = value["domain"]
    out["ValidationDomain"] = value["validation_domain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResendValidationEmailRequest:
    out: ResendValidationEmailRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        out["certificate_arn"] = ""
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        out["domain"] = ""
    if data.get("ValidationDomain") is not None:
        out["validation_domain"] = data["ValidationDomain"]
    else:
        out["validation_domain"] = ""
    return out
