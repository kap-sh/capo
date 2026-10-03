"""Generated from Smithy shape ``com.amazonaws.cloudfront#ViewerCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.certificate_source
    import capo_cloudfront.types.minimum_protocol_version
    import capo_cloudfront.types.server_certificate_id
    import capo_cloudfront.types.ssl_support_method
    import capo_cloudfront.types.string


class ViewerCertificate(TypedDict, closed=True):
    cloud_front_default_certificate: NotRequired[
        "capo_cloudfront.types.boolean.boolean"
    ]
    """<p>If the distribution uses the CloudFront domain name such as <code>d111111abcdef8.cloudfront.net</code>, set this field to <code>true</code>.</p> <p>If the distribution uses <code>Aliases</code> (alternate domain names or CNAMEs), set this field to <code>false</code> and specify values for the following fields:</p> <ul> <li> <p> <code>ACMCertificateArn</code> or <code>IAMCertificateId</code> (specify a value for one, not both)</p> </li> <li> <p> <code>MinimumProtocolVersion</code> </p> </li> <li> <p> <code>SSLSupportMethod</code> </p> </li> </ul>"""
    iam_certificate_id: NotRequired[
        "capo_cloudfront.types.server_certificate_id.ServerCertificateId"
    ]
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>If the distribution uses <code>Aliases</code> (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html">Identity and Access Management (IAM)</a>, provide the ID of the IAM certificate.</p> <p>If you specify an IAM certificate ID, you must also specify values for <code>MinimumProtocolVersion</code> and <code>SSLSupportMethod</code>. </p>"""
    acm_certificate_arn: NotRequired["capo_cloudfront.types.string.string"]
    """<p>If the distribution uses <code>Aliases</code> (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html">Certificate Manager (ACM)</a>, provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (<code>us-east-1</code>).</p> <p>If you specify an ACM certificate ARN, you must also specify values for <code>MinimumProtocolVersion</code> and <code>SSLSupportMethod</code>.</p>"""
    ssl_support_method: NotRequired[
        "capo_cloudfront.types.ssl_support_method.SSLSupportMethod"
    ]
    """<p>If the distribution uses <code>Aliases</code> (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.</p> <ul> <li> <p> <code>sni-only</code> – The distribution accepts HTTPS connections from only viewers that support <a href="https://en.wikipedia.org/wiki/Server_Name_Indication">server name indication (SNI)</a>. This is recommended. Most browsers and clients support SNI.</p> </li> <li> <p> <code>vip</code> – The distribution accepts HTTPS connections from all viewers including those that don't support SNI. This is not recommended, and results in additional monthly charges from CloudFront.</p> </li> <li> <p> <code>static-ip</code> - Do not specify this value unless your distribution has been enabled for this feature by the CloudFront team. If you have a use case that requires static IP addresses for a distribution, contact CloudFront through the <a href="https://console.aws.amazon.com/support/home">Amazon Web ServicesSupport Center</a>.</p> </li> </ul> <p>If the distribution uses the CloudFront domain name such as <code>d111111abcdef8.cloudfront.net</code>, don't set a value for this field.</p>"""
    minimum_protocol_version: NotRequired[
        "capo_cloudfront.types.minimum_protocol_version.MinimumProtocolVersion"
    ]
    """<p>If the distribution uses <code>Aliases</code> (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:</p> <ul> <li> <p>The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.</p> </li> <li> <p>The ciphers that CloudFront can use to encrypt the content that it returns to viewers.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValues-security-policy">Security Policy</a> and <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html#secure-connections-supported-ciphers">Supported Protocols and Ciphers Between Viewers and CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <note> <p>On the CloudFront console, this setting is called <b>Security Policy</b>.</p> </note> <p>When you're using SNI only (you set <code>SSLSupportMethod</code> to <code>sni-only</code>), you must specify <code>TLSv1</code> or higher.</p> <p>If the distribution uses the CloudFront domain name such as <code>d111111abcdef8.cloudfront.net</code> (you set <code>CloudFrontDefaultCertificate</code> to <code>true</code>), CloudFront automatically sets the security policy to <code>TLSv1</code> regardless of the value that you set here.</p>"""
    certificate: NotRequired["capo_cloudfront.types.string.string"]
    """<p>This field is deprecated. Use one of the following fields instead:</p> <ul> <li> <p> <code>ACMCertificateArn</code> </p> </li> <li> <p> <code>IAMCertificateId</code> </p> </li> <li> <p> <code>CloudFrontDefaultCertificate</code> </p> </li> </ul>"""
    certificate_source: NotRequired[
        "capo_cloudfront.types.certificate_source.CertificateSource"
    ]
    """<p>This field is deprecated. Use one of the following fields instead:</p> <ul> <li> <p> <code>ACMCertificateArn</code> </p> </li> <li> <p> <code>IAMCertificateId</code> </p> </li> <li> <p> <code>CloudFrontDefaultCertificate</code> </p> </li> </ul>"""


