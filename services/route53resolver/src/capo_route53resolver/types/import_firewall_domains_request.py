"""Generated from Smithy shape ``com.amazonaws.route53resolver#ImportFirewallDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.domain_list_file_url
    import capo_route53resolver.types.firewall_domain_import_operation
    import capo_route53resolver.types.resource_id


class ImportFirewallDomainsRequest(TypedDict, closed=True):
    firewall_domain_list_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the domain list that you want to modify with the import operation.</p>"""
    operation: "capo_route53resolver.types.firewall_domain_import_operation.FirewallDomainImportOperation"
    """<p>What you want DNS Firewall to do with the domains that are listed in the file. This must be set to <code>REPLACE</code>, which updates the domain list to exactly match the list in the file. </p>"""
    domain_file_url: "capo_route53resolver.types.domain_list_file_url.DomainListFileUrl"
    """<p>The fully qualified URL or URI of the file stored in Amazon Simple Storage Service (Amazon S3) that contains the list of domains to import.</p> <p>The file must be in an S3 bucket that's in the same Region as your DNS Firewall. The file must be a text file and must contain a single domain per line.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportFirewallDomainsRequest) -> dict:
    out: dict = {}
    out["FirewallDomainListId"] = value["firewall_domain_list_id"]
    import capo_route53resolver.types.firewall_domain_import_operation

    out["Operation"] = (
        capo_route53resolver.types.firewall_domain_import_operation.serialize_aws_json_1_1(
            value["operation"]
        )
    )
    out["DomainFileUrl"] = value["domain_file_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportFirewallDomainsRequest:
    out: ImportFirewallDomainsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallDomainListId") is not None:
        out["firewall_domain_list_id"] = data["FirewallDomainListId"]
    else:
        out["firewall_domain_list_id"] = ""
    if data.get("Operation") is not None:
        import capo_route53resolver.types.firewall_domain_import_operation

        out["operation"] = (
            capo_route53resolver.types.firewall_domain_import_operation.deserialize_aws_json_1_1(
                data["Operation"]
            )
        )
    else:
        import typing

        out["operation"] = typing.cast(
            "capo_route53resolver.types.firewall_domain_import_operation.FirewallDomainImportOperation",
            "",
        )
    if data.get("DomainFileUrl") is not None:
        out["domain_file_url"] = data["DomainFileUrl"]
    else:
        out["domain_file_url"] = ""
    return out
