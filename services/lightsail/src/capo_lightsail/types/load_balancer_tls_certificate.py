"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.domain_name
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record_list
    import capo_lightsail.types.load_balancer_tls_certificate_failure_reason
    import capo_lightsail.types.load_balancer_tls_certificate_renewal_summary
    import capo_lightsail.types.load_balancer_tls_certificate_revocation_reason
    import capo_lightsail.types.load_balancer_tls_certificate_status
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string
    import capo_lightsail.types.string_list
    import capo_lightsail.types.tag_list


class LoadBalancerTlsCertificate(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the SSL/TLS certificate (<code>my-certificate</code>).</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the SSL/TLS certificate.</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about your Lightsail load balancer or SSL/TLS certificate. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The time when you created your SSL/TLS certificate.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>The Amazon Web Services Region and Availability Zone where you created your certificate.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The resource type (<code>LoadBalancerTlsCertificate</code>).</p> <ul> <li> <p> <b> <code>Instance</code> </b> - A Lightsail instance (a virtual private server)</p> </li> <li> <p> <b> <code>StaticIp</code> </b> - A static IP address</p> </li> <li> <p> <b> <code>KeyPair</code> </b> - The key pair used to connect to a Lightsail instance</p> </li> <li> <p> <b> <code>InstanceSnapshot</code> </b> - A Lightsail instance snapshot</p> </li> <li> <p> <b> <code>Domain</code> </b> - A DNS zone</p> </li> <li> <p> <b> <code>PeeredVpc</code> </b> - A peered VPC</p> </li> <li> <p> <b> <code>LoadBalancer</code> </b> - A Lightsail load balancer</p> </li> <li> <p> <b> <code>LoadBalancerTlsCertificate</code> </b> - An SSL/TLS certificate associated with a Lightsail load balancer</p> </li> <li> <p> <b> <code>Disk</code> </b> - A Lightsail block storage disk</p> </li> <li> <p> <b> <code>DiskSnapshot</code> </b> - A block storage disk snapshot</p> </li> </ul>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    load_balancer_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The load balancer name where your SSL/TLS certificate is attached.</p>"""
    is_attached: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>When <code>true</code>, the SSL/TLS certificate is attached to the Lightsail load balancer.</p>"""
    status: NotRequired[
        "capo_lightsail.types.load_balancer_tls_certificate_status.LoadBalancerTlsCertificateStatus"
    ]
    """<p>The validation status of the SSL/TLS certificate. Valid values are below.</p>"""
    domain_name: NotRequired["capo_lightsail.types.domain_name.DomainName"]
    """<p>The domain name for your SSL/TLS certificate.</p>"""
    domain_validation_records: NotRequired[
        "capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record_list.LoadBalancerTlsCertificateDomainValidationRecordList"
    ]
    """<p>An array of LoadBalancerTlsCertificateDomainValidationRecord objects describing the records.</p>"""
    failure_reason: NotRequired[
        "capo_lightsail.types.load_balancer_tls_certificate_failure_reason.LoadBalancerTlsCertificateFailureReason"
    ]
    """<p>The validation failure reason, if any, of the certificate.</p> <p>The following failure reasons are possible:</p> <ul> <li> <p> <b> <code>NO_AVAILABLE_CONTACTS</code> </b> - This failure applies to email validation, which is not available for Lightsail certificates.</p> </li> <li> <p> <b> <code>ADDITIONAL_VERIFICATION_REQUIRED</code> </b> - Lightsail requires additional information to process this certificate request. This can happen as a fraud-protection measure, such as when the domain ranks within the Alexa top 1000 websites. To provide the required information, use the <a href="https://console.aws.amazon.com/support/home">AWS Support Center</a> to contact AWS Support.</p> <note> <p>You cannot request a certificate for Amazon-owned domain names such as those ending in amazonaws.com, cloudfront.net, or elasticbeanstalk.com.</p> </note> </li> <li> <p> <b> <code>DOMAIN_NOT_ALLOWED</code> </b> - One or more of the domain names in the certificate request was reported as an unsafe domain by <a href="https://www.virustotal.com/gui/home/url">VirusTotal</a>. To correct the problem, search for your domain name on the <a href="https://www.virustotal.com/gui/home/url">VirusTotal</a> website. If your domain is reported as suspicious, see <a href="https://developers.google.com/web/fundamentals/security/hacked">Google Help for Hacked Websites</a> to learn what you can do.</p> <p>If you believe that the result is a false positive, notify the organization that is reporting the domain. VirusTotal is an aggregate of several antivirus and URL scanners and cannot remove your domain from a block list itself. After you correct the problem and the VirusTotal registry has been updated, request a new certificate.</p> <p>If you see this error and your domain is not included in the VirusTotal list, visit the <a href="https://console.aws.amazon.com/support/home">AWS Support Center</a> and create a case.</p> </li> <li> <p> <b> <code>INVALID_PUBLIC_DOMAIN</code> </b> - One or more of the domain names in the certificate request is not valid. Typically, this is because a domain name in the request is not a valid top-level domain. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request, and ensure that all domain names in the request are for valid top-level domains. For example, you cannot request a certificate for <code>example.invalidpublicdomain</code> because <code>invalidpublicdomain</code> is not a valid top-level domain.</p> </li> <li> <p> <b> <code>OTHER</code> </b> - Typically, this failure occurs when there is a typographical error in one or more of the domain names in the certificate request. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request. </p> </li> </ul>"""
    issued_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The time when the SSL/TLS certificate was issued.</p>"""
    issuer: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The issuer of the certificate.</p>"""
    key_algorithm: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The algorithm used to generate the key pair (the public and private key).</p>"""
    not_after: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the SSL/TLS certificate expires.</p>"""
    not_before: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the SSL/TLS certificate is first valid.</p>"""
    renewal_summary: NotRequired[
        "capo_lightsail.types.load_balancer_tls_certificate_renewal_summary.LoadBalancerTlsCertificateRenewalSummary"
    ]
    """<p>An object that describes the status of the certificate renewal managed by Lightsail.</p>"""
    revocation_reason: NotRequired[
        "capo_lightsail.types.load_balancer_tls_certificate_revocation_reason.LoadBalancerTlsCertificateRevocationReason"
    ]
    """<p>The reason the certificate was revoked. This value is present only when the certificate status is <code>REVOKED</code>.</p>"""
    revoked_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate was revoked. This value is present only when the certificate status is <code>REVOKED</code>.</p>"""
    serial: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The serial number of the certificate.</p>"""
    signature_algorithm: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The algorithm that was used to sign the certificate.</p>"""
    subject: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The name of the entity that is associated with the public key contained in the certificate.</p>"""
    subject_alternative_names: NotRequired[
        "capo_lightsail.types.string_list.StringList"
    ]
    """<p>An array of strings that specify the alternate domains (<code>example2.com</code>) and subdomains (<code>blog.example.com</code>) for the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificate) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "load_balancer_name" in value:
        out["loadBalancerName"] = value["load_balancer_name"]
    if "is_attached" in value:
        out["isAttached"] = value["is_attached"]
    if "status" in value:
        import capo_lightsail.types.load_balancer_tls_certificate_status

        out["status"] = (
            capo_lightsail.types.load_balancer_tls_certificate_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "domain_validation_records" in value:
        import capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record_list

        out["domainValidationRecords"] = (
            capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record_list.serialize_aws_json_1_1(
                value["domain_validation_records"]
            )
        )
    if "failure_reason" in value:
        import capo_lightsail.types.load_balancer_tls_certificate_failure_reason

        out["failureReason"] = (
            capo_lightsail.types.load_balancer_tls_certificate_failure_reason.serialize_aws_json_1_1(
                value["failure_reason"]
            )
        )
    if "issued_at" in value:
        import capo_lightsail.types.iso_date

        out["issuedAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["issued_at"]
        )
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    if "key_algorithm" in value:
        out["keyAlgorithm"] = value["key_algorithm"]
    if "not_after" in value:
        import capo_lightsail.types.iso_date

        out["notAfter"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["not_after"]
        )
    if "not_before" in value:
        import capo_lightsail.types.iso_date

        out["notBefore"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["not_before"]
        )
    if "renewal_summary" in value:
        import capo_lightsail.types.load_balancer_tls_certificate_renewal_summary

        out["renewalSummary"] = (
            capo_lightsail.types.load_balancer_tls_certificate_renewal_summary.serialize_aws_json_1_1(
                value["renewal_summary"]
            )
        )
    if "revocation_reason" in value:
        import capo_lightsail.types.load_balancer_tls_certificate_revocation_reason

        out["revocationReason"] = (
            capo_lightsail.types.load_balancer_tls_certificate_revocation_reason.serialize_aws_json_1_1(
                value["revocation_reason"]
            )
        )
    if "revoked_at" in value:
        import capo_lightsail.types.iso_date

        out["revokedAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["revoked_at"]
        )
    if "serial" in value:
        out["serial"] = value["serial"]
    if "signature_algorithm" in value:
        out["signatureAlgorithm"] = value["signature_algorithm"]
    if "subject" in value:
        out["subject"] = value["subject"]
    if "subject_alternative_names" in value:
        import capo_lightsail.types.string_list

        out["subjectAlternativeNames"] = (
            capo_lightsail.types.string_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoadBalancerTlsCertificate:
    out: LoadBalancerTlsCertificate = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("supportCode") is not None:
        out["support_code"] = data["supportCode"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("loadBalancerName") is not None:
        out["load_balancer_name"] = data["loadBalancerName"]
    if data.get("isAttached") is not None:
        out["is_attached"] = data["isAttached"]
    if data.get("status") is not None:
        import capo_lightsail.types.load_balancer_tls_certificate_status

        out["status"] = (
            capo_lightsail.types.load_balancer_tls_certificate_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("domainValidationRecords") is not None:
        import capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record_list

        out["domain_validation_records"] = (
            capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record_list.deserialize_aws_json_1_1(
                data["domainValidationRecords"]
            )
        )
    if data.get("failureReason") is not None:
        import capo_lightsail.types.load_balancer_tls_certificate_failure_reason

        out["failure_reason"] = (
            capo_lightsail.types.load_balancer_tls_certificate_failure_reason.deserialize_aws_json_1_1(
                data["failureReason"]
            )
        )
    if data.get("issuedAt") is not None:
        import capo_lightsail.types.iso_date

        out["issued_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["issuedAt"]
        )
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    if data.get("keyAlgorithm") is not None:
        out["key_algorithm"] = data["keyAlgorithm"]
    if data.get("notAfter") is not None:
        import capo_lightsail.types.iso_date

        out["not_after"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["notAfter"]
        )
    if data.get("notBefore") is not None:
        import capo_lightsail.types.iso_date

        out["not_before"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["notBefore"]
        )
    if data.get("renewalSummary") is not None:
        import capo_lightsail.types.load_balancer_tls_certificate_renewal_summary

        out["renewal_summary"] = (
            capo_lightsail.types.load_balancer_tls_certificate_renewal_summary.deserialize_aws_json_1_1(
                data["renewalSummary"]
            )
        )
    if data.get("revocationReason") is not None:
        import capo_lightsail.types.load_balancer_tls_certificate_revocation_reason

        out["revocation_reason"] = (
            capo_lightsail.types.load_balancer_tls_certificate_revocation_reason.deserialize_aws_json_1_1(
                data["revocationReason"]
            )
        )
    if data.get("revokedAt") is not None:
        import capo_lightsail.types.iso_date

        out["revoked_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["revokedAt"]
        )
    if data.get("serial") is not None:
        out["serial"] = data["serial"]
    if data.get("signatureAlgorithm") is not None:
        out["signature_algorithm"] = data["signatureAlgorithm"]
    if data.get("subject") is not None:
        out["subject"] = data["subject"]
    if data.get("subjectAlternativeNames") is not None:
        import capo_lightsail.types.string_list

        out["subject_alternative_names"] = (
            capo_lightsail.types.string_list.deserialize_aws_json_1_1(
                data["subjectAlternativeNames"]
            )
        )
    return out
