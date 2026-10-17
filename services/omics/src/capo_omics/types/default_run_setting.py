"""Generated from Smithy shape ``com.amazonaws.omics#DefaultRunSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.aws_account_id
    import capo_omics.types.cache_behavior
    import capo_omics.types.configuration_name
    import capo_omics.types.engine_settings
    import capo_omics.types.networking_mode
    import capo_omics.types.numeric_id_in_arn
    import capo_omics.types.run_group_id
    import capo_omics.types.run_log_level
    import capo_omics.types.run_name
    import capo_omics.types.run_output_uri
    import capo_omics.types.run_parameters
    import capo_omics.types.run_retention_mode
    import capo_omics.types.run_role_arn
    import capo_omics.types.scratch_storage_mode
    import capo_omics.types.session_policy
    import capo_omics.types.storage_type
    import capo_omics.types.tag_map
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_owner_id
    import capo_omics.types.workflow_type
    import capo_omics.types.workflow_version_name


class DefaultRunSetting(TypedDict, closed=True):
    workflow_id: "capo_omics.types.workflow_id.WorkflowId"
    """<p>The identifier of the workflow to run.</p>"""
    workflow_type: NotRequired["capo_omics.types.workflow_type.WorkflowType"]
    """<p>The type of the originating workflow. Batch runs are not supported with <code>READY2RUN</code> workflows.</p>"""
    role_arn: "capo_omics.types.run_role_arn.RunRoleArn"
    """<p>The IAM role ARN that grants HealthOmics permissions to access required Amazon Web Services resources such as Amazon S3 and CloudWatch. The role must have the same permissions required for individual <code>StartRun</code> calls.</p>"""
    name: NotRequired["capo_omics.types.run_name.RunName"]
    """<p>An optional user-friendly name applied to each workflow run. Can be overridden per run.</p>"""
    cache_id: NotRequired["capo_omics.types.numeric_id_in_arn.NumericIdInArn"]
    """<p>The identifier of the run cache to associate with the runs.</p>"""
    cache_behavior: NotRequired["capo_omics.types.cache_behavior.CacheBehavior"]
    """<p>The cache behavior for the runs. Requires <code>cacheId</code> to be set.</p>"""
    run_group_id: NotRequired["capo_omics.types.run_group_id.RunGroupId"]
    """<p>The ID of the run group to contain all workflow runs in the batch.</p>"""
    priority: NotRequired["int"]
    """<p>An integer priority for the workflow runs. Higher values correspond to higher priority. A value of 0 corresponds to the lowest priority. Can be overridden per run.</p>"""
    parameters: NotRequired["capo_omics.types.run_parameters.RunParameters"]
    """<p>Workflow parameter names and values shared across all runs. Merged with per-run parameters; run-specific values take precedence when keys overlap. Can be overridden per run.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The filesystem size in gibibytes (GiB) provisioned for each workflow run and shared by all tasks in that run. Defaults to 1200 GiB if not specified.</p>"""
    output_uri: NotRequired["capo_omics.types.run_output_uri.RunOutputUri"]
    """<p>The destination S3 URI for workflow outputs. Must begin with <code>s3://</code>. The <code>roleArn</code> must grant write permissions to this bucket. Can be overridden per run.</p>"""
    log_level: NotRequired["capo_omics.types.run_log_level.RunLogLevel"]
    """<p>The verbosity level for CloudWatch Logs emitted during each run.</p>"""
    run_tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Amazon Web Services tags to associate with each workflow run. Merged with per-run <code>runTags</code>; run-specific values take precedence when keys overlap.</p>"""
    retention_mode: NotRequired["capo_omics.types.run_retention_mode.RunRetentionMode"]
    """<p>The retention behavior for runs after completion.</p>"""
    storage_type: NotRequired["capo_omics.types.storage_type.StorageType"]
    """<p>The storage type for the workflow runs.</p>"""
    workflow_owner_id: NotRequired["capo_omics.types.workflow_owner_id.WorkflowOwnerId"]
    """<p>The Amazon Web Services account ID of the workflow owner, used for cross-account workflow sharing.</p>"""
    output_bucket_owner_id: NotRequired["capo_omics.types.aws_account_id.AwsAccountId"]
    """<p>The expected Amazon Web Services account ID of the owner of the output S3 bucket. Can be overridden per run.</p>"""
    workflow_version_name: NotRequired[
        "capo_omics.types.workflow_version_name.WorkflowVersionName"
    ]
    """<p>The version name of the specified workflow.</p>"""
    networking_mode: NotRequired["capo_omics.types.networking_mode.NetworkingMode"]
    """<p>Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.</p>"""
    configuration_name: NotRequired[
        "capo_omics.types.configuration_name.ConfigurationName"
    ]
    """<p>Optional configuration name to use for the workflow run.</p>"""
    session_policy: NotRequired["capo_omics.types.session_policy.SessionPolicy"]
    """Optional inline policy json for scoping down permissions via a session policy on the IAM role provided in the roleArn parameter."""
    engine_settings: NotRequired["capo_omics.types.engine_settings.EngineSettings"]
    """<p>Engine-specific settings for the workflow run. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles).</p>"""
    scratch_storage_mode: NotRequired[
        "capo_omics.types.scratch_storage_mode.ScratchStorageMode"
    ]
    """<p>Optional configuration for enabling scratch ephemeral storage mounted at /tmp. If not specified, this will default to SHARED. This configuration is applicable only for CPU tasks. For tasks using GPUs, scratch storage is always LOCAL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultRunSetting) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    if "workflow_type" in value:
        out["workflowType"] = value["workflow_type"]
    out["roleArn"] = value["role_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "cache_id" in value:
        out["cacheId"] = value["cache_id"]
    if "cache_behavior" in value:
        out["cacheBehavior"] = value["cache_behavior"]
    if "run_group_id" in value:
        out["runGroupId"] = value["run_group_id"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    if "storage_capacity" in value:
        out["storageCapacity"] = value["storage_capacity"]
    if "output_uri" in value:
        out["outputUri"] = value["output_uri"]
    if "log_level" in value:
        out["logLevel"] = value["log_level"]
    if "run_tags" in value:
        import capo_omics.types.tag_map

        out["runTags"] = capo_omics.types.tag_map.serialize_json(value["run_tags"])
    if "retention_mode" in value:
        out["retentionMode"] = value["retention_mode"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "workflow_owner_id" in value:
        out["workflowOwnerId"] = value["workflow_owner_id"]
    if "output_bucket_owner_id" in value:
        out["outputBucketOwnerId"] = value["output_bucket_owner_id"]
    if "workflow_version_name" in value:
        out["workflowVersionName"] = value["workflow_version_name"]
    if "networking_mode" in value:
        out["networkingMode"] = value["networking_mode"]
    if "configuration_name" in value:
        out["configurationName"] = value["configuration_name"]
    if "session_policy" in value:
        out["sessionPolicy"] = value["session_policy"]
    if "engine_settings" in value:
        out["engineSettings"] = value["engine_settings"]
    if "scratch_storage_mode" in value:
        out["scratchStorageMode"] = value["scratch_storage_mode"]
    return out


def deserialize_json(data: dict) -> DefaultRunSetting:
    out: DefaultRunSetting = {}  # type: ignore[typeddict-item]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("DefaultRunSetting.workflow_id required")
    if data.get("workflowType") is not None:
        out["workflow_type"] = data["workflowType"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("DefaultRunSetting.role_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("cacheId") is not None:
        out["cache_id"] = data["cacheId"]
    if data.get("cacheBehavior") is not None:
        out["cache_behavior"] = data["cacheBehavior"]
    if data.get("runGroupId") is not None:
        out["run_group_id"] = data["runGroupId"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("parameters") is not None:
        out["parameters"] = data["parameters"]
    if data.get("storageCapacity") is not None:
        out["storage_capacity"] = data["storageCapacity"]
    if data.get("outputUri") is not None:
        out["output_uri"] = data["outputUri"]
    if data.get("logLevel") is not None:
        out["log_level"] = data["logLevel"]
    if data.get("runTags") is not None:
        import capo_omics.types.tag_map

        out["run_tags"] = capo_omics.types.tag_map.deserialize_json(data["runTags"])
    if data.get("retentionMode") is not None:
        out["retention_mode"] = data["retentionMode"]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    if data.get("workflowOwnerId") is not None:
        out["workflow_owner_id"] = data["workflowOwnerId"]
    if data.get("outputBucketOwnerId") is not None:
        out["output_bucket_owner_id"] = data["outputBucketOwnerId"]
    if data.get("workflowVersionName") is not None:
        out["workflow_version_name"] = data["workflowVersionName"]
    if data.get("networkingMode") is not None:
        out["networking_mode"] = data["networkingMode"]
    if data.get("configurationName") is not None:
        out["configuration_name"] = data["configurationName"]
    if data.get("sessionPolicy") is not None:
        out["session_policy"] = data["sessionPolicy"]
    if data.get("engineSettings") is not None:
        out["engine_settings"] = data["engineSettings"]
    if data.get("scratchStorageMode") is not None:
        out["scratch_storage_mode"] = data["scratchStorageMode"]
    return out
