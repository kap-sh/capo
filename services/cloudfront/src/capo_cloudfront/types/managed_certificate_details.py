"""Generated from Smithy shape ``com.amazonaws.cloudfront#ManagedCertificateDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.managed_certificate_status
    import capo_cloudfront.types.string
    import capo_cloudfront.types.validation_token_detail_list
    import capo_cloudfront.types.validation_token_host


class ManagedCertificateDetails(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ARN of the CloudFront managed ACM certificate.</p>"""
    certificate_status: NotRequired[
        "capo_cloudfront.types.managed_certificate_status.ManagedCertificateStatus"
    ]
    """<p>The status of the CloudFront managed ACM certificate.</p> <note> <p>Your distribution tenant will be updated with the latest certificate status. When calling the <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistributionTenant.html">UpdateDistributionTenant</a> operation, use the latest value for the <code>ETag</code>.</p> </note>"""
    validation_token_host: NotRequired[
        "capo_cloudfront.types.validation_token_host.ValidationTokenHost"
    ]
    """<p>Contains details about the validation token host of the specified CloudFront managed ACM certificate.</p> <ul> <li> <p>For <code>cloudfront</code>, CloudFront will automatically serve the validation token. Choose this mode if you can point the domain's DNS to CloudFront immediately.</p> </li> <li> <p>For <code>self-hosted</code>, you serve the validation token from your existing infrastructure. Choose this mode when you need to maintain current traffic flow while your certificate is being issued. You can place the validation token at the well-known path on your existing web server, wait for ACM to validate and issue the certificate, and then update your DNS to point to CloudFront.</p> </li> </ul> <note> <p>This setting only affects the initial certificate request. Once the DNS points to CloudFront, all future certificate renewals are automatically handled through CloudFront.</p> </note>"""
    validation_token_details: NotRequired[
        "capo_cloudfront.types.validation_token_detail_list.ValidationTokenDetailList"
    ]
    """<p>Contains details about the validation token of the specified CloudFront managed ACM certificate.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ManagedCertificateDetails, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "certificate_arn" in value:
        SubElement(el, "CertificateArn").text = str(value["certificate_arn"])
    if "certificate_status" in value:
        import capo_cloudfront.types.managed_certificate_status

        capo_cloudfront.types.managed_certificate_status.serialize_xml(
            value["certificate_status"], el, "CertificateStatus"
        )
    if "validation_token_host" in value:
        import capo_cloudfront.types.validation_token_host

        capo_cloudfront.types.validation_token_host.serialize_xml(
            value["validation_token_host"], el, "ValidationTokenHost"
        )
    if "validation_token_details" in value:
        import capo_cloudfront.types.validation_token_detail_list

        capo_cloudfront.types.validation_token_detail_list.serialize_xml(
            value["validation_token_details"], el, "ValidationTokenDetails"
        )


def deserialize_xml(el: Element) -> ManagedCertificateDetails:
    out: ManagedCertificateDetails = {}  # type: ignore[typeddict-item]
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    child_certificate_status = el.find("CertificateStatus")
    if child_certificate_status is not None:
        import capo_cloudfront.types.managed_certificate_status

        out["certificate_status"] = (
            capo_cloudfront.types.managed_certificate_status.deserialize_xml(
                child_certificate_status
            )
        )
    child_validation_token_host = el.find("ValidationTokenHost")
    if child_validation_token_host is not None:
        import capo_cloudfront.types.validation_token_host

        out["validation_token_host"] = (
            capo_cloudfront.types.validation_token_host.deserialize_xml(
                child_validation_token_host
            )
        )
    child_validation_token_details = el.find("ValidationTokenDetails")
    if child_validation_token_details is not None:
        import capo_cloudfront.types.validation_token_detail_list

        out["validation_token_details"] = (
            capo_cloudfront.types.validation_token_detail_list.deserialize_xml(
                child_validation_token_details
            )
        )
    return out
