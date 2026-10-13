"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAssetBundleExportJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration
    import capo_quicksight.types.asset_bundle_export_format
    import capo_quicksight.types.asset_bundle_export_job_error_list
    import capo_quicksight.types.asset_bundle_export_job_status
    import capo_quicksight.types.asset_bundle_export_job_validation_strategy
    import capo_quicksight.types.asset_bundle_export_job_warning_list
    import capo_quicksight.types.asset_bundle_resource_arns
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean
    import capo_quicksight.types.include_folder_members
    import capo_quicksight.types.non_empty_string
    import capo_quicksight.types.sensitive_s3_uri
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.timestamp


class DescribeAssetBundleExportJobResponse(TypedDict, closed=True):
    job_status: NotRequired[
        "capo_quicksight.types.asset_bundle_export_job_status.AssetBundleExportJobStatus"
    ]
    """<p>Indicates the status of a job through its queuing and execution.</p> <p>Poll this <code>DescribeAssetBundleExportApi</code> until <code>JobStatus</code> is either <code>SUCCESSFUL</code> or <code>FAILED</code>.</p>"""
    download_url: NotRequired["capo_quicksight.types.sensitive_s3_uri.SensitiveS3Uri"]
    """<p>The URL to download the exported asset bundle data from.</p> <p>This URL is available only after the job has succeeded. This URL is valid for 5 minutes after issuance. Call <code>DescribeAssetBundleExportJob</code> again for a fresh URL if needed.</p> <p>The downloaded asset bundle is a zip file named <code>assetbundle-{jobId}.qs</code>. The file has a <code>.qs</code> extension.</p> <p>This URL can't be used in a <code>StartAssetBundleImportJob</code> API call and should only be used for download purposes.</p>"""
    errors: NotRequired[
        "capo_quicksight.types.asset_bundle_export_job_error_list.AssetBundleExportJobErrorList"
    ]
    """<p>An array of error records that describes any failures that occurred during the export job processing.</p> <p>Error records accumulate while the job runs. The complete set of error records is available after the job has completed and failed.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the export job.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the export job was created.</p>"""
    asset_bundle_export_job_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the job. The job ID is set when you start a new job with a <code>StartAssetBundleExportJob</code> API call.</p>"""
    aws_account_id: NotRequired["capo_quicksight.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account that the export job was executed in. </p>"""
    resource_arns: NotRequired[
        "capo_quicksight.types.asset_bundle_resource_arns.AssetBundleResourceArns"
    ]
    """<p>A list of resource ARNs that exported with the job.</p>"""
    include_all_dependencies: "capo_quicksight.types.boolean.Boolean"
    """<p>The include dependencies flag.</p>"""
    export_format: NotRequired[
        "capo_quicksight.types.asset_bundle_export_format.AssetBundleExportFormat"
    ]
    """<p>The format of the exported asset bundle. A <code>QUICKSIGHT_JSON</code> formatted file can be used to make a <code>StartAssetBundleImportJob</code> API call. A <code>CLOUDFORMATION_JSON</code> formatted file can be used in the CloudFormation console and with the CloudFormation APIs.</p>"""
    cloud_formation_override_property_configuration: NotRequired[
        "capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration.AssetBundleCloudFormationOverridePropertyConfiguration"
    ]
    """<p>The CloudFormation override property configuration for the export job.</p>"""
    request_id: NotRequired["capo_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the response.</p>"""
    include_permissions: "capo_quicksight.types.boolean.Boolean"
    """<p>The include permissions flag.</p>"""
    include_tags: "capo_quicksight.types.boolean.Boolean"
    """<p>The include tags flag.</p>"""
    validation_strategy: NotRequired[
        "capo_quicksight.types.asset_bundle_export_job_validation_strategy.AssetBundleExportJobValidationStrategy"
    ]
    """<p>The validation strategy that is used to export the analysis or dashboard.</p>"""
    warnings: NotRequired[
        "capo_quicksight.types.asset_bundle_export_job_warning_list.AssetBundleExportJobWarningList"
    ]
    """<p>An array of warning records that describe the analysis or dashboard that is exported. This array includes UI errors that can be skipped during the validation process.</p> <p>This property only appears if <code>StrictModeForAllResources</code> in <code>ValidationStrategy</code> is set to <code>FALSE</code>.</p>"""
    include_folder_memberships: "capo_quicksight.types.boolean.Boolean"
    """<p>The include folder memberships flag.</p>"""
    include_folder_members: NotRequired[
        "capo_quicksight.types.include_folder_members.IncludeFolderMembers"
    ]
    """<p>A setting that determines whether folder members are included.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetBundleExportJobResponse) -> dict:
    out: dict = {}
    if "job_status" in value:
        import capo_quicksight.types.asset_bundle_export_job_status

        out["JobStatus"] = (
            capo_quicksight.types.asset_bundle_export_job_status.serialize_json(
                value["job_status"]
            )
        )
    if "download_url" in value:
        out["DownloadUrl"] = value["download_url"]
    if "errors" in value:
        import capo_quicksight.types.asset_bundle_export_job_error_list

        out["Errors"] = (
            capo_quicksight.types.asset_bundle_export_job_error_list.serialize_json(
                value["errors"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "asset_bundle_export_job_id" in value:
        out["AssetBundleExportJobId"] = value["asset_bundle_export_job_id"]
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "resource_arns" in value:
        import capo_quicksight.types.asset_bundle_resource_arns

        out["ResourceArns"] = (
            capo_quicksight.types.asset_bundle_resource_arns.serialize_json(
                value["resource_arns"]
            )
        )
    out["IncludeAllDependencies"] = value.get("include_all_dependencies", False)
    if "export_format" in value:
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
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    out["IncludePermissions"] = value.get("include_permissions", False)
    out["IncludeTags"] = value.get("include_tags", False)
    if "validation_strategy" in value:
        import capo_quicksight.types.asset_bundle_export_job_validation_strategy

        out["ValidationStrategy"] = (
            capo_quicksight.types.asset_bundle_export_job_validation_strategy.serialize_json(
                value["validation_strategy"]
            )
        )
    if "warnings" in value:
        import capo_quicksight.types.asset_bundle_export_job_warning_list

        out["Warnings"] = (
            capo_quicksight.types.asset_bundle_export_job_warning_list.serialize_json(
                value["warnings"]
            )
        )
    out["IncludeFolderMemberships"] = value.get("include_folder_memberships", False)
    if "include_folder_members" in value:
        import capo_quicksight.types.include_folder_members

        out["IncludeFolderMembers"] = (
            capo_quicksight.types.include_folder_members.serialize_json(
                value["include_folder_members"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetBundleExportJobResponse:
    out: DescribeAssetBundleExportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobStatus") is not None:
        import capo_quicksight.types.asset_bundle_export_job_status

        out["job_status"] = (
            capo_quicksight.types.asset_bundle_export_job_status.deserialize_json(
                data["JobStatus"]
            )
        )
    if data.get("DownloadUrl") is not None:
        out["download_url"] = data["DownloadUrl"]
    if data.get("Errors") is not None:
        import capo_quicksight.types.asset_bundle_export_job_error_list

        out["errors"] = (
            capo_quicksight.types.asset_bundle_export_job_error_list.deserialize_json(
                data["Errors"]
            )
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("AssetBundleExportJobId") is not None:
        out["asset_bundle_export_job_id"] = data["AssetBundleExportJobId"]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    if data.get("ResourceArns") is not None:
        import capo_quicksight.types.asset_bundle_resource_arns

        out["resource_arns"] = (
            capo_quicksight.types.asset_bundle_resource_arns.deserialize_json(
                data["ResourceArns"]
            )
        )
    if data.get("IncludeAllDependencies") is not None:
        out["include_all_dependencies"] = data["IncludeAllDependencies"]
    else:
        out["include_all_dependencies"] = False
    if data.get("ExportFormat") is not None:
        import capo_quicksight.types.asset_bundle_export_format

        out["export_format"] = (
            capo_quicksight.types.asset_bundle_export_format.deserialize_json(
                data["ExportFormat"]
            )
        )
    if data.get("CloudFormationOverridePropertyConfiguration") is not None:
        import capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration

        out["cloud_formation_override_property_configuration"] = (
            capo_quicksight.types.asset_bundle_cloud_formation_override_property_configuration.deserialize_json(
                data["CloudFormationOverridePropertyConfiguration"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("IncludePermissions") is not None:
        out["include_permissions"] = data["IncludePermissions"]
    else:
        out["include_permissions"] = False
    if data.get("IncludeTags") is not None:
        out["include_tags"] = data["IncludeTags"]
    else:
        out["include_tags"] = False
    if data.get("ValidationStrategy") is not None:
        import capo_quicksight.types.asset_bundle_export_job_validation_strategy

        out["validation_strategy"] = (
            capo_quicksight.types.asset_bundle_export_job_validation_strategy.deserialize_json(
                data["ValidationStrategy"]
            )
        )
    if data.get("Warnings") is not None:
        import capo_quicksight.types.asset_bundle_export_job_warning_list

        out["warnings"] = (
            capo_quicksight.types.asset_bundle_export_job_warning_list.deserialize_json(
                data["Warnings"]
            )
        )
    if data.get("IncludeFolderMemberships") is not None:
        out["include_folder_memberships"] = data["IncludeFolderMemberships"]
    else:
        out["include_folder_memberships"] = False
    if data.get("IncludeFolderMembers") is not None:
        import capo_quicksight.types.include_folder_members

        out["include_folder_members"] = (
            capo_quicksight.types.include_folder_members.deserialize_json(
                data["IncludeFolderMembers"]
            )
        )
    return out


def redact_sensitive(value: DescribeAssetBundleExportJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "download_url" in value:
        out["download_url"] = "*** Sensitive Data Redacted ***"
    return out
