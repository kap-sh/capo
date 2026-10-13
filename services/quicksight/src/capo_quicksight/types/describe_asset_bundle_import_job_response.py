"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAssetBundleImportJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.asset_bundle_import_failure_action
    import capo_quicksight.types.asset_bundle_import_job_error_list
    import capo_quicksight.types.asset_bundle_import_job_override_parameters
    import capo_quicksight.types.asset_bundle_import_job_override_permissions
    import capo_quicksight.types.asset_bundle_import_job_override_tags
    import capo_quicksight.types.asset_bundle_import_job_override_validation_strategy
    import capo_quicksight.types.asset_bundle_import_job_status
    import capo_quicksight.types.asset_bundle_import_job_warning_list
    import capo_quicksight.types.asset_bundle_import_source_description
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.non_empty_string
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.timestamp


class DescribeAssetBundleImportJobResponse(TypedDict, closed=True):
    job_status: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_status.AssetBundleImportJobStatus"
    ]
    """<p>Indicates the status of a job through its queuing and execution.</p> <p>Poll the <code>DescribeAssetBundleImport</code> API until <code>JobStatus</code> returns one of the following values:</p> <ul> <li> <p> <code>SUCCESSFUL</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> <li> <p> <code>FAILED_ROLLBACK_COMPLETED</code> </p> </li> <li> <p> <code>FAILED_ROLLBACK_ERROR</code> </p> </li> </ul>"""
    errors: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_error_list.AssetBundleImportJobErrorList"
    ]
    """<p>An array of error records that describes any failures that occurred during the export job processing.</p> <p>Error records accumulate while the job is still running. The complete set of error records is available after the job has completed and failed.</p>"""
    rollback_errors: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_error_list.AssetBundleImportJobErrorList"
    ]
    """<p>An array of error records that describes any failures that occurred while an import job was attempting a rollback.</p> <p>Error records accumulate while the job is still running. The complete set of error records is available after the job has completed and failed.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the import job.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the import job was created.</p>"""
    asset_bundle_import_job_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the job. The job ID is set when you start a new job with a <code>StartAssetBundleImportJob</code> API call.</p>"""
    aws_account_id: NotRequired["capo_quicksight.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account the import job was executed in. </p>"""
    asset_bundle_import_source: NotRequired[
        "capo_quicksight.types.asset_bundle_import_source_description.AssetBundleImportSourceDescription"
    ]
    """<p>The source of the asset bundle zip file that contains the data that is imported by the job.</p>"""
    override_parameters: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_override_parameters.AssetBundleImportJobOverrideParameters"
    ]
    """<p>Optional overrides that are applied to the resource configuration before import.</p>"""
    failure_action: NotRequired[
        "capo_quicksight.types.asset_bundle_import_failure_action.AssetBundleImportFailureAction"
    ]
    """<p>The failure action for the import job.</p>"""
    request_id: NotRequired["capo_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the response.</p>"""
    override_permissions: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_override_permissions.AssetBundleImportJobOverridePermissions"
    ]
    """<p>Optional permission overrides that are applied to the resource configuration before import.</p>"""
    override_tags: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_override_tags.AssetBundleImportJobOverrideTags"
    ]
    """<p>Optional tag overrides that are applied to the resource configuration before import.</p>"""
    override_validation_strategy: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_override_validation_strategy.AssetBundleImportJobOverrideValidationStrategy"
    ]
    """<p>An optional validation strategy override for all analyses and dashboards to be applied to the resource configuration before import.</p>"""
    warnings: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_warning_list.AssetBundleImportJobWarningList"
    ]
    """<p>An array of warning records that describe all permitted errors that are encountered during the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetBundleImportJobResponse) -> dict:
    out: dict = {}
    if "job_status" in value:
        import capo_quicksight.types.asset_bundle_import_job_status

        out["JobStatus"] = (
            capo_quicksight.types.asset_bundle_import_job_status.serialize_json(
                value["job_status"]
            )
        )
    if "errors" in value:
        import capo_quicksight.types.asset_bundle_import_job_error_list

        out["Errors"] = (
            capo_quicksight.types.asset_bundle_import_job_error_list.serialize_json(
                value["errors"]
            )
        )
    if "rollback_errors" in value:
        import capo_quicksight.types.asset_bundle_import_job_error_list

        out["RollbackErrors"] = (
            capo_quicksight.types.asset_bundle_import_job_error_list.serialize_json(
                value["rollback_errors"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "asset_bundle_import_job_id" in value:
        out["AssetBundleImportJobId"] = value["asset_bundle_import_job_id"]
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "asset_bundle_import_source" in value:
        import capo_quicksight.types.asset_bundle_import_source_description

        out["AssetBundleImportSource"] = (
            capo_quicksight.types.asset_bundle_import_source_description.serialize_json(
                value["asset_bundle_import_source"]
            )
        )
    if "override_parameters" in value:
        import capo_quicksight.types.asset_bundle_import_job_override_parameters

        out["OverrideParameters"] = (
            capo_quicksight.types.asset_bundle_import_job_override_parameters.serialize_json(
                value["override_parameters"]
            )
        )
    if "failure_action" in value:
        import capo_quicksight.types.asset_bundle_import_failure_action

        out["FailureAction"] = (
            capo_quicksight.types.asset_bundle_import_failure_action.serialize_json(
                value["failure_action"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "override_permissions" in value:
        import capo_quicksight.types.asset_bundle_import_job_override_permissions

        out["OverridePermissions"] = (
            capo_quicksight.types.asset_bundle_import_job_override_permissions.serialize_json(
                value["override_permissions"]
            )
        )
    if "override_tags" in value:
        import capo_quicksight.types.asset_bundle_import_job_override_tags

        out["OverrideTags"] = (
            capo_quicksight.types.asset_bundle_import_job_override_tags.serialize_json(
                value["override_tags"]
            )
        )
    if "override_validation_strategy" in value:
        import capo_quicksight.types.asset_bundle_import_job_override_validation_strategy

        out["OverrideValidationStrategy"] = (
            capo_quicksight.types.asset_bundle_import_job_override_validation_strategy.serialize_json(
                value["override_validation_strategy"]
            )
        )
    if "warnings" in value:
        import capo_quicksight.types.asset_bundle_import_job_warning_list

        out["Warnings"] = (
            capo_quicksight.types.asset_bundle_import_job_warning_list.serialize_json(
                value["warnings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetBundleImportJobResponse:
    out: DescribeAssetBundleImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobStatus") is not None:
        import capo_quicksight.types.asset_bundle_import_job_status

        out["job_status"] = (
            capo_quicksight.types.asset_bundle_import_job_status.deserialize_json(
                data["JobStatus"]
            )
        )
    if data.get("Errors") is not None:
        import capo_quicksight.types.asset_bundle_import_job_error_list

        out["errors"] = (
            capo_quicksight.types.asset_bundle_import_job_error_list.deserialize_json(
                data["Errors"]
            )
        )
    if data.get("RollbackErrors") is not None:
        import capo_quicksight.types.asset_bundle_import_job_error_list

        out["rollback_errors"] = (
            capo_quicksight.types.asset_bundle_import_job_error_list.deserialize_json(
                data["RollbackErrors"]
            )
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("AssetBundleImportJobId") is not None:
        out["asset_bundle_import_job_id"] = data["AssetBundleImportJobId"]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    if data.get("AssetBundleImportSource") is not None:
        import capo_quicksight.types.asset_bundle_import_source_description

        out["asset_bundle_import_source"] = (
            capo_quicksight.types.asset_bundle_import_source_description.deserialize_json(
                data["AssetBundleImportSource"]
            )
        )
    if data.get("OverrideParameters") is not None:
        import capo_quicksight.types.asset_bundle_import_job_override_parameters

        out["override_parameters"] = (
            capo_quicksight.types.asset_bundle_import_job_override_parameters.deserialize_json(
                data["OverrideParameters"]
            )
        )
    if data.get("FailureAction") is not None:
        import capo_quicksight.types.asset_bundle_import_failure_action

        out["failure_action"] = (
            capo_quicksight.types.asset_bundle_import_failure_action.deserialize_json(
                data["FailureAction"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("OverridePermissions") is not None:
        import capo_quicksight.types.asset_bundle_import_job_override_permissions

        out["override_permissions"] = (
            capo_quicksight.types.asset_bundle_import_job_override_permissions.deserialize_json(
                data["OverridePermissions"]
            )
        )
    if data.get("OverrideTags") is not None:
        import capo_quicksight.types.asset_bundle_import_job_override_tags

        out["override_tags"] = (
            capo_quicksight.types.asset_bundle_import_job_override_tags.deserialize_json(
                data["OverrideTags"]
            )
        )
    if data.get("OverrideValidationStrategy") is not None:
        import capo_quicksight.types.asset_bundle_import_job_override_validation_strategy

        out["override_validation_strategy"] = (
            capo_quicksight.types.asset_bundle_import_job_override_validation_strategy.deserialize_json(
                data["OverrideValidationStrategy"]
            )
        )
    if data.get("Warnings") is not None:
        import capo_quicksight.types.asset_bundle_import_job_warning_list

        out["warnings"] = (
            capo_quicksight.types.asset_bundle_import_job_warning_list.deserialize_json(
                data["Warnings"]
            )
        )
    return out


def redact_sensitive(value: DescribeAssetBundleImportJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "asset_bundle_import_source" in value:
        import capo_quicksight.types.asset_bundle_import_source_description

        out["asset_bundle_import_source"] = (
            capo_quicksight.types.asset_bundle_import_source_description.redact_sensitive(
                value["asset_bundle_import_source"]
            )
        )
    if "override_parameters" in value:
        import capo_quicksight.types.asset_bundle_import_job_override_parameters

        out["override_parameters"] = (
            capo_quicksight.types.asset_bundle_import_job_override_parameters.redact_sensitive(
                value["override_parameters"]
            )
        )
    return out
