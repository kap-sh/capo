"""Generated from Smithy shape ``com.amazonaws.inspector2#AmiAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.ami_id
    import capo_inspector2.types.provider
    import capo_inspector2.types.provider_account_id
    import capo_inspector2.types.provider_org_id
    import capo_inspector2.types.provider_partition
    import capo_inspector2.types.provider_region
    import capo_inspector2.types.severity_counts


class AmiAggregationResponse(TypedDict, closed=True):
    ami: "capo_inspector2.types.ami_id.AmiId"
    """<p>The ID of the AMI that findings were aggregated for.</p>"""
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the AMI.</p>"""
    cloud_provider: NotRequired["capo_inspector2.types.provider.Provider"]
    """<p>The cloud service provider associated with this Amazon Machine Image (AMI) aggregation. Valid values:</p> <ul> <li> <p> <code>AWS</code> – Findings from Amazon Web Services resources.</p> </li> <li> <p> <code>AZURE</code> – Findings from Microsoft Azure resources.</p> </li> </ul>"""
    cloud_partition: NotRequired[
        "capo_inspector2.types.provider_partition.ProviderPartition"
    ]
    """<p>The cloud infrastructure partition associated with this AMI aggregation. Valid values:</p> <ul> <li> <p> <code>aws</code> – Amazon Web Services commercial Regions.</p> </li> <li> <p> <code>aws-cn</code> – Amazon Web Services China Regions.</p> </li> <li> <p> <code>aws-us-gov</code> – Amazon Web Services GovCloud (US) Regions.</p> </li> <li> <p> <code>AzureCloud</code> – Azure commercial Regions.</p> </li> </ul>"""
    cloud_region: NotRequired["capo_inspector2.types.provider_region.ProviderRegion"]
    """<p>The cloud Region associated with this AMI aggregation. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services Region, such as <code>us-east-1</code>.</p> </li> <li> <p>An Azure region, such as <code>eastus</code>.</p> </li> </ul>"""
    cloud_org_id: NotRequired["capo_inspector2.types.provider_org_id.ProviderOrgId"]
    """<p>The cloud organization ID for the AMI aggregation.</p>"""
    cloud_account_id: NotRequired[
        "capo_inspector2.types.provider_account_id.ProviderAccountId"
    ]
    """<p>The cloud account ID for the AMI aggregation.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>An object that contains the count of matched findings per severity.</p>"""
    affected_instances: NotRequired["int"]
    """<p>The IDs of Amazon EC2 instances using this AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiAggregationResponse) -> dict:
    out: dict = {}
    out["ami"] = value["ami"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "cloud_provider" in value:
        out["cloudProvider"] = value["cloud_provider"]
    if "cloud_partition" in value:
        out["cloudPartition"] = value["cloud_partition"]
    if "cloud_region" in value:
        out["cloudRegion"] = value["cloud_region"]
    if "cloud_org_id" in value:
        out["cloudOrgId"] = value["cloud_org_id"]
    if "cloud_account_id" in value:
        out["cloudAccountId"] = value["cloud_account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "affected_instances" in value:
        out["affectedInstances"] = value["affected_instances"]
    return out


def deserialize_json(data: dict) -> AmiAggregationResponse:
    out: AmiAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ami") is not None:
        out["ami"] = data["ami"]
    else:
        out["ami"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("cloudProvider") is not None:
        out["cloud_provider"] = data["cloudProvider"]
    if data.get("cloudPartition") is not None:
        out["cloud_partition"] = data["cloudPartition"]
    if data.get("cloudRegion") is not None:
        out["cloud_region"] = data["cloudRegion"]
    if data.get("cloudOrgId") is not None:
        out["cloud_org_id"] = data["cloudOrgId"]
    if data.get("cloudAccountId") is not None:
        out["cloud_account_id"] = data["cloudAccountId"]
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if data.get("affectedInstances") is not None:
        out["affected_instances"] = data["affectedInstances"]
    return out
