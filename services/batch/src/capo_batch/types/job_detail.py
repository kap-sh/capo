"""Generated from Smithy shape ``com.amazonaws.batch#JobDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.array_properties_detail
    import capo_batch.types.attempt_details
    import capo_batch.types.boolean
    import capo_batch.types.consumable_resource_properties
    import capo_batch.types.container_detail
    import capo_batch.types.ecs_properties_detail
    import capo_batch.types.eks_attempt_details
    import capo_batch.types.eks_properties_detail
    import capo_batch.types.integer
    import capo_batch.types.job_dependency_list
    import capo_batch.types.job_status
    import capo_batch.types.job_timeout
    import capo_batch.types.long
    import capo_batch.types.node_details
    import capo_batch.types.node_properties
    import capo_batch.types.parameters_map
    import capo_batch.types.platform_capability_list
    import capo_batch.types.retry_strategy
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map


class JobDetail(TypedDict, closed=True):
    job_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_name: NotRequired["capo_batch.types.string.String"]
    """<p>The job name.</p>"""
    job_id: NotRequired["capo_batch.types.string.String"]
    """<p>The job ID.</p>"""
    job_queue: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job queue that the job is associated with.</p>"""
    status: NotRequired["capo_batch.types.job_status.JobStatus"]
    """<p>The current status for the job.</p> <note> <p>If your jobs don't progress to <code>STARTING</code>, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#job_stuck_in_runnable">Jobs stuck in RUNNABLE status</a> in the troubleshooting section of the <i>Batch User Guide</i>.</p> </note>"""
    share_identifier: NotRequired["capo_batch.types.string.String"]
    """<p>The share identifier for the job.</p>"""
    scheduling_priority: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The scheduling policy of the job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.</p>"""
    attempts: NotRequired["capo_batch.types.attempt_details.AttemptDetails"]
    """<p>A list of job attempts that are associated with this job.</p>"""
    status_reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short, human-readable string to provide more details for the current status of the job.</p> <ul> <li> <p> <code>CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY</code> - All compute environments have insufficient capacity to service the job.</p> </li> <li> <p> <code>MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE</code> - All compute environments have a <code>maxVcpu</code> setting that is smaller than the job requirements.</p> </li> <li> <p> <code>MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT</code> - All compute environments have no connected instances that meet the job requirements.</p> </li> <li> <p> <code>MISCONFIGURATION:SERVICE_ROLE_PERMISSIONS</code> - All compute environments have problems with the service role permissions.</p> </li> </ul>"""
    created_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the <code>SUBMITTED</code> state. This is specifically at the time <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html">SubmitJob</a> was called. For array child jobs, this is when the child job was spawned by its parent and entered the <code>PENDING</code> state.</p>"""
    retry_strategy: NotRequired["capo_batch.types.retry_strategy.RetryStrategy"]
    """<p>The retry strategy to use for this job if an attempt fails.</p>"""
    started_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the job was started. More specifically, it's when the job transitioned from the <code>STARTING</code> state to the <code>RUNNING</code> state. </p>"""
    stopped_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the job was stopped. More specifically, it's when the job transitioned from the <code>RUNNING</code> state to a terminal state, such as <code>SUCCEEDED</code> or <code>FAILED</code>.</p>"""
    depends_on: NotRequired["capo_batch.types.job_dependency_list.JobDependencyList"]
    """<p>A list of job IDs that this job depends on.</p>"""
    job_definition: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job definition that this job uses.</p>"""
    parameters: NotRequired["capo_batch.types.parameters_map.ParametersMap"]
    """<p>Additional parameters that are passed to the job that replace parameter substitution placeholders or override any corresponding parameter defaults from the job definition.</p>"""
    container: NotRequired["capo_batch.types.container_detail.ContainerDetail"]
    """<p>An object that represents the details for the container that's associated with the job. If the details are for a multiple-container job, this object will be empty. </p>"""
    node_details: NotRequired["capo_batch.types.node_details.NodeDetails"]
    """<p>An object that represents the details of a node that's associated with a multi-node parallel job.</p>"""
    node_properties: NotRequired["capo_batch.types.node_properties.NodeProperties"]
    """<p>An object that represents the node properties of a multi-node parallel job.</p> <note> <p>This isn't applicable to jobs that are running on Fargate resources.</p> </note>"""
    array_properties: NotRequired[
        "capo_batch.types.array_properties_detail.ArrayPropertiesDetail"
    ]
    """<p>The array properties of the job, if it's an array job.</p>"""
    timeout: NotRequired["capo_batch.types.job_timeout.JobTimeout"]
    """<p>The timeout configuration for the job.</p>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that are applied to the job.</p>"""
    propagate_tags: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the <code>FAILED</code> state.</p>"""
    platform_capabilities: NotRequired[
        "capo_batch.types.platform_capability_list.PlatformCapabilityList"
    ]
    """<p>The platform capabilities required by the job definition. If no value is specified, it defaults to <code>EC2</code>. Jobs run on Fargate resources specify <code>FARGATE</code>. Jobs run on Amazon ECS Managed Instances specify <code>MANAGED_INSTANCES</code>.</p>"""
    eks_properties: NotRequired[
        "capo_batch.types.eks_properties_detail.EksPropertiesDetail"
    ]
    """<p>An object with various properties that are specific to Amazon EKS based jobs. </p>"""
    eks_attempts: NotRequired["capo_batch.types.eks_attempt_details.EksAttemptDetails"]
    """<p>A list of job attempts that are associated with this job.</p>"""
    ecs_properties: NotRequired[
        "capo_batch.types.ecs_properties_detail.EcsPropertiesDetail"
    ]
    """<p>An object with properties that are specific to Amazon ECS-based jobs. </p>"""
    is_cancelled: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Indicates whether the job is cancelled.</p>"""
    is_terminated: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Indicates whether the job is terminated.</p>"""
    consumable_resource_properties: NotRequired[
        "capo_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>Contains a list of consumable resources required by the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetail) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    if "status" in value:
        import capo_batch.types.job_status

        out["status"] = capo_batch.types.job_status.serialize_json(value["status"])
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "scheduling_priority" in value:
        out["schedulingPriority"] = value["scheduling_priority"]
    if "attempts" in value:
        import capo_batch.types.attempt_details

        out["attempts"] = capo_batch.types.attempt_details.serialize_json(
            value["attempts"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "retry_strategy" in value:
        import capo_batch.types.retry_strategy

        out["retryStrategy"] = capo_batch.types.retry_strategy.serialize_json(
            value["retry_strategy"]
        )
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "stopped_at" in value:
        out["stoppedAt"] = value["stopped_at"]
    if "depends_on" in value:
        import capo_batch.types.job_dependency_list

        out["dependsOn"] = capo_batch.types.job_dependency_list.serialize_json(
            value["depends_on"]
        )
    if "job_definition" in value:
        out["jobDefinition"] = value["job_definition"]
    if "parameters" in value:
        import capo_batch.types.parameters_map

        out["parameters"] = capo_batch.types.parameters_map.serialize_json(
            value["parameters"]
        )
    if "container" in value:
        import capo_batch.types.container_detail

        out["container"] = capo_batch.types.container_detail.serialize_json(
            value["container"]
        )
    if "node_details" in value:
        import capo_batch.types.node_details

        out["nodeDetails"] = capo_batch.types.node_details.serialize_json(
            value["node_details"]
        )
    if "node_properties" in value:
        import capo_batch.types.node_properties

        out["nodeProperties"] = capo_batch.types.node_properties.serialize_json(
            value["node_properties"]
        )
    if "array_properties" in value:
        import capo_batch.types.array_properties_detail

        out["arrayProperties"] = (
            capo_batch.types.array_properties_detail.serialize_json(
                value["array_properties"]
            )
        )
    if "timeout" in value:
        import capo_batch.types.job_timeout

        out["timeout"] = capo_batch.types.job_timeout.serialize_json(value["timeout"])
    if "tags" in value:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.serialize_json(value["tags"])
    if "propagate_tags" in value:
        out["propagateTags"] = value["propagate_tags"]
    if "platform_capabilities" in value:
        import capo_batch.types.platform_capability_list

        out["platformCapabilities"] = (
            capo_batch.types.platform_capability_list.serialize_json(
                value["platform_capabilities"]
            )
        )
    if "eks_properties" in value:
        import capo_batch.types.eks_properties_detail

        out["eksProperties"] = capo_batch.types.eks_properties_detail.serialize_json(
            value["eks_properties"]
        )
    if "eks_attempts" in value:
        import capo_batch.types.eks_attempt_details

        out["eksAttempts"] = capo_batch.types.eks_attempt_details.serialize_json(
            value["eks_attempts"]
        )
    if "ecs_properties" in value:
        import capo_batch.types.ecs_properties_detail

        out["ecsProperties"] = capo_batch.types.ecs_properties_detail.serialize_json(
            value["ecs_properties"]
        )
    if "is_cancelled" in value:
        out["isCancelled"] = value["is_cancelled"]
    if "is_terminated" in value:
        out["isTerminated"] = value["is_terminated"]
    if "consumable_resource_properties" in value:
        import capo_batch.types.consumable_resource_properties

        out["consumableResourceProperties"] = (
            capo_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobDetail:
    out: JobDetail = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("jobQueue") is not None:
        out["job_queue"] = data["jobQueue"]
    if data.get("status") is not None:
        import capo_batch.types.job_status

        out["status"] = capo_batch.types.job_status.deserialize_json(data["status"])
    if data.get("shareIdentifier") is not None:
        out["share_identifier"] = data["shareIdentifier"]
    if data.get("schedulingPriority") is not None:
        out["scheduling_priority"] = data["schedulingPriority"]
    if data.get("attempts") is not None:
        import capo_batch.types.attempt_details

        out["attempts"] = capo_batch.types.attempt_details.deserialize_json(
            data["attempts"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    if data.get("retryStrategy") is not None:
        import capo_batch.types.retry_strategy

        out["retry_strategy"] = capo_batch.types.retry_strategy.deserialize_json(
            data["retryStrategy"]
        )
    if data.get("startedAt") is not None:
        out["started_at"] = data["startedAt"]
    if data.get("stoppedAt") is not None:
        out["stopped_at"] = data["stoppedAt"]
    if data.get("dependsOn") is not None:
        import capo_batch.types.job_dependency_list

        out["depends_on"] = capo_batch.types.job_dependency_list.deserialize_json(
            data["dependsOn"]
        )
    if data.get("jobDefinition") is not None:
        out["job_definition"] = data["jobDefinition"]
    if data.get("parameters") is not None:
        import capo_batch.types.parameters_map

        out["parameters"] = capo_batch.types.parameters_map.deserialize_json(
            data["parameters"]
        )
    if data.get("container") is not None:
        import capo_batch.types.container_detail

        out["container"] = capo_batch.types.container_detail.deserialize_json(
            data["container"]
        )
    if data.get("nodeDetails") is not None:
        import capo_batch.types.node_details

        out["node_details"] = capo_batch.types.node_details.deserialize_json(
            data["nodeDetails"]
        )
    if data.get("nodeProperties") is not None:
        import capo_batch.types.node_properties

        out["node_properties"] = capo_batch.types.node_properties.deserialize_json(
            data["nodeProperties"]
        )
    if data.get("arrayProperties") is not None:
        import capo_batch.types.array_properties_detail

        out["array_properties"] = (
            capo_batch.types.array_properties_detail.deserialize_json(
                data["arrayProperties"]
            )
        )
    if data.get("timeout") is not None:
        import capo_batch.types.job_timeout

        out["timeout"] = capo_batch.types.job_timeout.deserialize_json(data["timeout"])
    if data.get("tags") is not None:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    if data.get("propagateTags") is not None:
        out["propagate_tags"] = data["propagateTags"]
    if data.get("platformCapabilities") is not None:
        import capo_batch.types.platform_capability_list

        out["platform_capabilities"] = (
            capo_batch.types.platform_capability_list.deserialize_json(
                data["platformCapabilities"]
            )
        )
    if data.get("eksProperties") is not None:
        import capo_batch.types.eks_properties_detail

        out["eks_properties"] = capo_batch.types.eks_properties_detail.deserialize_json(
            data["eksProperties"]
        )
    if data.get("eksAttempts") is not None:
        import capo_batch.types.eks_attempt_details

        out["eks_attempts"] = capo_batch.types.eks_attempt_details.deserialize_json(
            data["eksAttempts"]
        )
    if data.get("ecsProperties") is not None:
        import capo_batch.types.ecs_properties_detail

        out["ecs_properties"] = capo_batch.types.ecs_properties_detail.deserialize_json(
            data["ecsProperties"]
        )
    if data.get("isCancelled") is not None:
        out["is_cancelled"] = data["isCancelled"]
    if data.get("isTerminated") is not None:
        out["is_terminated"] = data["isTerminated"]
    if data.get("consumableResourceProperties") is not None:
        import capo_batch.types.consumable_resource_properties

        out["consumable_resource_properties"] = (
            capo_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourceProperties"]
            )
        )
    return out
