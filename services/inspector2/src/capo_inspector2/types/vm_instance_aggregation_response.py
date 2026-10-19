"""Generated from Smithy shape ``com.amazonaws.inspector2#VmInstanceAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.provider
    import capo_inspector2.types.provider_account_id
    import capo_inspector2.types.provider_org_id
    import capo_inspector2.types.provider_partition
    import capo_inspector2.types.provider_region
    import capo_inspector2.types.severity_counts
    import capo_inspector2.types.tag_map


class VmInstanceAggregationResponse(TypedDict, closed=True):
    resource_id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The resource ID for the VM instance.</p>"""
    cloud_provider: NotRequired["capo_inspector2.types.provider.Provider"]
    """<p>The cloud service provider associated with this VM instance aggregation. Valid values:</p> <ul> <li> <p> <code>AWS</code> – Findings from Amazon Web Services resources.</p> </li> <li> <p> <code>AZURE</code> – Findings from Microsoft Azure resources.</p> </li> </ul>"""
    cloud_account_id: NotRequired[
        "capo_inspector2.types.provider_account_id.ProviderAccountId"
    ]
    """<p>The cloud account ID for the VM instance aggregation.</p>"""
    cloud_partition: NotRequired[
        "capo_inspector2.types.provider_partition.ProviderPartition"
    ]
    """<p>The cloud infrastructure partition associated with this VM instance aggregation. Valid values:</p> <ul> <li> <p> <code>aws</code> – Amazon Web Services commercial Regions.</p> </li> <li> <p> <code>aws-cn</code> – Amazon Web Services China Regions.</p> </li> <li> <p> <code>aws-us-gov</code> – Amazon Web Services GovCloud (US) Regions.</p> </li> <li> <p> <code>AzureCloud</code> – Azure commercial Regions.</p> </li> </ul>"""
    cloud_region: NotRequired["capo_inspector2.types.provider_region.ProviderRegion"]
    """<p>The cloud Region associated with this VM instance aggregation. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services Region, such as <code>us-east-1</code>.</p> </li> <li> <p>An Azure region, such as <code>eastus</code>.</p> </li> </ul>"""
    cloud_org_id: NotRequired["capo_inspector2.types.provider_org_id.ProviderOrgId"]
    """<p>The cloud organization ID for the VM instance aggregation.</p>"""
    vm_image_reference: NotRequired["str"]
    """<p>The VM image reference for the VM instance.</p>"""
    operating_system: NotRequired["str"]
    """<p>The operating system of the VM instance.</p>"""
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags attached to the VM instance.</p>"""
    account_id: NotRequired["str"]
    """<p>The account ID associated with the VM instance.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    network_findings: NotRequired["int"]
    """<p>The number of network findings for the VM instance. This field applies only to Amazon Web Services resources.</p>"""
    exploit_available_active_findings_count: NotRequired["int"]
    """<p>The number of active findings with an exploit available for the VM instance.</p>"""
    fix_available_active_findings_count: NotRequired["int"]
    """<p>The number of active findings with a fix available for the VM instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VmInstanceAggregationResponse) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    if "cloud_provider" in value:
        out["cloudProvider"] = value["cloud_provider"]
    if "cloud_account_id" in value:
        out["cloudAccountId"] = value["cloud_account_id"]
    if "cloud_partition" in value:
        out["cloudPartition"] = value["cloud_partition"]
    if "cloud_region" in value:
        out["cloudRegion"] = value["cloud_region"]
    if "cloud_org_id" in value:
        out["cloudOrgId"] = value["cloud_org_id"]
    if "vm_image_reference" in value:
        out["vmImageReference"] = value["vm_image_reference"]
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "network_findings" in value:
        out["networkFindings"] = value["network_findings"]
    if "exploit_available_active_findings_count" in value:
        out["exploitAvailableActiveFindingsCount"] = value[
            "exploit_available_active_findings_count"
        ]
    if "fix_available_active_findings_count" in value:
        out["fixAvailableActiveFindingsCount"] = value[
            "fix_available_active_findings_count"
        ]
    return out


def deserialize_json(data: dict) -> VmInstanceAggregationResponse:
    out: VmInstanceAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("cloudProvider") is not None:
        out["cloud_provider"] = data["cloudProvider"]
    if data.get("cloudAccountId") is not None:
        out["cloud_account_id"] = data["cloudAccountId"]
    if data.get("cloudPartition") is not None:
        out["cloud_partition"] = data["cloudPartition"]
    if data.get("cloudRegion") is not None:
        out["cloud_region"] = data["cloudRegion"]
    if data.get("cloudOrgId") is not None:
        out["cloud_org_id"] = data["cloudOrgId"]
    if data.get("vmImageReference") is not None:
        out["vm_image_reference"] = data["vmImageReference"]
    if data.get("operatingSystem") is not None:
        out["operating_system"] = data["operatingSystem"]
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if data.get("networkFindings") is not None:
        out["network_findings"] = data["networkFindings"]
    if data.get("exploitAvailableActiveFindingsCount") is not None:
        out["exploit_available_active_findings_count"] = data[
            "exploitAvailableActiveFindingsCount"
        ]
    if data.get("fixAvailableActiveFindingsCount") is not None:
        out["fix_available_active_findings_count"] = data[
            "fixAvailableActiveFindingsCount"
        ]
    return out
