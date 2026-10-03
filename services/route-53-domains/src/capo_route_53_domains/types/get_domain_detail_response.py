"""Generated from Smithy shape ``com.amazonaws.route53domains#GetDomainDetailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.boolean
    import capo_route_53_domains.types.contact_detail
    import capo_route_53_domains.types.contact_number
    import capo_route_53_domains.types.dns_sec
    import capo_route_53_domains.types.dnssec_key_list
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.domain_status_list
    import capo_route_53_domains.types.email
    import capo_route_53_domains.types.nameserver_list
    import capo_route_53_domains.types.registrar_name
    import capo_route_53_domains.types.registrar_url
    import capo_route_53_domains.types.registrar_who_is_server
    import capo_route_53_domains.types.registry_domain_id
    import capo_route_53_domains.types.reseller
    import capo_route_53_domains.types.timestamp


class GetDomainDetailResponse(TypedDict, closed=True):
    domain_name: NotRequired["capo_route_53_domains.types.domain_name.DomainName"]
    """<p>The name of a domain.</p>"""
    nameservers: NotRequired[
        "capo_route_53_domains.types.nameserver_list.NameserverList"
    ]
    """<p>The name servers of the domain.</p>"""
    auto_renew: NotRequired["capo_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether the domain registration is set to renew automatically.</p>"""
    admin_contact: NotRequired[
        "capo_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides details about the domain administrative contact.</p>"""
    registrant_contact: NotRequired[
        "capo_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides details about the domain registrant.</p>"""
    tech_contact: NotRequired[
        "capo_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides details about the domain technical contact.</p>"""
    admin_privacy: NotRequired["capo_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether contact information is concealed from WHOIS queries. If the value is <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is <code>false</code>, WHOIS queries return the information that you entered for the admin contact.</p>"""
    registrant_privacy: NotRequired["capo_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether contact information is concealed from WHOIS queries. If the value is <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is <code>false</code>, WHOIS queries return the information that you entered for the registrant contact (domain owner).</p>"""
    tech_privacy: NotRequired["capo_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether contact information is concealed from WHOIS queries. If the value is <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is <code>false</code>, WHOIS queries return the information that you entered for the technical contact.</p>"""
    registrar_name: NotRequired[
        "capo_route_53_domains.types.registrar_name.RegistrarName"
    ]
    """<p>Name of the registrar of the domain as identified in the registry. </p>"""
    who_is_server: NotRequired[
        "capo_route_53_domains.types.registrar_who_is_server.RegistrarWhoIsServer"
    ]
    """<p>The fully qualified name of the WHOIS server that can answer the WHOIS query for the domain.</p>"""
    registrar_url: NotRequired["capo_route_53_domains.types.registrar_url.RegistrarUrl"]
    """<p>Web address of the registrar.</p>"""
    abuse_contact_email: NotRequired["capo_route_53_domains.types.email.Email"]
    """<p>Email address to contact to report incorrect contact information for a domain, to report that the domain is being used to send spam, to report that someone is cybersquatting on a domain name, or report some other type of abuse.</p>"""
    abuse_contact_phone: NotRequired[
        "capo_route_53_domains.types.contact_number.ContactNumber"
    ]
    """<p>Phone number for reporting abuse.</p>"""
    registry_domain_id: NotRequired[
        "capo_route_53_domains.types.registry_domain_id.RegistryDomainId"
    ]
    """<p>Reserved for future use.</p>"""
    creation_date: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p>The date when the domain was created as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).</p>"""
    updated_date: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p>The last updated date of the domain as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).</p>"""
    expiration_date: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p>The date when the registration for the domain is set to expire. The date and time is in Unix time format and Coordinated Universal time (UTC).</p>"""
    reseller: NotRequired["capo_route_53_domains.types.reseller.Reseller"]
    """<p>Reserved for future use.</p>"""
    dns_sec: NotRequired["capo_route_53_domains.types.dns_sec.DNSSec"]
    """<p>Deprecated.</p>"""
    status_list: NotRequired[
        "capo_route_53_domains.types.domain_status_list.DomainStatusList"
    ]
    """<p>An array of domain name status codes, also known as Extensible Provisioning Protocol (EPP) status codes.</p> <p>ICANN, the organization that maintains a central database of domain names, has developed a set of domain name status codes that tell you the status of a variety of operations on a domain name, for example, registering a domain name, transferring a domain name to another registrar, renewing the registration for a domain name, and so on. All registrars use this same set of status codes.</p> <p>For a current list of domain name status codes and an explanation of what each code means, go to the <a href="https://www.icann.org/">ICANN website</a> and search for <code>epp status codes</code>. (Search on the ICANN website; web searches sometimes return an old version of the document.)</p>"""
    dnssec_keys: NotRequired[
        "capo_route_53_domains.types.dnssec_key_list.DnssecKeyList"
    ]
    """<p>A complex type that contains information about the DNSSEC configuration.</p>"""
    billing_contact: NotRequired[
        "capo_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides details about the domain billing contact.</p>"""
    billing_privacy: NotRequired["capo_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether contact information is concealed from WHOIS queries. If the value is <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is <code>false</code>, WHOIS queries return the information that you entered for the billing contact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainDetailResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "nameservers" in value:
        import capo_route_53_domains.types.nameserver_list

        out["Nameservers"] = (
            capo_route_53_domains.types.nameserver_list.serialize_aws_json_1_1(
                value["nameservers"]
            )
        )
    if "auto_renew" in value:
        out["AutoRenew"] = value["auto_renew"]
    if "admin_contact" in value:
        import capo_route_53_domains.types.contact_detail

        out["AdminContact"] = (
            capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["admin_contact"]
            )
        )
    if "registrant_contact" in value:
        import capo_route_53_domains.types.contact_detail

        out["RegistrantContact"] = (
            capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["registrant_contact"]
            )
        )
    if "tech_contact" in value:
        import capo_route_53_domains.types.contact_detail

        out["TechContact"] = (
            capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["tech_contact"]
            )
        )
    if "admin_privacy" in value:
        out["AdminPrivacy"] = value["admin_privacy"]
    if "registrant_privacy" in value:
        out["RegistrantPrivacy"] = value["registrant_privacy"]
    if "tech_privacy" in value:
        out["TechPrivacy"] = value["tech_privacy"]
    if "registrar_name" in value:
        out["RegistrarName"] = value["registrar_name"]
    if "who_is_server" in value:
        out["WhoIsServer"] = value["who_is_server"]
    if "registrar_url" in value:
        out["RegistrarUrl"] = value["registrar_url"]
    if "abuse_contact_email" in value:
        out["AbuseContactEmail"] = value["abuse_contact_email"]
    if "abuse_contact_phone" in value:
        out["AbuseContactPhone"] = value["abuse_contact_phone"]
    if "registry_domain_id" in value:
        out["RegistryDomainId"] = value["registry_domain_id"]
    if "creation_date" in value:
        import capo_route_53_domains.types.timestamp

        out["CreationDate"] = (
            capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "updated_date" in value:
        import capo_route_53_domains.types.timestamp

        out["UpdatedDate"] = (
            capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["updated_date"]
            )
        )
    if "expiration_date" in value:
        import capo_route_53_domains.types.timestamp

        out["ExpirationDate"] = (
            capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["expiration_date"]
            )
        )
    if "reseller" in value:
        out["Reseller"] = value["reseller"]
    if "dns_sec" in value:
        out["DnsSec"] = value["dns_sec"]
    if "status_list" in value:
        import capo_route_53_domains.types.domain_status_list

        out["StatusList"] = (
            capo_route_53_domains.types.domain_status_list.serialize_aws_json_1_1(
                value["status_list"]
            )
        )
    if "dnssec_keys" in value:
        import capo_route_53_domains.types.dnssec_key_list

        out["DnssecKeys"] = (
            capo_route_53_domains.types.dnssec_key_list.serialize_aws_json_1_1(
                value["dnssec_keys"]
            )
        )
    if "billing_contact" in value:
        import capo_route_53_domains.types.contact_detail

        out["BillingContact"] = (
            capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["billing_contact"]
            )
        )
    if "billing_privacy" in value:
        out["BillingPrivacy"] = value["billing_privacy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainDetailResponse:
    out: GetDomainDetailResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("Nameservers") is not None:
        import capo_route_53_domains.types.nameserver_list

        out["nameservers"] = (
            capo_route_53_domains.types.nameserver_list.deserialize_aws_json_1_1(
                data["Nameservers"]
            )
        )
    if data.get("AutoRenew") is not None:
        out["auto_renew"] = data["AutoRenew"]
    if data.get("AdminContact") is not None:
        import capo_route_53_domains.types.contact_detail

        out["admin_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["AdminContact"]
            )
        )
    if data.get("RegistrantContact") is not None:
        import capo_route_53_domains.types.contact_detail

        out["registrant_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["RegistrantContact"]
            )
        )
    if data.get("TechContact") is not None:
        import capo_route_53_domains.types.contact_detail

        out["tech_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["TechContact"]
            )
        )
    if data.get("AdminPrivacy") is not None:
        out["admin_privacy"] = data["AdminPrivacy"]
    if data.get("RegistrantPrivacy") is not None:
        out["registrant_privacy"] = data["RegistrantPrivacy"]
    if data.get("TechPrivacy") is not None:
        out["tech_privacy"] = data["TechPrivacy"]
    if data.get("RegistrarName") is not None:
        out["registrar_name"] = data["RegistrarName"]
    if data.get("WhoIsServer") is not None:
        out["who_is_server"] = data["WhoIsServer"]
    if data.get("RegistrarUrl") is not None:
        out["registrar_url"] = data["RegistrarUrl"]
    if data.get("AbuseContactEmail") is not None:
        out["abuse_contact_email"] = data["AbuseContactEmail"]
    if data.get("AbuseContactPhone") is not None:
        out["abuse_contact_phone"] = data["AbuseContactPhone"]
    if data.get("RegistryDomainId") is not None:
        out["registry_domain_id"] = data["RegistryDomainId"]
    if data.get("CreationDate") is not None:
        import capo_route_53_domains.types.timestamp

        out["creation_date"] = (
            capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if data.get("UpdatedDate") is not None:
        import capo_route_53_domains.types.timestamp

        out["updated_date"] = (
            capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["UpdatedDate"]
            )
        )
    if data.get("ExpirationDate") is not None:
        import capo_route_53_domains.types.timestamp

        out["expiration_date"] = (
            capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationDate"]
            )
        )
    if data.get("Reseller") is not None:
        out["reseller"] = data["Reseller"]
    if data.get("DnsSec") is not None:
        out["dns_sec"] = data["DnsSec"]
    if data.get("StatusList") is not None:
        import capo_route_53_domains.types.domain_status_list

        out["status_list"] = (
            capo_route_53_domains.types.domain_status_list.deserialize_aws_json_1_1(
                data["StatusList"]
            )
        )
    if data.get("DnssecKeys") is not None:
        import capo_route_53_domains.types.dnssec_key_list

        out["dnssec_keys"] = (
            capo_route_53_domains.types.dnssec_key_list.deserialize_aws_json_1_1(
                data["DnssecKeys"]
            )
        )
    if data.get("BillingContact") is not None:
        import capo_route_53_domains.types.contact_detail

        out["billing_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["BillingContact"]
            )
        )
    if data.get("BillingPrivacy") is not None:
        out["billing_privacy"] = data["BillingPrivacy"]
    return out
