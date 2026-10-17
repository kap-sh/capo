"""Generated from Smithy shape ``com.amazonaws.omics#StartRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.cache_behavior
    import capo_omics.types.configuration_name
    import capo_omics.types.engine_settings
    import capo_omics.types.networking_mode
    import capo_omics.types.numeric_id_in_arn
    import capo_omics.types.run_group_id
    import capo_omics.types.run_id
    import capo_omics.types.run_log_level
    import capo_omics.types.run_name
    import capo_omics.types.run_output_uri
    import capo_omics.types.run_parameters
    import capo_omics.types.run_request_id
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


class StartRunRequest(TypedDict, closed=True):
    workflow_id: NotRequired["capo_omics.types.workflow_id.WorkflowId"]
    """<p>The run's workflow ID. The <code>workflowId</code> is not the UUID.</p>"""
    workflow_type: NotRequired["capo_omics.types.workflow_type.WorkflowType"]
    """<p>The run's workflow type. The <code>workflowType</code> must be specified if you are running a <code>READY2RUN</code> workflow. If you are running a <code>PRIVATE</code> workflow (default), you do not need to include the workflow type. </p>"""
    run_id: NotRequired["capo_omics.types.run_id.RunId"]
    """<p>The ID of a run to duplicate.</p>"""
    role_arn: "capo_omics.types.run_role_arn.RunRoleArn"
    """<p>A service role for the run. The <code>roleArn</code> requires access to Amazon Web Services HealthOmics, S3, Cloudwatch logs, and EC2. An example <code>roleArn</code> is <code>arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ</code>. In this example, the Amazon Web Services account ID is <code>123456789012</code> and the role name is <code>omics-service-role-serviceRole-W8O1XMPL7QZ</code>.</p>"""
    name: NotRequired["capo_omics.types.run_name.RunName"]
    """<p>A name for the run. This is recommended to view and organize runs in the Amazon Web Services HealthOmics console and CloudWatch logs.</p>"""
    cache_id: NotRequired["capo_omics.types.numeric_id_in_arn.NumericIdInArn"]
    """<p>Identifier of the cache associated with this run. If you don't specify a cache ID, no task outputs are cached for this run.</p>"""
    cache_behavior: NotRequired["capo_omics.types.cache_behavior.CacheBehavior"]
    """<p>The cache behavior for the run. You specify this value if you want to override the default behavior for the cache. You had set the default value when you created the cache. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior">Run cache behavior</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    run_group_id: NotRequired["capo_omics.types.run_group_id.RunGroupId"]
    """<p>The run's group ID. Use a run group to cap the compute resources (and number of concurrent runs) for the runs that you add to the run group.</p>"""
    priority: NotRequired["int"]
    """<p>Use the run priority (highest: 1) to establish the order of runs in a run group when you start a run. If multiple runs share the same priority, the run that was initiated first will have the higher priority. Runs that do not belong to a run group can be assigned a priority. The priorities of these runs are ranked among other runs that are not in a run group. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html#run-priority">Run priority</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    parameters: NotRequired["capo_omics.types.run_parameters.RunParameters"]
    """<p>Parameters for the run. The run needs all required parameters and can include optional parameters. The run cannot include any parameters that are not defined in the parameter template. To retrieve parameters from the run, use the GetRun API operation.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The <code>STATIC</code> storage capacity (in gibibytes, GiB) for this run. The default run storage capacity is 1200 GiB. If your requested storage capacity is unavailable, the system rounds up the value to the nearest 1200 GiB multiple. If the requested storage capacity is still unavailable, the system rounds up the value to the nearest 2400 GiB multiple. This field is not required if the storage type is <code>DYNAMIC</code> (the system ignores any value that you enter).</p>"""
    output_uri: "capo_omics.types.run_output_uri.RunOutputUri"
    """<p>An output S3 URI for the run. The S3 bucket must be in the same region as the workflow. The role ARN must have permission to write to this S3 bucket.</p>"""
    log_level: NotRequired["capo_omics.types.run_log_level.RunLogLevel"]
    """<p>A log level for the run.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Tags for the run. You can add up to 50 tags per run. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    request_id: "capo_omics.types.run_request_id.RunRequestId"
    """<p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>"""
    retention_mode: NotRequired["capo_omics.types.run_retention_mode.RunRetentionMode"]
    """<p>The retention mode for the run. The default value is <code>RETAIN</code>. </p> <p>Amazon Web Services HealthOmics stores a fixed number of runs that are available to the console and API. In the default mode (<code>RETAIN</code>), you need to remove runs manually when the number of run exceeds the maximum. If you set the retention mode to <code>REMOVE</code>, Amazon Web Services HealthOmics automatically removes runs (that have mode set to <code>REMOVE</code>) when the number of run exceeds the maximum. All run logs are available in CloudWatch logs, if you need information about a run that is no longer available to the API.</p> <p>For more information about retention mode, see <a href="https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html">Specifying run retention mode</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    storage_type: NotRequired["capo_omics.types.storage_type.StorageType"]
    """<p>The storage type for the run. If you set the storage type to <code>DYNAMIC</code>, Amazon Web Services HealthOmics dynamically scales the storage up or down, based on file system utilization. By default, the run uses <code>STATIC</code> storage type, which allocates a fixed amount of storage. For more information about <code>DYNAMIC</code> and <code>STATIC</code> storage, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    workflow_owner_id: NotRequired["capo_omics.types.workflow_owner_id.WorkflowOwnerId"]
    """<p>The 12-digit account ID of the workflow owner that is used for running a shared workflow. The workflow owner ID can be retrieved using the <code>GetShare</code> API operation. If you are the workflow owner, you do not need to include this ID.</p>"""
    workflow_version_name: NotRequired[
        "capo_omics.types.workflow_version_name.WorkflowVersionName"
    ]
    """<p>The name of the workflow version. Use workflow versions to track and organize changes to the workflow. If your workflow has multiple versions, the run uses the default version unless you specify a version name. To learn more, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html">Workflow versioning</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    networking_mode: NotRequired["capo_omics.types.networking_mode.NetworkingMode"]
    """<p>Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.</p>"""
    scratch_storage_mode: NotRequired[
        "capo_omics.types.scratch_storage_mode.ScratchStorageMode"
    ]
    """<p>Optional configuration for enabling scratch ephemeral storage mounted at /tmp. If not specified, this will default to SHARED. This configuration is applicable only for CPU tasks. For tasks using GPUs, scratch storage is always LOCAL.</p>"""
    configuration_name: NotRequired[
        "capo_omics.types.configuration_name.ConfigurationName"
    ]
    """<p>Optional configuration name to use for the workflow run.</p>"""
    session_policy: NotRequired["capo_omics.types.session_policy.SessionPolicy"]
    """Optional inline policy json for scoping down permissions via a session policy on the IAM role provided in the roleArn parameter."""
    engine_settings: NotRequired["capo_omics.types.engine_settings.EngineSettings"]
    """<p>Engine-specific settings for the workflow run. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRunRequest) -> dict:
    out: dict = {}
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "workflow_type" in value:
        out["workflowType"] = value["workflow_type"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
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
    out["outputUri"] = value["output_uri"]
    if "log_level" in value:
        out["logLevel"] = value["log_level"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    out["requestId"] = value["request_id"]
    if "retention_mode" in value:
        out["retentionMode"] = value["retention_mode"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "workflow_owner_id" in value:
        out["workflowOwnerId"] = value["workflow_owner_id"]
    if "workflow_version_name" in value:
        out["workflowVersionName"] = value["workflow_version_name"]
    if "networking_mode" in value:
        out["networkingMode"] = value["networking_mode"]
    if "scratch_storage_mode" in value:
        out["scratchStorageMode"] = value["scratch_storage_mode"]
    if "configuration_name" in value:
        out["configurationName"] = value["configuration_name"]
    if "session_policy" in value:
        out["sessionPolicy"] = value["session_policy"]
    if "engine_settings" in value:
        out["engineSettings"] = value["engine_settings"]
    return out


def deserialize_json(data: dict) -> StartRunRequest:
    out: StartRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    if data.get("workflowType") is not None:
        out["workflow_type"] = data["workflowType"]
    if data.get("runId") is not None:
        out["run_id"] = data["runId"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("StartRunRequest.role_arn required")
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
    else:
        raise DeserializationError("StartRunRequest.output_uri required")
    if data.get("logLevel") is not None:
        out["log_level"] = data["logLevel"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("StartRunRequest.request_id required")
    if data.get("retentionMode") is not None:
        out["retention_mode"] = data["retentionMode"]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    if data.get("workflowOwnerId") is not None:
        out["workflow_owner_id"] = data["workflowOwnerId"]
    if data.get("workflowVersionName") is not None:
        out["workflow_version_name"] = data["workflowVersionName"]
    if data.get("networkingMode") is not None:
        out["networking_mode"] = data["networkingMode"]
    if data.get("scratchStorageMode") is not None:
        out["scratch_storage_mode"] = data["scratchStorageMode"]
    if data.get("configurationName") is not None:
        out["configuration_name"] = data["configurationName"]
    if data.get("sessionPolicy") is not None:
        out["session_policy"] = data["sessionPolicy"]
    if data.get("engineSettings") is not None:
        out["engine_settings"] = data["engineSettings"]
    return out
