"""Generated from Smithy shape ``com.amazonaws.omics#GetRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.accelerators
    import capo_omics.types.batch_id
    import capo_omics.types.cache_behavior
    import capo_omics.types.configuration_details
    import capo_omics.types.engine_settings
    import capo_omics.types.engine_version
    import capo_omics.types.networking_mode
    import capo_omics.types.numeric_id_in_arn
    import capo_omics.types.run_arn
    import capo_omics.types.run_failure_reason
    import capo_omics.types.run_group_id
    import capo_omics.types.run_id
    import capo_omics.types.run_log_level
    import capo_omics.types.run_log_location
    import capo_omics.types.run_name
    import capo_omics.types.run_output_uri
    import capo_omics.types.run_parameters
    import capo_omics.types.run_resource_digests
    import capo_omics.types.run_retention_mode
    import capo_omics.types.run_role_arn
    import capo_omics.types.run_started_by
    import capo_omics.types.run_status
    import capo_omics.types.run_status_message
    import capo_omics.types.run_timestamp
    import capo_omics.types.run_uuid
    import capo_omics.types.scratch_storage_mode
    import capo_omics.types.session_policy
    import capo_omics.types.storage_type
    import capo_omics.types.tag_map
    import capo_omics.types.vpc_config_response
    import capo_omics.types.workflow_definition
    import capo_omics.types.workflow_digest
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_owner_id
    import capo_omics.types.workflow_type
    import capo_omics.types.workflow_uuid
    import capo_omics.types.workflow_version_name


class GetRunResponse(TypedDict, closed=True):
    arn: NotRequired["capo_omics.types.run_arn.RunArn"]
    """<p>The run's ARN.</p>"""
    id: NotRequired["capo_omics.types.run_id.RunId"]
    """<p>The run's ID.</p>"""
    cache_id: NotRequired["capo_omics.types.numeric_id_in_arn.NumericIdInArn"]
    """<p>The run cache associated with the run.</p>"""
    cache_behavior: NotRequired["capo_omics.types.cache_behavior.CacheBehavior"]
    """<p>The run cache behavior for the run.</p>"""
    engine_version: NotRequired["capo_omics.types.engine_version.EngineVersion"]
    """<p>The actual Nextflow engine version that Amazon Web Services HealthOmics used for the run. The other workflow definition languages don't provide a value for this field.</p>"""
    status: NotRequired["capo_omics.types.run_status.RunStatus"]
    """<p>The run's status.</p>"""
    workflow_id: NotRequired["capo_omics.types.workflow_id.WorkflowId"]
    """<p>The run's workflow ID.</p>"""
    workflow_type: NotRequired["capo_omics.types.workflow_type.WorkflowType"]
    """<p>The run's workflow type.</p>"""
    run_id: NotRequired["capo_omics.types.run_id.RunId"]
    """<p>The run's ID.</p>"""
    role_arn: NotRequired["capo_omics.types.run_role_arn.RunRoleArn"]
    """<p>The run's service role ARN.</p>"""
    name: NotRequired["capo_omics.types.run_name.RunName"]
    """<p>The run's name.</p>"""
    run_group_id: NotRequired["capo_omics.types.run_group_id.RunGroupId"]
    """<p>The run's group ID.</p>"""
    batch_id: NotRequired["capo_omics.types.batch_id.BatchId"]
    """<p>The run's batch ID.</p>"""
    priority: NotRequired["int"]
    """<p>The run's priority.</p>"""
    definition: NotRequired["capo_omics.types.workflow_definition.WorkflowDefinition"]
    """<p>The run's definition.</p>"""
    digest: NotRequired["capo_omics.types.workflow_digest.WorkflowDigest"]
    """<p>The run's digest.</p>"""
    parameters: NotRequired["capo_omics.types.run_parameters.RunParameters"]
    """<p>The run's parameters.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The run's storage capacity in gibibytes. For dynamic storage, after the run has completed, this value is the maximum amount of storage used during the run.</p>"""
    output_uri: NotRequired["capo_omics.types.run_output_uri.RunOutputUri"]
    """<p>The run's output URI.</p>"""
    log_level: NotRequired["capo_omics.types.run_log_level.RunLogLevel"]
    """<p>The run's log level.</p>"""
    resource_digests: NotRequired[
        "capo_omics.types.run_resource_digests.RunResourceDigests"
    ]
    """<p>The run's resource digests.</p>"""
    started_by: NotRequired["capo_omics.types.run_started_by.RunStartedBy"]
    """<p>Who started the run.</p>"""
    creation_time: NotRequired["capo_omics.types.run_timestamp.RunTimestamp"]
    """<p>When the run was created.</p>"""
    start_time: NotRequired["capo_omics.types.run_timestamp.RunTimestamp"]
    """<p>When the run started.</p>"""
    stop_time: NotRequired["capo_omics.types.run_timestamp.RunTimestamp"]
    """<p>The run's stop time.</p>"""
    status_message: NotRequired["capo_omics.types.run_status_message.RunStatusMessage"]
    """<p>The run's status message.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>The run's tags.</p>"""
    accelerators: NotRequired["capo_omics.types.accelerators.Accelerators"]
    """<p>The computational accelerator used to run the workflow.</p>"""
    retention_mode: NotRequired["capo_omics.types.run_retention_mode.RunRetentionMode"]
    """<p>The run's retention mode.</p>"""
    failure_reason: NotRequired["capo_omics.types.run_failure_reason.RunFailureReason"]
    """<p>The reason a run has failed.</p>"""
    log_location: NotRequired["capo_omics.types.run_log_location.RunLogLocation"]
    """<p>The location of the run log.</p>"""
    uuid: NotRequired["capo_omics.types.run_uuid.RunUuid"]
    """<p>The universally unique identifier for a run.</p>"""
    run_output_uri: NotRequired["capo_omics.types.run_output_uri.RunOutputUri"]
    """<p>The destination for workflow outputs.</p>"""
    storage_type: NotRequired["capo_omics.types.storage_type.StorageType"]
    """<p>The run's storage type.</p>"""
    workflow_owner_id: NotRequired["capo_omics.types.workflow_owner_id.WorkflowOwnerId"]
    """<p>The ID of the workflow owner.</p>"""
    workflow_version_name: NotRequired[
        "capo_omics.types.workflow_version_name.WorkflowVersionName"
    ]
    """<p>The workflow version name.</p>"""
    workflow_uuid: NotRequired["capo_omics.types.workflow_uuid.WorkflowUuid"]
    """<p>The universally unique identifier (UUID) value for the workflow.</p>"""
    networking_mode: NotRequired["capo_omics.types.networking_mode.NetworkingMode"]
    """<p>Configuration for run networking behavior. If absent, this will default to RESTRICTED.</p>"""
    scratch_storage_mode: NotRequired[
        "capo_omics.types.scratch_storage_mode.ScratchStorageMode"
    ]
    """<p>Optional configuration for enabling scratch ephemeral storage mounted at /tmp. If absent, this will default to SHARED. This configuration is applicable only for CPU tasks. For tasks using GPUs, scratch storage is always LOCAL.</p>"""
    configuration: NotRequired[
        "capo_omics.types.configuration_details.ConfigurationDetails"
    ]
    """<p>Configuration details for the workflow run.</p>"""
    vpc_config: NotRequired["capo_omics.types.vpc_config_response.VpcConfigResponse"]
    """<p>VPC configuration for the workflow run.</p>"""
    engine_settings: NotRequired["capo_omics.types.engine_settings.EngineSettings"]
    """<p>The engine-specific settings for the workflow run.</p>"""
    session_policy: NotRequired["capo_omics.types.session_policy.SessionPolicy"]
    """Inline policy json for scoping down permissions via a session policy on the IAM role."""


