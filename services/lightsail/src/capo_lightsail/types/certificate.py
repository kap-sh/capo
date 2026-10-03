"""Generated from Smithy shape ``com.amazonaws.lightsail#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.certificate_name
    import capo_lightsail.types.certificate_status
    import capo_lightsail.types.domain_name
    import capo_lightsail.types.domain_validation_record_list
    import capo_lightsail.types.eligible_to_renew
    import capo_lightsail.types.in_use_resource_count
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.issuer_ca
    import capo_lightsail.types.key_algorithm
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.renewal_summary
    import capo_lightsail.types.request_failure_reason
    import capo_lightsail.types.revocation_reason
    import capo_lightsail.types.serial_number
    import capo_lightsail.types.string
    import capo_lightsail.types.subject_alternative_name_list
    import capo_lightsail.types.tag_list


class Certificate(TypedDict, closed=True):
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    name: NotRequired["capo_lightsail.types.certificate_name.CertificateName"]
    """<p>The name of the certificate (<code>my-certificate</code>).</p>"""
    domain_name: NotRequired["capo_lightsail.types.domain_name.DomainName"]
    """<p>The domain name of the certificate.</p>"""
    status: NotRequired["capo_lightsail.types.certificate_status.CertificateStatus"]
    """<p>The validation status of the certificate.</p>"""
    serial_number: NotRequired["capo_lightsail.types.serial_number.SerialNumber"]
    """<p>The serial number of the certificate.</p>"""
    subject_alternative_names: NotRequired[
        "capo_lightsail.types.subject_alternative_name_list.SubjectAlternativeNameList"
    ]
    """<p>An array of strings that specify the alternate domains (<code>example2.com</code>) and subdomains (<code>blog.example.com</code>) of the certificate.</p>"""
    domain_validation_records: NotRequired[
        "capo_lightsail.types.domain_validation_record_list.DomainValidationRecordList"
    ]
    """<p>An array of objects that describe the domain validation records of the certificate.</p>"""
    request_failure_reason: NotRequired[
        "capo_lightsail.types.request_failure_reason.RequestFailureReason"
    ]
    """<p>The validation failure reason, if any, of the certificate.</p> <p>The following failure reasons are possible:</p> <ul> <li> <p> <b> <code>NO_AVAILABLE_CONTACTS</code> </b> - This failure applies to email validation, which is not available for Lightsail certificates.</p> </li> <li> <p> <b> <code>ADDITIONAL_VERIFICATION_REQUIRED</code> </b> - Lightsail requires additional information to process this certificate request. This can happen as a fraud-protection measure, such as when the domain ranks within the Alexa top 1000 websites. To provide the required information, use the <a href="https://console.aws.amazon.com/support/home">Amazon Web Services Support Center</a> to contact Amazon Web Services Support.</p> <note> <p>You cannot request a certificate for Amazon-owned domain names such as those ending in amazonaws.com, cloudfront.net, or elasticbeanstalk.com.</p> </note> </li> <li> <p> <b> <code>DOMAIN_NOT_ALLOWED</code> </b> - One or more of the domain names in the certificate request was reported as an unsafe domain by <a href="https://www.virustotal.com/gui/home/url">VirusTotal</a>. To correct the problem, search for your domain name on the <a href="https://www.virustotal.com/gui/home/url">VirusTotal</a> website. If your domain is reported as suspicious, see <a href="https://developers.google.com/web/fundamentals/security/hacked">Google Help for Hacked Websites</a> to learn what you can do.</p> <p>If you believe that the result is a false positive, notify the organization that is reporting the domain. VirusTotal is an aggregate of several antivirus and URL scanners and cannot remove your domain from a block list itself. After you correct the problem and the VirusTotal registry has been updated, request a new certificate.</p> <p>If you see this error and your domain is not included in the VirusTotal list, visit the <a href="https://console.aws.amazon.com/support/home">Amazon Web Services Support Center</a> and create a case.</p> </li> <li> <p> <b> <code>INVALID_PUBLIC_DOMAIN</code> </b> - One or more of the domain names in the certificate request is not valid. Typically, this is because a domain name in the request is not a valid top-level domain. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request, and ensure that all domain names in the request are for valid top-level domains. For example, you cannot request a certificate for <code>example.invalidpublicdomain</code> because <code>invalidpublicdomain</code> is not a valid top-level domain.</p> </li> <li> <p> <b> <code>OTHER</code> </b> - Typically, this failure occurs when there is a typographical error in one or more of the domain names in the certificate request. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request. </p> </li> </ul>"""
    in_use_resource_count: (
        "capo_lightsail.types.in_use_resource_count.InUseResourceCount"
    )
    """<p>The number of Lightsail resources that the certificate is attached to.</p>"""
    key_algorithm: NotRequired["capo_lightsail.types.key_algorithm.KeyAlgorithm"]
    """<p>The algorithm used to generate the key pair (the public and private key) of the certificate.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate was created.</p>"""
    issued_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate was issued.</p>"""
    issuer_ca: NotRequired["capo_lightsail.types.issuer_ca.IssuerCA"]
    """<p>The certificate authority that issued the certificate.</p>"""
    not_before: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate is first valid.</p>"""
    not_after: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate expires.</p>"""
    eligible_to_renew: NotRequired[
        "capo_lightsail.types.eligible_to_renew.EligibleToRenew"
    ]
    """<p>The renewal eligibility of the certificate.</p>"""
    renewal_summary: NotRequired["capo_lightsail.types.renewal_summary.RenewalSummary"]
    """<p>An object that describes the status of the certificate renewal managed by Lightsail.</p>"""
    revoked_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate was revoked. This value is present only when the certificate status is <code>REVOKED</code>.</p>"""
    revocation_reason: NotRequired[
        "capo_lightsail.types.revocation_reason.RevocationReason"
    ]
    """<p>The reason the certificate was revoked. This value is present only when the certificate status is <code>REVOKED</code>.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about your Lightsail certificate. This code enables our support team to look up your Lightsail information more easily.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Certificate) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "status" in value:
        import capo_lightsail.types.certificate_status

        out["status"] = capo_lightsail.types.certificate_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "serial_number" in value:
        out["serialNumber"] = value["serial_number"]
    if "subject_alternative_names" in value:
        import capo_lightsail.types.subject_alternative_name_list

        out["subjectAlternativeNames"] = (
            capo_lightsail.types.subject_alternative_name_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "domain_validation_records" in value:
        import capo_lightsail.types.domain_validation_record_list

        out["domainValidationRecords"] = (
            capo_lightsail.types.domain_validation_record_list.serialize_aws_json_1_1(
                value["domain_validation_records"]
            )
        )
    if "request_failure_reason" in value:
        out["requestFailureReason"] = value["request_failure_reason"]
    out["inUseResourceCount"] = value.get("in_use_resource_count", 0)
    if "key_algorithm" in value:
        out["keyAlgorithm"] = value["key_algorithm"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "issued_at" in value:
        import capo_lightsail.types.iso_date

        out["issuedAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["issued_at"]
        )
    if "issuer_ca" in value:
        out["issuerCA"] = value["issuer_ca"]
    if "not_before" in value:
        import capo_lightsail.types.iso_date

        out["notBefore"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["not_before"]
        )
    if "not_after" in value:
        import capo_lightsail.types.iso_date

        out["notAfter"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["not_after"]
        )
    if "eligible_to_renew" in value:
        out["eligibleToRenew"] = value["eligible_to_renew"]
    if "renewal_summary" in value:
        import capo_lightsail.types.renewal_summary

        out["renewalSummary"] = (
            capo_lightsail.types.renewal_summary.serialize_aws_json_1_1(
                value["renewal_summary"]
            )
        )
    if "revoked_at" in value:
        import capo_lightsail.types.iso_date

        out["revokedAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["revoked_at"]
        )
    if "revocation_reason" in value:
        out["revocationReason"] = value["revocation_reason"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("status") is not None:
        import capo_lightsail.types.certificate_status

        out["status"] = (
            capo_lightsail.types.certificate_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("serialNumber") is not None:
        out["serial_number"] = data["serialNumber"]
    if data.get("subjectAlternativeNames") is not None:
        import capo_lightsail.types.subject_alternative_name_list

        out["subject_alternative_names"] = (
            capo_lightsail.types.subject_alternative_name_list.deserialize_aws_json_1_1(
                data["subjectAlternativeNames"]
            )
        )
    if data.get("domainValidationRecords") is not None:
        import capo_lightsail.types.domain_validation_record_list

        out["domain_validation_records"] = (
            capo_lightsail.types.domain_validation_record_list.deserialize_aws_json_1_1(
                data["domainValidationRecords"]
            )
        )
    if data.get("requestFailureReason") is not None:
        out["request_failure_reason"] = data["requestFailureReason"]
    if data.get("inUseResourceCount") is not None:
        out["in_use_resource_count"] = data["inUseResourceCount"]
    else:
        out["in_use_resource_count"] = 0
    if data.get("keyAlgorithm") is not None:
        out["key_algorithm"] = data["keyAlgorithm"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("issuedAt") is not None:
        import capo_lightsail.types.iso_date

        out["issued_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["issuedAt"]
        )
    if data.get("issuerCA") is not None:
        out["issuer_ca"] = data["issuerCA"]
    if data.get("notBefore") is not None:
        import capo_lightsail.types.iso_date

        out["not_before"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["notBefore"]
        )
    if data.get("notAfter") is not None:
        import capo_lightsail.types.iso_date

        out["not_after"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["notAfter"]
        )
    if data.get("eligibleToRenew") is not None:
        out["eligible_to_renew"] = data["eligibleToRenew"]
    if data.get("renewalSummary") is not None:
        import capo_lightsail.types.renewal_summary

        out["renewal_summary"] = (
            capo_lightsail.types.renewal_summary.deserialize_aws_json_1_1(
                data["renewalSummary"]
            )
        )
    if data.get("revokedAt") is not None:
        import capo_lightsail.types.iso_date

        out["revoked_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["revokedAt"]
        )
    if data.get("revocationReason") is not None:
        out["revocation_reason"] = data["revocationReason"]
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("supportCode") is not None:
        out["support_code"] = data["supportCode"]
    return out
