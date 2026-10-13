"""Generated from Smithy shape ``com.amazonaws.quicksight#StartAssetBundleImportJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_failure_action
    import capo_quicksight.types.asset_bundle_import_job_override_parameters
    import capo_quicksight.types.asset_bundle_import_job_override_permissions
    import capo_quicksight.types.asset_bundle_import_job_override_tags
    import capo_quicksight.types.asset_bundle_import_job_override_validation_strategy
    import capo_quicksight.types.asset_bundle_import_source
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class StartAssetBundleImportJobRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account to import assets into. </p>"""
    asset_bundle_import_job_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.</p>"""
    asset_bundle_import_source: (
        "capo_quicksight.types.asset_bundle_import_source.AssetBundleImportSource"
    )
    """<p>The source of the asset bundle zip file that contains the data that you want to import. The file must be in <code>QUICKSIGHT_JSON</code> format. </p>"""
    override_parameters: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_override_parameters.AssetBundleImportJobOverrideParameters"
    ]
    """<p>Optional overrides that are applied to the resource configuration before import.</p>"""
    failure_action: NotRequired[
        "capo_quicksight.types.asset_bundle_import_failure_action.AssetBundleImportFailureAction"
    ]
    """<p>The failure action for the import job.</p> <p>If you choose <code>ROLLBACK</code>, failed import jobs will attempt to undo any asset changes caused by the failed job.</p> <p>If you choose <code>DO_NOTHING</code>, failed import jobs will not attempt to roll back any asset changes caused by the failed job, possibly keeping the Amazon Quick Sight account in an inconsistent state.</p>"""
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
    """<p>An optional validation strategy override for all analyses and dashboards that is applied to the resource configuration before import. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAssetBundleImportJobRequest) -> dict:
    out: dict = {}
    out["AssetBundleImportJobId"] = value["asset_bundle_import_job_id"]
    import capo_quicksight.types.asset_bundle_import_source

    out["AssetBundleImportSource"] = (
        capo_quicksight.types.asset_bundle_import_source.serialize_json(
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
    return out


def deserialize_json(data: dict) -> StartAssetBundleImportJobRequest:
    out: StartAssetBundleImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssetBundleImportJobId") is not None:
        out["asset_bundle_import_job_id"] = data["AssetBundleImportJobId"]
    else:
        raise DeserializationError(
            "StartAssetBundleImportJobRequest.asset_bundle_import_job_id required"
        )
    if data.get("AssetBundleImportSource") is not None:
        import capo_quicksight.types.asset_bundle_import_source

        out["asset_bundle_import_source"] = (
            capo_quicksight.types.asset_bundle_import_source.deserialize_json(
                data["AssetBundleImportSource"]
            )
        )
    else:
        raise DeserializationError(
            "StartAssetBundleImportJobRequest.asset_bundle_import_source required"
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
    return out


def redact_sensitive(value: StartAssetBundleImportJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "asset_bundle_import_source" in value:
        import capo_quicksight.types.asset_bundle_import_source

        out["asset_bundle_import_source"] = (
            capo_quicksight.types.asset_bundle_import_source.redact_sensitive(
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