# --- restJson1 ser/de ---
def serialize_json(value: GetRunResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "cache_id" in value:
        out["cacheId"] = value["cache_id"]
    if "cache_behavior" in value:
        out["cacheBehavior"] = value["cache_behavior"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "status" in value:
        out["status"] = value["status"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "workflow_type" in value:
        out["workflowType"] = value["workflow_type"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "run_group_id" in value:
        out["runGroupId"] = value["run_group_id"]
    if "batch_id" in value:
        out["batchId"] = value["batch_id"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "definition" in value:
        out["definition"] = value["definition"]
    if "digest" in value:
        out["digest"] = value["digest"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    if "storage_capacity" in value:
        out["storageCapacity"] = value["storage_capacity"]
    if "output_uri" in value:
        out["outputUri"] = value["output_uri"]
    if "log_level" in value:
        out["logLevel"] = value["log_level"]
    if "resource_digests" in value:
        import capo_omics.types.run_resource_digests

        out["resourceDigests"] = capo_omics.types.run_resource_digests.serialize_json(
            value["resource_digests"]
        )
    if "started_by" in value:
        out["startedBy"] = value["started_by"]
    if "creation_time" in value:
        import capo_omics.types.run_timestamp

        out["creationTime"] = capo_omics.types.run_timestamp.serialize_json(
            value["creation_time"]
        )
    if "start_time" in value:
        import capo_omics.types.run_timestamp

        out["startTime"] = capo_omics.types.run_timestamp.serialize_json(
            value["start_time"]
        )
    if "stop_time" in value:
        import capo_omics.types.run_timestamp

        out["stopTime"] = capo_omics.types.run_timestamp.serialize_json(
            value["stop_time"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "accelerators" in value:
        out["accelerators"] = value["accelerators"]
    if "retention_mode" in value:
        out["retentionMode"] = value["retention_mode"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "log_location" in value:
        import capo_omics.types.run_log_location

        out["logLocation"] = capo_omics.types.run_log_location.serialize_json(
            value["log_location"]
        )
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "run_output_uri" in value:
        out["runOutputUri"] = value["run_output_uri"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "workflow_owner_id" in value:
        out["workflowOwnerId"] = value["workflow_owner_id"]
    if "workflow_version_name" in value:
        out["workflowVersionName"] = value["workflow_version_name"]
    if "workflow_uuid" in value:
        out["workflowUuid"] = value["workflow_uuid"]
    if "networking_mode" in value:
        out["networkingMode"] = value["networking_mode"]
    if "scratch_storage_mode" in value:
        out["scratchStorageMode"] = value["scratch_storage_mode"]
    if "configuration" in value:
        import capo_omics.types.configuration_details

        out["configuration"] = capo_omics.types.configuration_details.serialize_json(
            value["configuration"]
        )
    if "vpc_config" in value:
        import capo_omics.types.vpc_config_response

        out["vpcConfig"] = capo_omics.types.vpc_config_response.serialize_json(
            value["vpc_config"]
        )
    if "engine_settings" in value:
        out["engineSettings"] = value["engine_settings"]
    if "session_policy" in value:
        out["sessionPolicy"] = value["session_policy"]
    return out


def deserialize_json(data: dict) -> GetRunResponse:
    out: GetRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("cacheId") is not None:
        out["cache_id"] = data["cacheId"]
    if data.get("cacheBehavior") is not None:
        out["cache_behavior"] = data["cacheBehavior"]
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    if data.get("workflowType") is not None:
        out["workflow_type"] = data["workflowType"]
    if data.get("runId") is not None:
        out["run_id"] = data["runId"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("runGroupId") is not None:
        out["run_group_id"] = data["runGroupId"]
    if data.get("batchId") is not None:
        out["batch_id"] = data["batchId"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    if data.get("digest") is not None:
        out["digest"] = data["digest"]
    if data.get("parameters") is not None:
        out["parameters"] = data["parameters"]
    if data.get("storageCapacity") is not None:
        out["storage_capacity"] = data["storageCapacity"]
    if data.get("outputUri") is not None:
        out["output_uri"] = data["outputUri"]
    if data.get("logLevel") is not None:
        out["log_level"] = data["logLevel"]
    if data.get("resourceDigests") is not None:
        import capo_omics.types.run_resource_digests

        out["resource_digests"] = (
            capo_omics.types.run_resource_digests.deserialize_json(
                data["resourceDigests"]
            )
        )
    if data.get("startedBy") is not None:
        out["started_by"] = data["startedBy"]
    if data.get("creationTime") is not None:
        import capo_omics.types.run_timestamp

        out["creation_time"] = capo_omics.types.run_timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("startTime") is not None:
        import capo_omics.types.run_timestamp

        out["start_time"] = capo_omics.types.run_timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("stopTime") is not None:
        import capo_omics.types.run_timestamp

        out["stop_time"] = capo_omics.types.run_timestamp.deserialize_json(
            data["stopTime"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("accelerators") is not None:
        out["accelerators"] = data["accelerators"]
    if data.get("retentionMode") is not None:
        out["retention_mode"] = data["retentionMode"]
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("logLocation") is not None:
        import capo_omics.types.run_log_location

        out["log_location"] = capo_omics.types.run_log_location.deserialize_json(
            data["logLocation"]
        )
    if data.get("uuid") is not None:
        out["uuid"] = data["uuid"]
    if data.get("runOutputUri") is not None:
        out["run_output_uri"] = data["runOutputUri"]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    if data.get("workflowOwnerId") is not None:
        out["workflow_owner_id"] = data["workflowOwnerId"]
    if data.get("workflowVersionName") is not None:
        out["workflow_version_name"] = data["workflowVersionName"]
    if data.get("workflowUuid") is not None:
        out["workflow_uuid"] = data["workflowUuid"]
    if data.get("networkingMode") is not None:
        out["networking_mode"] = data["networkingMode"]
    if data.get("scratchStorageMode") is not None:
        out["scratch_storage_mode"] = data["scratchStorageMode"]
    if data.get("configuration") is not None:
        import capo_omics.types.configuration_details

        out["configuration"] = capo_omics.types.configuration_details.deserialize_json(
            data["configuration"]
        )
    if data.get("vpcConfig") is not None:
        import capo_omics.types.vpc_config_response

        out["vpc_config"] = capo_omics.types.vpc_config_response.deserialize_json(
            data["vpcConfig"]
        )
    if data.get("engineSettings") is not None:
        out["engine_settings"] = data["engineSettings"]
    if data.get("sessionPolicy") is not None:
        out["session_policy"] = data["sessionPolicy"]
    return out
