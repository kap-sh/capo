"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateDistributionTenantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.customizations
    import capo_cloudfront.types.domain_list
    import capo_cloudfront.types.managed_certificate_request
    import capo_cloudfront.types.parameters
    import capo_cloudfront.types.string
    import capo_cloudfront.types.tags


class CreateDistributionTenantRequest(TypedDict, closed=True):
    distribution_id: "capo_cloudfront.types.string.string"
    """<p>The ID of the multi-tenant distribution to use for creating the distribution tenant.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>The name of the distribution tenant. Enter a friendly identifier that is unique within your Amazon Web Services account. This name can't be updated after you create the distribution tenant.</p>"""
    domains: "capo_cloudfront.types.domain_list.DomainList"
    """<p>The domains associated with the distribution tenant. You must specify at least one domain in the request.</p>"""
    tags: NotRequired["capo_cloudfront.types.tags.Tags"]
    customizations: NotRequired["capo_cloudfront.types.customizations.Customizations"]
    """<p>Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.</p>"""
    parameters: NotRequired["capo_cloudfront.types.parameters.Parameters"]
    """<p>A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.</p>"""
    connection_group_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the connection group to associate with the distribution tenant.</p>"""
    managed_certificate_request: NotRequired[
        "capo_cloudfront.types.managed_certificate_request.ManagedCertificateRequest"
    ]
    """<p>The configuration for the CloudFront managed ACM certificate request.</p>"""
    enabled: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>Indicates whether the distribution tenant should be enabled when created. If the distribution tenant is disabled, the distribution tenant won't serve traffic.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateDistributionTenantRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "DistributionId").text = str(value["distribution_id"])
    SubElement(el, "Name").text = str(value["name"])
    import capo_cloudfront.types.domain_list

    capo_cloudfront.types.domain_list.serialize_xml(value["domains"], el, "Domains")
    if "tags" in value:
        import capo_cloudfront.types.tags

        capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")
    if "customizations" in value:
        import capo_cloudfront.types.customizations

        capo_cloudfront.types.customizations.serialize_xml(
            value["customizations"], el, "Customizations"
        )
    if "parameters" in value:
        import capo_cloudfront.types.parameters

        capo_cloudfront.types.parameters.serialize_xml(
            value["parameters"], el, "Parameters"
        )
    if "connection_group_id" in value:
        SubElement(el, "ConnectionGroupId").text = str(value["connection_group_id"])
    if "managed_certificate_request" in value:
        import capo_cloudfront.types.managed_certificate_request

        capo_cloudfront.types.managed_certificate_request.serialize_xml(
            value["managed_certificate_request"], el, "ManagedCertificateRequest"
        )
    if "enabled" in value:
        SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"


def deserialize_xml(el: Element) -> CreateDistributionTenantRequest:
    out: CreateDistributionTenantRequest = {}  # type: ignore[typeddict-item]
    child_distribution_id = el.find("DistributionId")
    if child_distribution_id is not None:
        out["distribution_id"] = str(child_distribution_id.text or "")
    else:
        out["distribution_id"] = ""
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_domains = el.find("Domains")
    if child_domains is not None:
        import capo_cloudfront.types.domain_list

        out["domains"] = capo_cloudfront.types.domain_list.deserialize_xml(
            child_domains
        )
    else:
        out["domains"] = []
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    child_customizations = el.find("Customizations")
    if child_customizations is not None:
        import capo_cloudfront.types.customizations

        out["customizations"] = capo_cloudfront.types.customizations.deserialize_xml(
            child_customizations
        )
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_cloudfront.types.parameters

        out["parameters"] = capo_cloudfront.types.parameters.deserialize_xml(
            child_parameters
        )
    child_connection_group_id = el.find("ConnectionGroupId")
    if child_connection_group_id is not None:
        out["connection_group_id"] = str(child_connection_group_id.text or "")
    child_managed_certificate_request = el.find("ManagedCertificateRequest")
    if child_managed_certificate_request is not None:
        import capo_cloudfront.types.managed_certificate_request

        out["managed_certificate_request"] = (
            capo_cloudfront.types.managed_certificate_request.deserialize_xml(
                child_managed_certificate_request
            )
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
