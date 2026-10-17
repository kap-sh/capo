"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.discovery_type
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.resource_category
    import capo_securityhub.types.resource_config
    import capo_securityhub.types.resource_findings_summary_list
    import capo_securityhub.types.resource_info
    import capo_securityhub.types.resource_sub_category
    import capo_securityhub.types.resource_tag_list


class ResourceResult(TypedDict, closed=True):
    resource_guid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The global identifier used to identify a resource.</p>"""
    resource_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for a resource.</p>"""
    account_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account that recorded the resource data in Security Hub.</p>"""
    account_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Amazon Web Services account that's associated with the resource.</p>"""
    region: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region that recorded the resource data in Security Hub.</p>"""
    resource_provider: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The cloud provider where the resource exists. Valid values are <code>AWS</code> and <code>Azure</code>. This field is always included.</p>"""
    resource_owner_account_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the cloud account that owns the resource. For Amazon Web Services resources, this is the Amazon Web Services account ID. For Azure resources, this is the Azure subscription ID.</p>"""
    resource_owner_org_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the cloud organization that owns the resource. For Amazon Web Services resources, this is the Organizations ID. For Azure resources, this is the Azure tenant ID.</p>"""
    resource_cloud_partition: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The cloud partition where the resource exists. For Amazon Web Services, valid values include <code>aws</code>, <code>aws-cn</code>, and <code>aws-us-gov</code>. This field isn't returned for cloud providers that don't use partitions.</p>"""
    resource_region: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The native cloud region where the resource is located. For Amazon Web Services, this is an Amazon Web Services Region (for example, <code>us-east-1</code>). For Azure resources, this is the Azure region (for example, <code>westus2</code>). This field is always included.</p>"""
    resource_category: NotRequired[
        "capo_securityhub.types.resource_category.ResourceCategory"
    ]
    """<p>The grouping where the resource belongs.</p>"""
    resource_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of resource.</p>"""
    resource_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the resource.</p>"""
    resource_creation_time_dt: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The time when the resource was created.</p>"""
    resource_detail_capture_time_dt: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The timestamp when information about the resource was captured.</p>"""
    findings_summary: NotRequired[
        "capo_securityhub.types.resource_findings_summary_list.ResourceFindingsSummaryList"
    ]
    """<p>An aggregated view of security findings associated with a resource.</p>"""
    resource_tags: NotRequired[
        "capo_securityhub.types.resource_tag_list.ResourceTagList"
    ]
    """<p>The key-value pairs associated with a resource.</p>"""
    resource_config: NotRequired[
        "capo_securityhub.types.resource_config.ResourceConfig"
    ]
    """<p>The configuration details of a resource.</p>"""
    resource_sub_category: NotRequired[
        "capo_securityhub.types.resource_sub_category.ResourceSubCategory"
    ]
    """<p>The AI/ML sub-grouping of the resource. Present only when <code>ResourceCategory</code> is <code>AI/ML</code>.</p>"""
    discovery_type: NotRequired["capo_securityhub.types.discovery_type.DiscoveryType"]
    """<p>Specifies how the resource was discovered. If the value is <code>Managed</code>, the resource is natively provided by a cloud service provider. If the value is <code>SelfHosted</code>, the resource is hosted on customer-managed infrastructure, such as a compute instance or container image.</p>"""
    resource_info: NotRequired["capo_securityhub.types.resource_info.ResourceInfo"]
    """<p>Additional resource-type-specific details. For self-hosted AI resources and their host resources, contains an <code>AIDetails</code> structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceResult) -> dict:
    out: dict = {}
    if "resource_guid" in value:
        out["ResourceGuid"] = value["resource_guid"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "region" in value:
        out["Region"] = value["region"]
    if "resource_provider" in value:
        out["ResourceProvider"] = value["resource_provider"]
    if "resource_owner_account_id" in value:
        out["ResourceOwnerAccountId"] = value["resource_owner_account_id"]
    if "resource_owner_org_id" in value:
        out["ResourceOwnerOrgId"] = value["resource_owner_org_id"]
    if "resource_cloud_partition" in value:
        out["ResourceCloudPartition"] = value["resource_cloud_partition"]
    if "resource_region" in value:
        out["ResourceRegion"] = value["resource_region"]
    if "resource_category" in value:
        import capo_securityhub.types.resource_category

        out["ResourceCategory"] = (
            capo_securityhub.types.resource_category.serialize_json(
                value["resource_category"]
            )
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "resource_creation_time_dt" in value:
        out["ResourceCreationTimeDt"] = value["resource_creation_time_dt"]
    if "resource_detail_capture_time_dt" in value:
        out["ResourceDetailCaptureTimeDt"] = value["resource_detail_capture_time_dt"]
    if "findings_summary" in value:
        import capo_securityhub.types.resource_findings_summary_list

        out["FindingsSummary"] = (
            capo_securityhub.types.resource_findings_summary_list.serialize_json(
                value["findings_summary"]
            )
        )
    if "resource_tags" in value:
        import capo_securityhub.types.resource_tag_list

        out["ResourceTags"] = capo_securityhub.types.resource_tag_list.serialize_json(
            value["resource_tags"]
        )
    if "resource_config" in value:
        out["ResourceConfig"] = value["resource_config"]
    if "resource_sub_category" in value:
        import capo_securityhub.types.resource_sub_category

        out["ResourceSubCategory"] = (
            capo_securityhub.types.resource_sub_category.serialize_json(
                value["resource_sub_category"]
            )
        )
    if "discovery_type" in value:
        import capo_securityhub.types.discovery_type

        out["DiscoveryType"] = capo_securityhub.types.discovery_type.serialize_json(
            value["discovery_type"]
        )
    if "resource_info" in value:
        import capo_securityhub.types.resource_info

        out["ResourceInfo"] = capo_securityhub.types.resource_info.serialize_json(
            value["resource_info"]
        )
    return out


def deserialize_json(data: dict) -> ResourceResult:
    out: ResourceResult = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGuid") is not None:
        out["resource_guid"] = data["ResourceGuid"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("AccountName") is not None:
        out["account_name"] = data["AccountName"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("ResourceProvider") is not None:
        out["resource_provider"] = data["ResourceProvider"]
    if data.get("ResourceOwnerAccountId") is not None:
        out["resource_owner_account_id"] = data["ResourceOwnerAccountId"]
    if data.get("ResourceOwnerOrgId") is not None:
        out["resource_owner_org_id"] = data["ResourceOwnerOrgId"]
    if data.get("ResourceCloudPartition") is not None:
        out["resource_cloud_partition"] = data["ResourceCloudPartition"]
    if data.get("ResourceRegion") is not None:
        out["resource_region"] = data["ResourceRegion"]
    if data.get("ResourceCategory") is not None:
        import capo_securityhub.types.resource_category

        out["resource_category"] = (
            capo_securityhub.types.resource_category.deserialize_json(
                data["ResourceCategory"]
            )
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    if data.get("ResourceCreationTimeDt") is not None:
        out["resource_creation_time_dt"] = data["ResourceCreationTimeDt"]
    if data.get("ResourceDetailCaptureTimeDt") is not None:
        out["resource_detail_capture_time_dt"] = data["ResourceDetailCaptureTimeDt"]
    if data.get("FindingsSummary") is not None:
        import capo_securityhub.types.resource_findings_summary_list

        out["findings_summary"] = (
            capo_securityhub.types.resource_findings_summary_list.deserialize_json(
                data["FindingsSummary"]
            )
        )
    if data.get("ResourceTags") is not None:
        import capo_securityhub.types.resource_tag_list

        out["resource_tags"] = (
            capo_securityhub.types.resource_tag_list.deserialize_json(
                data["ResourceTags"]
            )
        )
    if data.get("ResourceConfig") is not None:
        out["resource_config"] = data["ResourceConfig"]
    if data.get("ResourceSubCategory") is not None:
        import capo_securityhub.types.resource_sub_category

        out["resource_sub_category"] = (
            capo_securityhub.types.resource_sub_category.deserialize_json(
                data["ResourceSubCategory"]
            )
        )
    if data.get("DiscoveryType") is not None:
        import capo_securityhub.types.discovery_type

        out["discovery_type"] = capo_securityhub.types.discovery_type.deserialize_json(
            data["DiscoveryType"]
        )
    if data.get("ResourceInfo") is not None:
        import capo_securityhub.types.resource_info

        out["resource_info"] = capo_securityhub.types.resource_info.deserialize_json(
            data["ResourceInfo"]
        )
    return out