# --- restXml ser/de ---
def serialize_xml(value: ViewerCertificate, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "cloud_front_default_certificate" in value:
        SubElement(el, "CloudFrontDefaultCertificate").text = (
            "true" if value["cloud_front_default_certificate"] else "false"
        )
    if "iam_certificate_id" in value:
        SubElement(el, "IAMCertificateId").text = str(value["iam_certificate_id"])
    if "acm_certificate_arn" in value:
        SubElement(el, "ACMCertificateArn").text = str(value["acm_certificate_arn"])
    if "ssl_support_method" in value:
        import capo_cloudfront.types.ssl_support_method

        capo_cloudfront.types.ssl_support_method.serialize_xml(
            value["ssl_support_method"], el, "SSLSupportMethod"
        )
    if "minimum_protocol_version" in value:
        import capo_cloudfront.types.minimum_protocol_version

        capo_cloudfront.types.minimum_protocol_version.serialize_xml(
            value["minimum_protocol_version"], el, "MinimumProtocolVersion"
        )
    if "certificate" in value:
        SubElement(el, "Certificate").text = str(value["certificate"])
    if "certificate_source" in value:
        import capo_cloudfront.types.certificate_source

        capo_cloudfront.types.certificate_source.serialize_xml(
            value["certificate_source"], el, "CertificateSource"
        )


def deserialize_xml(el: Element) -> ViewerCertificate:
    out: ViewerCertificate = {}  # type: ignore[typeddict-item]
    child_cloud_front_default_certificate = el.find("CloudFrontDefaultCertificate")
    if child_cloud_front_default_certificate is not None:
        out["cloud_front_default_certificate"] = (
            child_cloud_front_default_certificate.text or ""
        ).lower() == "true"
    child_iam_certificate_id = el.find("IAMCertificateId")
    if child_iam_certificate_id is not None:
        out["iam_certificate_id"] = str(child_iam_certificate_id.text or "")
    child_acm_certificate_arn = el.find("ACMCertificateArn")
    if child_acm_certificate_arn is not None:
        out["acm_certificate_arn"] = str(child_acm_certificate_arn.text or "")
    child_ssl_support_method = el.find("SSLSupportMethod")
    if child_ssl_support_method is not None:
        import capo_cloudfront.types.ssl_support_method

        out["ssl_support_method"] = (
            capo_cloudfront.types.ssl_support_method.deserialize_xml(
                child_ssl_support_method
            )
        )
    child_minimum_protocol_version = el.find("MinimumProtocolVersion")
    if child_minimum_protocol_version is not None:
        import capo_cloudfront.types.minimum_protocol_version

        out["minimum_protocol_version"] = (
            capo_cloudfront.types.minimum_protocol_version.deserialize_xml(
                child_minimum_protocol_version
            )
        )
    child_certificate = el.find("Certificate")
    if child_certificate is not None:
        out["certificate"] = str(child_certificate.text or "")
    child_certificate_source = el.find("CertificateSource")
    if child_certificate_source is not None:
        import capo_cloudfront.types.certificate_source

        out["certificate_source"] = (
            capo_cloudfront.types.certificate_source.deserialize_xml(
                child_certificate_source
            )
        )
    return out
