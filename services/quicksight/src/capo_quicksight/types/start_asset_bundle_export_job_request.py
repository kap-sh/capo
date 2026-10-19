"""Generated from Smithy shape ``com.amazonaws.quicksight#StartAssetBundleExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration
    import capo_quicksight.types.asset_bundle_export_format
    import capo_quicksight.types.asset_bundle_export_job_validation_strategy
    import capo_quicksight.types.asset_bundle_resource_arns
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean
    import capo_quicksight.types.include_folder_members
    import capo_quicksight.types.short_restrictive_resource_id


class StartAssetBundleExportJobRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account to export assets from.</p>"""
    asset_bundle_export_job_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.</p>"""
    resource_arns: (
        "capo_quicksight.types.asset_bundle_resource_arns.AssetBundleResourceArns"
    )
    """<p>An array of resource ARNs to export. The following resources are supported.</p> <ul> <li> <p> <code>Analysis</code> </p> </li> <li> <p> <code>Dashboard</code> </p> </li> <li> <p> <code>DataSet</code> </p> </li> <li> <p> <code>DataSource</code> </p> </li> <li> <p> <code>RefreshSchedule</code> </p> </li> <li> <p> <code>Theme</code> </p> </li> <li> <p> <code>VPCConnection</code> </p> </li> </ul> <p>The API caller must have the necessary permissions in their IAM role to access each resource before the resources can be exported.</p>"""
    include_all_dependencies: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>A Boolean that determines whether all dependencies of each resource ARN are recursively exported with the job. For example, say you provided a Dashboard ARN to the <code>ResourceArns</code> parameter. If you set <code>IncludeAllDependencies</code> to <code>TRUE</code>, any theme, dataset, and data source resource that is a dependency of the dashboard is also exported.</p>"""
    export_format: (
        "capo_quicksight.types.asset_bundle_export_format.AssetBundleExportFormat"
    )
    """<p>The export data format.</p>"""
    cloud_formation_override_property_configuration: NotRequired[
        "capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration.AssetBundleCloudFormationOverridePropertyConfiguration"
    ]
    """<p>An optional collection of structures that generate CloudFormation parameters to override the existing resource property values when the resource is exported to a new CloudFormation template.</p> <p>Use this field if the <code>ExportFormat</code> field of a <code>StartAssetBundleExportJobRequest</code> API call is set to <code>CLOUDFORMATION_JSON</code>.</p>"""
    include_permissions: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>A Boolean that determines whether all permissions for each resource ARN are exported with the job. If you set <code>IncludePermissions</code> to <code>TRUE</code>, any permissions associated with each resource are exported. </p>"""
    include_tags: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p> A Boolean that determines whether all tags for each resource ARN are exported with the job. If you set <code>IncludeTags</code> to <code>TRUE</code>, any tags associated with each resource are exported.</p>"""
    validation_strategy: NotRequired[
        "capo_quicksight.types.asset_bundle_export_job_validation_strategy.AssetBundleExportJobValidationStrategy"
    ]
    """<p>An optional parameter that determines which validation strategy to use for the export job. If <code>StrictModeForAllResources</code> is set to <code>TRUE</code>, strict validation for every error is enforced. If it is set to <code>FALSE</code>, validation is skipped for specific UI errors that are shown as warnings. The default value for <code>StrictModeForAllResources</code> is <code>FALSE</code>.</p>"""
    include_folder_memberships: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>A Boolean that determines if the exported asset carries over information about the folders that the asset is a member of. </p>"""
    include_folder_members: NotRequired[
        "capo_quicksight.types.include_folder_members.IncludeFolderMembers"
    ]
    """<p>A setting that indicates whether you want to include folder assets. You can also use this setting to recusrsively include all subfolders of an exported folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAssetBundleExportJobRequest) -> dict:
    out: dict = {}
    out["AssetBundleExportJobId"] = value["asset_bundle_export_job_id"]
    import capo_quicksight.types.asset_bundle_resource_arns

    out["ResourceArns"] = (
        capo_quicksight.types.asset_bundle_resource_arns.serialize_json(
            value["resource_arns"]
        )
    )
    if "include_all_dependencies" in value:
        out["IncludeAllDependencies"] = value["include_all_dependencies"]
    import capo_quicksight.types.asset_bundle_export_format

    out["ExportFormat"] = (
        capo_quicksight.types.asset_bundle_export_format.serialize_json(
            value["export_format"]
        )
    )
    if "cloud_formation_override_property_configuration" in value:
        import capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration

        out["CloudFormationOverridePropertyConfiguration"] = (
            capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration.serialize_json(
                value["cloud_formation_override_property_configuration"]
            )
        )
    if "include_permissions" in value:
        out["IncludePermissions"] = value["include_permissions"]
    if "include_tags" in value:
        out["IncludeTags"] = value["include_tags"]
    if "validation_strategy" in value:
        import capo_quicksight.types.asset_bundle_export_job_validation_strategy

        out["ValidationStrategy"] = (
            capo_quicksight.types.asset_bundle_export_job_validation_strategy.serialize_json(
                value["validation_strategy"]
            )
        )
    if "include_folder_memberships" in value:
        out["IncludeFolderMemberships"] = value["include_folder_memberships"]
    if "include_folder_members" in value:
        import capo_quicksight.types.include_folder_members

        out["IncludeFolderMembers"] = (
            capo_quicksight.types.include_folder_members.serialize_json(
                value["include_folder_members"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartAssetBundleExportJobRequest:
    out: StartAssetBundleExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssetBundleExportJobId") is not None:
        out["asset_bundle_export_job_id"] = data["AssetBundleExportJobId"]
    else:
        raise DeserializationError(
            "StartAssetBundleExportJobRequest.asset_bundle_export_job_id required"
        )
    if data.get("ResourceArns") is not None:
        import capo_quicksight.types.asset_bundle_resource_arns

        out["resource_arns"] = (
            capo_quicksight.types.asset_bundle_resource_arns.deserialize_json(
                data["ResourceArns"]
            )
        )
    else:
        raise DeserializationError(
            "StartAssetBundleExportJobRequest.resource_arns required"
        )
    if data.get("IncludeAllDependencies") is not None:
        out["include_all_dependencies"] = data["IncludeAllDependencies"]
    if data.get("ExportFormat") is not None:
        import capo_quicksight.types.asset_bundle_export_format

        out["export_format"] = (
            capo_quicksight.types.asset_bundle_export_format.deserialize_json(
                data["ExportFormat"]
            )
        )
    else:
        raise DeserializationError(
            "StartAssetBundleExportJobRequest.export_format required"
        )
    if data.get("CloudFormationOverridePropertyConfiguration") is not None:
        import capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration

        out["cloud_formation_override_property_configuration"] = (
            capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration.deserialize_json(
                data["CloudFormationOverridePropertyConfiguration"]
            )
        )
    if data.get("IncludePermissions") is not None:
        out["include_permissions"] = data["IncludePermissions"]
    if data.get("IncludeTags") is not None:
        out["include_tags"] = data["IncludeTags"]
    if data.get("ValidationStrategy") is not None:
        import capo_quicksight.types.asset_bundle_export_job_validation_strategy

        out["validation_strategy"] = (
            capo_quicksight.types.asset_bundle_export_job_validation_strategy.deserialize_json(
                data["ValidationStrategy"]
            )
        )
    if data.get("IncludeFolderMemberships") is not None:
        out["include_folder_memberships"] = data["IncludeFolderMemberships"]
    if data.get("IncludeFolderMembers") is not None:
        import capo_quicksight.types.include_folder_members

        out["include_folder_members"] = (
            capo_quicksight.types.include_folder_members.deserialize_json(
                data["IncludeFolderMembers"]
            )
        )
    return out
