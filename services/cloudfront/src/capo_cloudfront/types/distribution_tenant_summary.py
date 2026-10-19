"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionTenantSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.customizations
    import capo_cloudfront.types.domain_result_list
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class DistributionTenantSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The ID of the distribution tenant.</p>"""
    distribution_id: "capo_cloudfront.types.string.string"
    """<p>The identifier for the multi-tenant distribution. For example: <code>EDFDVBD632BHDS5</code>.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>The name of the distribution tenant.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the distribution tenant.</p>"""
    domains: "capo_cloudfront.types.domain_result_list.DomainResultList"
    """<p>The domains associated with the distribution tenant.</p>"""
    connection_group_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the connection group ID for the distribution tenant. If you don't specify a connection group, CloudFront uses the default connection group.</p>"""
    customizations: NotRequired["capo_cloudfront.types.customizations.Customizations"]
    """<p>Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.</p>"""
    created_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the distribution tenant was created.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the distribution tenant was updated.</p>"""
    e_tag: "capo_cloudfront.types.string.string"
    """<p>The current version of the distribution tenant.</p>"""
    enabled: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>Indicates whether the distribution tenants are in an enabled state. If disabled, the distribution tenant won't service traffic.</p>"""
    status: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The status of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DistributionTenantSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "DistributionId").text = str(value["distribution_id"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Arn").text = str(value["arn"])
    import capo_cloudfront.types.domain_result_list

    capo_cloudfront.types.domain_result_list.serialize_xml(
        value["domains"], el, "Domains"
    )
    if "connection_group_id" in value:
        SubElement(el, "ConnectionGroupId").text = str(value["connection_group_id"])
    if "customizations" in value:
        import capo_cloudfront.types.customizations

        capo_cloudfront.types.customizations.serialize_xml(
            value["customizations"], el, "Customizations"
        )
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["created_time"], el, "CreatedTime"
    )
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    SubElement(el, "ETag").text = str(value["e_tag"])
    if "enabled" in value:
        SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    if "status" in value:
        SubElement(el, "Status").text = str(value["status"])


def deserialize_xml(el: Element) -> DistributionTenantSummary:
    out: DistributionTenantSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
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
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        out["arn"] = ""
    child_domains = el.find("Domains")
    if child_domains is not None:
        import capo_cloudfront.types.domain_result_list

        out["domains"] = capo_cloudfront.types.domain_result_list.deserialize_xml(
            child_domains
        )
    else:
        out["domains"] = []
    child_connection_group_id = el.find("ConnectionGroupId")
    if child_connection_group_id is not None:
        out["connection_group_id"] = str(child_connection_group_id.text or "")
    child_customizations = el.find("Customizations")
    if child_customizations is not None:
        import capo_cloudfront.types.customizations

        out["customizations"] = capo_cloudfront.types.customizations.deserialize_xml(
            child_customizations
        )
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_cloudfront.types.timestamp

        out["created_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    else:
        out["e_tag"] = ""
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
