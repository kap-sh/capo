"""Generated from Smithy shape ``com.amazonaws.route53domains#TransferDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.boolean
    import capo_route_53_domains.types.contact_detail
    import capo_route_53_domains.types.domain_auth_code
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.duration_in_years
    import capo_route_53_domains.types.lang_code
    import capo_route_53_domains.types.nameserver_list


class TransferDomainRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to transfer to Route 53. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>The domain name can contain only the following characters:</p> <ul> <li> <p>Letters a through z. Domain names are not case sensitive.</p> </li> <li> <p>Numbers 0 through 9.</p> </li> <li> <p>Hyphen (-). You can't specify a hyphen at the beginning or end of a label. </p> </li> <li> <p>Period (.) to separate the labels in the name, such as the <code>.</code> in <code>example.com</code>.</p> </li> </ul>"""
    idn_lang_code: NotRequired["capo_route_53_domains.types.lang_code.LangCode"]
    """<p>Reserved for future use.</p>"""
    duration_in_years: NotRequired[
        "capo_route_53_domains.types.duration_in_years.DurationInYears"
    ]
    """<p>Reserved for future use.</p> <p>Currently, the effect of a domain transfer on the registration period varies by TLD. For information about how transferring a domain affects the expiration date, see the Transfer Term column in the pricing information at <a href="http://aws.amazon.com/route53/pricing/">Amazon Route 53 Pricing</a>.</p> <p>Default: 1</p>"""
    nameservers: NotRequired[
        "capo_route_53_domains.types.nameserver_list.NameserverList"
    ]
    """<p>Contains details for the host and glue IP addresses.</p>"""
    auth_code: NotRequired[
        "capo_route_53_domains.types.domain_auth_code.DomainAuthCode"
    ]
    """<p>The authorization code for the domain. You get this value from the current registrar.</p>"""
    auto_renew: NotRequired["capo_route_53_domains.types.boolean.Boolean"]
    """<p>Indicates whether the domain will be automatically renewed (true) or not (false). Auto renewal only takes effect after the account is charged.</p> <p>Default: true</p>"""
    admin_contact: "capo_route_53_domains.types.contact_detail.ContactDetail"
    """<p>Provides detailed contact information.</p>"""
    registrant_contact: "capo_route_53_domains.types.contact_detail.ContactDetail"
    """<p>Provides detailed contact information.</p>"""
    tech_contact: "capo_route_53_domains.types.contact_detail.ContactDetail"
    """<p>Provides detailed contact information.</p>"""
    privacy_protect_admin_contact: NotRequired[
        "capo_route_53_domains.types.boolean.Boolean"
    ]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information for the registrar, the phrase "REDACTED FOR PRIVACY", or "On behalf of <domain name> owner.".</p> <note> <p>While some domains may allow different privacy settings per contact, we recommend specifying the same privacy setting for all contacts.</p> </note> <p>Default: <code>true</code> </p>"""
    privacy_protect_registrant_contact: NotRequired[
        "capo_route_53_domains.types.boolean.Boolean"
    ]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the registrant contact (domain owner).</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>"""
    privacy_protect_tech_contact: NotRequired[
        "capo_route_53_domains.types.boolean.Boolean"
    ]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the technical contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>"""
    billing_contact: NotRequired[
        "capo_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information.</p>"""
    privacy_protect_billing_contact: NotRequired[
        "capo_route_53_domains.types.boolean.Boolean"
    ]
    """<p> Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the billing contact. </p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransferDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "idn_lang_code" in value:
        out["IdnLangCode"] = value["idn_lang_code"]
    if "duration_in_years" in value:
        out["DurationInYears"] = value["duration_in_years"]
    if "nameservers" in value:
        import capo_route_53_domains.types.nameserver_list

        out["Nameservers"] = (
            capo_route_53_domains.types.nameserver_list.serialize_aws_json_1_1(
                value["nameservers"]
            )
        )
    if "auth_code" in value:
        out["AuthCode"] = value["auth_code"]
    if "auto_renew" in value:
        out["AutoRenew"] = value["auto_renew"]
    import capo_route_53_domains.types.contact_detail

    out["AdminContact"] = (
        capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
            value["admin_contact"]
        )
    )
    import capo_route_53_domains.types.contact_detail

    out["RegistrantContact"] = (
        capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
            value["registrant_contact"]
        )
    )
    import capo_route_53_domains.types.contact_detail

    out["TechContact"] = (
        capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
            value["tech_contact"]
        )
    )
    if "privacy_protect_admin_contact" in value:
        out["PrivacyProtectAdminContact"] = value["privacy_protect_admin_contact"]
    if "privacy_protect_registrant_contact" in value:
        out["PrivacyProtectRegistrantContact"] = value[
            "privacy_protect_registrant_contact"
        ]
    if "privacy_protect_tech_contact" in value:
        out["PrivacyProtectTechContact"] = value["privacy_protect_tech_contact"]
    if "billing_contact" in value:
        import capo_route_53_domains.types.contact_detail

        out["BillingContact"] = (
            capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["billing_contact"]
            )
        )
    if "privacy_protect_billing_contact" in value:
        out["PrivacyProtectBillingContact"] = value["privacy_protect_billing_contact"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransferDomainRequest:
    out: TransferDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("TransferDomainRequest.domain_name required")
    if data.get("IdnLangCode") is not None:
        out["idn_lang_code"] = data["IdnLangCode"]
    if data.get("DurationInYears") is not None:
        out["duration_in_years"] = data["DurationInYears"]
    if data.get("Nameservers") is not None:
        import capo_route_53_domains.types.nameserver_list

        out["nameservers"] = (
            capo_route_53_domains.types.nameserver_list.deserialize_aws_json_1_1(
                data["Nameservers"]
            )
        )
    if data.get("AuthCode") is not None:
        out["auth_code"] = data["AuthCode"]
    if data.get("AutoRenew") is not None:
        out["auto_renew"] = data["AutoRenew"]
    if data.get("AdminContact") is not None:
        import capo_route_53_domains.types.contact_detail

        out["admin_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["AdminContact"]
            )
        )
    else:
        raise DeserializationError("TransferDomainRequest.admin_contact required")
    if data.get("RegistrantContact") is not None:
        import capo_route_53_domains.types.contact_detail

        out["registrant_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["RegistrantContact"]
            )
        )
    else:
        raise DeserializationError("TransferDomainRequest.registrant_contact required")
    if data.get("TechContact") is not None:
        import capo_route_53_domains.types.contact_detail

        out["tech_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["TechContact"]
            )
        )
    else:
        raise DeserializationError("TransferDomainRequest.tech_contact required")
    if data.get("PrivacyProtectAdminContact") is not None:
        out["privacy_protect_admin_contact"] = data["PrivacyProtectAdminContact"]
    if data.get("PrivacyProtectRegistrantContact") is not None:
        out["privacy_protect_registrant_contact"] = data[
            "PrivacyProtectRegistrantContact"
        ]
    if data.get("PrivacyProtectTechContact") is not None:
        out["privacy_protect_tech_contact"] = data["PrivacyProtectTechContact"]
    if data.get("BillingContact") is not None:
        import capo_route_53_domains.types.contact_detail

        out["billing_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["BillingContact"]
            )
        )
    if data.get("PrivacyProtectBillingContact") is not None:
        out["privacy_protect_billing_contact"] = data["PrivacyProtectBillingContact"]
    return out
