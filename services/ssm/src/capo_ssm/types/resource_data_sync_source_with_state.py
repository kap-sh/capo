"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncSourceWithState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.resource_data_sync_aws_organizations_source
    import capo_ssm.types.resource_data_sync_enable_all_ops_data_sources
    import capo_ssm.types.resource_data_sync_include_future_regions
    import capo_ssm.types.resource_data_sync_source_region_list
    import capo_ssm.types.resource_data_sync_source_type
    import capo_ssm.types.resource_data_sync_state


class ResourceDataSyncSourceWithState(TypedDict, closed=True):
    source_type: NotRequired[
        "capo_ssm.types.resource_data_sync_source_type.ResourceDataSyncSourceType"
    ]
    """<p>The type of data source for the resource data sync. <code>SourceType</code> is either <code>AwsOrganizations</code> (if an organization is present in Organizations) or <code>singleAccountMultiRegions</code>.</p>"""
    aws_organizations_source: NotRequired[
        "capo_ssm.types.resource_data_sync_aws_organizations_source.ResourceDataSyncAwsOrganizationsSource"
    ]
    """<p>The field name in <code>SyncSource</code> for the <code>ResourceDataSyncAwsOrganizationsSource</code> type.</p>"""
    source_regions: NotRequired[
        "capo_ssm.types.resource_data_sync_source_region_list.ResourceDataSyncSourceRegionList"
    ]
    """<p>The <code>SyncSource</code> Amazon Web Services Regions included in the resource data sync.</p>"""
    include_future_regions: "capo_ssm.types.resource_data_sync_include_future_regions.ResourceDataSyncIncludeFutureRegions"
    """<p>Whether to automatically synchronize and aggregate data from new Amazon Web Services Regions when those Regions come online.</p>"""
    state: NotRequired["capo_ssm.types.resource_data_sync_state.ResourceDataSyncState"]
    """<p>The data type name for including resource data sync state. There are four sync states:</p> <p> <code>OrganizationNotExists</code>: Your organization doesn't exist.</p> <p> <code>NoPermissions</code>: The system can't locate the service-linked role. This role is automatically created when a user creates a resource data sync in Explorer.</p> <p> <code>InvalidOrganizationalUnit</code>: You specified or selected an invalid unit in the resource data sync configuration.</p> <p> <code>TrustedAccessDisabled</code>: You disabled Systems Manager access in the organization in Organizations.</p>"""
    enable_all_ops_data_sources: "capo_ssm.types.resource_data_sync_enable_all_ops_data_sources.ResourceDataSyncEnableAllOpsDataSources"
    """<p>When you create a resource data sync, if you choose one of the Organizations options, then Systems Manager automatically enables all OpsData sources in the selected Amazon Web Services Regions for all Amazon Web Services accounts in your organization (or in the selected organization units). For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html">Setting up Systems Manager Explorer to display data from multiple accounts and Regions</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncSourceWithState) -> dict:
    out: dict = {}
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "aws_organizations_source" in value:
        import capo_ssm.types.resource_data_sync_aws_organizations_source

        out["AwsOrganizationsSource"] = (
            capo_ssm.types.resource_data_sync_aws_organizations_source.serialize_aws_json_1_1(
                value["aws_organizations_source"]
            )
        )
    if "source_regions" in value:
        import capo_ssm.types.resource_data_sync_source_region_list

        out["SourceRegions"] = (
            capo_ssm.types.resource_data_sync_source_region_list.serialize_aws_json_1_1(
                value["source_regions"]
            )
        )
    out["IncludeFutureRegions"] = value.get("include_future_regions", False)
    if "state" in value:
        out["State"] = value["state"]
    out["EnableAllOpsDataSources"] = value.get("enable_all_ops_data_sources", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncSourceWithState:
    out: ResourceDataSyncSourceWithState = {}  # type: ignore[typeddict-item]
    if data.get("SourceType") is not None:
        out["source_type"] = data["SourceType"]
    if data.get("AwsOrganizationsSource") is not None:
        import capo_ssm.types.resource_data_sync_aws_organizations_source

        out["aws_organizations_source"] = (
            capo_ssm.types.resource_data_sync_aws_organizations_source.deserialize_aws_json_1_1(
                data["AwsOrganizationsSource"]
            )
        )
    if data.get("SourceRegions") is not None:
        import capo_ssm.types.resource_data_sync_source_region_list

        out["source_regions"] = (
            capo_ssm.types.resource_data_sync_source_region_list.deserialize_aws_json_1_1(
                data["SourceRegions"]
            )
        )
    if data.get("IncludeFutureRegions") is not None:
        out["include_future_regions"] = data["IncludeFutureRegions"]
    else:
        out["include_future_regions"] = False
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("EnableAllOpsDataSources") is not None:
        out["enable_all_ops_data_sources"] = data["EnableAllOpsDataSources"]
    else:
        out["enable_all_ops_data_sources"] = False
    return out
