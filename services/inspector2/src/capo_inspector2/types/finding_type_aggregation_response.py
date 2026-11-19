"""Generated from Smithy shape ``com.amazonaws.inspector2#FindingTypeAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.severity_counts


class FindingTypeAggregationResponse(TypedDict, closed=True):
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account associated with the findings.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>The value to sort results by.</p>"""
    exploit_available_count: NotRequired["int"]
    """<p>The number of findings that have an exploit available.</p>"""
    fix_available_count: NotRequired["int"]
    """<p> Details about the number of fixes. </p>"""
    cloud_provider: NotRequired["str"]
    """<p>The cloud service provider associated with this finding type aggregation. Valid values:</p> <ul> <li> <p> <code>AWS</code> – Findings from Amazon Web Services resources.</p> </li> <li> <p> <code>AZURE</code> – Findings from Microsoft Azure resources.</p> </li> <li> <p> <code>GCP</code> – Findings from Google Cloud Platform (GCP) resources.</p> </li> </ul>"""
    cloud_account_id: NotRequired["str"]
    """<p>The cloud account ID for the finding type aggregation.</p>"""
    cloud_org_id: NotRequired["str"]
    """<p>The cloud organization ID for the finding type aggregation.</p>"""
    cloud_region: NotRequired["str"]
    """<p>The cloud Region associated with this finding type aggregation. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services Region, such as <code>us-east-1</code>.</p> </li> <li> <p>An Azure region, such as <code>eastus</code>.</p> </li> <li> <p>A Google Cloud Platform (GCP) location, such as the region <code>us-central1</code> or the zone <code>us-central1-a</code>.</p> </li> </ul>"""
    cloud_partition: NotRequired["str"]
    """<p>The cloud infrastructure partition associated with this finding type aggregation. Valid values:</p> <ul> <li> <p> <code>aws</code> – Amazon Web Services commercial Regions.</p> </li> <li> <p> <code>aws-cn</code> – Amazon Web Services China Regions.</p> </li> <li> <p> <code>aws-us-gov</code> – Amazon Web Services GovCloud (US) Regions.</p> </li> <li> <p> <code>AzureCloud</code> – Azure commercial Regions.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeAggregationResponse) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "exploit_available_count" in value:
        out["exploitAvailableCount"] = value["exploit_available_count"]
    if "fix_available_count" in value:
        out["fixAvailableCount"] = value["fix_available_count"]
    if "cloud_provider" in value:
        out["cloudProvider"] = value["cloud_provider"]
    if "cloud_account_id" in value:
        out["cloudAccountId"] = value["cloud_account_id"]
    if "cloud_org_id" in value:
        out["cloudOrgId"] = value["cloud_org_id"]
    if "cloud_region" in value:
        out["cloudRegion"] = value["cloud_region"]
    if "cloud_partition" in value:
        out["cloudPartition"] = value["cloud_partition"]
    return out


def deserialize_json(data: dict) -> FindingTypeAggregationResponse:
    out: FindingTypeAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if data.get("exploitAvailableCount") is not None:
        out["exploit_available_count"] = data["exploitAvailableCount"]
    if data.get("fixAvailableCount") is not None:
        out["fix_available_count"] = data["fixAvailableCount"]
    if data.get("cloudProvider") is not None:
        out["cloud_provider"] = data["cloudProvider"]
    if data.get("cloudAccountId") is not None:
        out["cloud_account_id"] = data["cloudAccountId"]
    if data.get("cloudOrgId") is not None:
        out["cloud_org_id"] = data["cloudOrgId"]
    if data.get("cloudRegion") is not None:
        out["cloud_region"] = data["cloudRegion"]
    if data.get("cloudPartition") is not None:
        out["cloud_partition"] = data["cloudPartition"]
    return out
