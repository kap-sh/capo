"""Generated from Smithy shape ``com.amazonaws.inspector2#ContainerImageAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.provider
    import capo_inspector2.types.provider_account_id
    import capo_inspector2.types.provider_org_id
    import capo_inspector2.types.provider_partition
    import capo_inspector2.types.provider_region
    import capo_inspector2.types.severity_counts
    import capo_inspector2.types.string_list


class ContainerImageAggregationResponse(TypedDict, closed=True):
    resource_id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The resource ID for the container image.</p>"""
    cloud_provider: NotRequired["capo_inspector2.types.provider.Provider"]
    """<p>The cloud service provider associated with this container image aggregation. Valid values:</p> <ul> <li> <p> <code>AWS</code> – Findings from Amazon Web Services resources.</p> </li> <li> <p> <code>AZURE</code> – Findings from Microsoft Azure resources.</p> </li> </ul>"""
    cloud_account_id: NotRequired[
        "capo_inspector2.types.provider_account_id.ProviderAccountId"
    ]
    """<p>The cloud account ID for the container image aggregation.</p>"""
    cloud_partition: NotRequired[
        "capo_inspector2.types.provider_partition.ProviderPartition"
    ]
    """<p>The cloud infrastructure partition associated with this container image aggregation. Valid values:</p> <ul> <li> <p> <code>aws</code> – Amazon Web Services commercial Regions.</p> </li> <li> <p> <code>aws-cn</code> – Amazon Web Services China Regions.</p> </li> <li> <p> <code>aws-us-gov</code> – Amazon Web Services GovCloud (US) Regions.</p> </li> <li> <p> <code>AzureCloud</code> – Azure commercial Regions.</p> </li> </ul>"""
    cloud_region: NotRequired["capo_inspector2.types.provider_region.ProviderRegion"]
    """<p>The cloud Region associated with this container image aggregation. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services Region, such as <code>us-east-1</code>.</p> </li> <li> <p>An Azure region, such as <code>eastus</code>.</p> </li> </ul>"""
    cloud_org_id: NotRequired["capo_inspector2.types.provider_org_id.ProviderOrgId"]
    """<p>The cloud organization ID for the container image aggregation.</p>"""
    image_digest: NotRequired["str"]
    """<p>The image digest for the container image.</p>"""
    repository: NotRequired["str"]
    """<p>The repository for the container image.</p>"""
    registry: NotRequired["str"]
    """<p>The registry for the container image.</p>"""
    architecture: NotRequired["str"]
    """<p>The architecture of the container image.</p>"""
    image_tags: NotRequired["capo_inspector2.types.string_list.StringList"]
    """<p>The image tags attached to the container image.</p>"""
    account_id: NotRequired["str"]
    """<p>The account ID associated with the container image.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    last_in_use_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The last time the container image was in use.</p>"""
    in_use_count: NotRequired["int"]
    """<p>The number of times the container image is in use.</p>"""
    exploit_available_active_findings_count: NotRequired["int"]
    """<p>The number of active findings with an exploit available for the container image.</p>"""
    fix_available_active_findings_count: NotRequired["int"]
    """<p>The number of active findings with a fix available for the container image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerImageAggregationResponse) -> dict:
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
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "repository" in value:
        out["repository"] = value["repository"]
    if "registry" in value:
        out["registry"] = value["registry"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "image_tags" in value:
        import capo_inspector2.types.string_list

        out["imageTags"] = capo_inspector2.types.string_list.serialize_json(
            value["image_tags"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "last_in_use_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["lastInUseAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["last_in_use_at"]
        )
    if "in_use_count" in value:
        out["inUseCount"] = value["in_use_count"]
    if "exploit_available_active_findings_count" in value:
        out["exploitAvailableActiveFindingsCount"] = value[
            "exploit_available_active_findings_count"
        ]
    if "fix_available_active_findings_count" in value:
        out["fixAvailableActiveFindingsCount"] = value[
            "fix_available_active_findings_count"
        ]
    return out


def deserialize_json(data: dict) -> ContainerImageAggregationResponse:
    out: ContainerImageAggregationResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("imageDigest") is not None:
        out["image_digest"] = data["imageDigest"]
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    if data.get("registry") is not None:
        out["registry"] = data["registry"]
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    if data.get("imageTags") is not None:
        import capo_inspector2.types.string_list

        out["image_tags"] = capo_inspector2.types.string_list.deserialize_json(
            data["imageTags"]
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if data.get("lastInUseAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["last_in_use_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastInUseAt"]
            )
        )
    if data.get("inUseCount") is not None:
        out["in_use_count"] = data["inUseCount"]
    if data.get("exploitAvailableActiveFindingsCount") is not None:
        out["exploit_available_active_findings_count"] = data[
            "exploitAvailableActiveFindingsCount"
        ]
    if data.get("fixAvailableActiveFindingsCount") is not None:
        out["fix_available_active_findings_count"] = data[
            "fixAvailableActiveFindingsCount"
        ]
    return out
