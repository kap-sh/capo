"""Generated from Smithy shape ``com.amazonaws.batch#SubmitJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.array_properties
    import capo_batch.types.boolean
    import capo_batch.types.consumable_resource_properties
    import capo_batch.types.container_overrides
    import capo_batch.types.ecs_properties_override
    import capo_batch.types.eks_properties_override
    import capo_batch.types.integer
    import capo_batch.types.job_dependency_list
    import capo_batch.types.job_timeout
    import capo_batch.types.node_overrides
    import capo_batch.types.parameters_map
    import capo_batch.types.retry_strategy
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map


class SubmitJobRequest(TypedDict, closed=True):
    job_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the job. It can be up to 128 letters long. The first character must be alphanumeric, can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    job_queue: NotRequired["capo_batch.types.string.String"]
    """<p>The job queue where the job is submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue.</p>"""
    share_identifier: NotRequired["capo_batch.types.string.String"]
    """<p>The share identifier for the job. Don't specify this parameter if the job queue doesn't have a fair-share scheduling policy. If the job queue has a fair-share scheduling policy, then this parameter must be specified.</p> <p>This string is limited to 255 alphanumeric characters, and can be followed by an asterisk (*).</p>"""
    scheduling_priority_override: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The scheduling priority for the job. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority. This overrides any scheduling priority in the job definition and works only within a single share identifier.</p> <p>The minimum supported value is 0 and the maximum supported value is 9999.</p>"""
    array_properties: NotRequired["capo_batch.types.array_properties.ArrayProperties"]
    """<p>The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html">Array Jobs</a> in the <i>Batch User Guide</i>.</p>"""
    depends_on: NotRequired["capo_batch.types.job_dependency_list.JobDependencyList"]
    """<p>A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a <code>SEQUENTIAL</code> type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an <code>N_TO_N</code> type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.</p>"""
    job_definition: NotRequired["capo_batch.types.string.String"]
    """<p>The job definition used by this job. This value can be one of <code>definition-name</code>, <code>definition-name:revision</code>, or the Amazon Resource Name (ARN) for the job definition, with or without the revision (<code>arn:aws:batch:<i>region</i>:<i>account</i>:job-definition/<i>definition-name</i>:<i>revision</i> </code>, or <code>arn:aws:batch:<i>region</i>:<i>account</i>:job-definition/<i>definition-name</i> </code>).</p> <p>If the revision is not specified, then the latest active revision is used.</p>"""
    parameters: NotRequired["capo_batch.types.parameters_map.ParametersMap"]
    """<p>Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters in a <code>SubmitJob</code> request override any corresponding parameter defaults from the job definition.</p>"""
    container_overrides: NotRequired[
        "capo_batch.types.container_overrides.ContainerOverrides"
    ]
    """<p>An object with properties that override the defaults for the job definition that specify the name of a container in the specified job definition and the overrides it should receive. You can override the default command for a container, which is specified in the job definition or the Docker image, with a <code>command</code> override. You can also override existing environment variables on a container or add new environment variables to it with an <code>environment</code> override.</p>"""
    node_overrides: NotRequired["capo_batch.types.node_overrides.NodeOverrides"]
    """<p>A list of node overrides in JSON format that specify the node range to target and the container overrides for that node range.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources; use <code>containerOverrides</code> instead.</p> </note>"""
    retry_strategy: NotRequired["capo_batch.types.retry_strategy.RetryStrategy"]
    """<p>The retry strategy to use for failed jobs from this <a>SubmitJob</a> operation. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.</p>"""
    propagate_tags: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the <code>FAILED</code> state. When specified, this overrides the tag propagation setting in the job definition.</p>"""
    timeout: NotRequired["capo_batch.types.job_timeout.JobTimeout"]
    """<p>The timeout configuration for this <a>SubmitJob</a> operation. You can specify a timeout duration after which Batch terminates your jobs if they haven't finished. If a job is terminated due to a timeout, it isn't retried. The minimum value for the timeout is 60 seconds. This configuration overrides any timeout configuration specified in the job definition. For array jobs, child jobs have the same timeout configuration as the parent job. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html">Job Timeouts</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that you apply to the job request to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in <i>Amazon Web Services General Reference</i>.</p>"""
    eks_properties_override: NotRequired[
        "capo_batch.types.eks_properties_override.EksPropertiesOverride"
    ]
    """<p>An object, with properties that override defaults for the job definition, can only be specified for jobs that are run on Amazon EKS resources.</p>"""
    ecs_properties_override: NotRequired[
        "capo_batch.types.ecs_properties_override.EcsPropertiesOverride"
    ]
    """<p>An object, with properties that override defaults for the job definition, can only be specified for jobs that are run on Amazon ECS resources.</p>"""
    consumable_resource_properties_override: NotRequired[
        "capo_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>An object that contains overrides for the consumable resources of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmitJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "scheduling_priority_override" in value:
        out["schedulingPriorityOverride"] = value["scheduling_priority_override"]
    if "array_properties" in value:
        import capo_batch.types.array_properties

        out["arrayProperties"] = capo_batch.types.array_properties.serialize_json(
            value["array_properties"]
        )
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
    if "container_overrides" in value:
        import capo_batch.types.container_overrides

        out["containerOverrides"] = capo_batch.types.container_overrides.serialize_json(
            value["container_overrides"]
        )
    if "node_overrides" in value:
        import capo_batch.types.node_overrides

        out["nodeOverrides"] = capo_batch.types.node_overrides.serialize_json(
            value["node_overrides"]
        )
    if "retry_strategy" in value:
        import capo_batch.types.retry_strategy

        out["retryStrategy"] = capo_batch.types.retry_strategy.serialize_json(
            value["retry_strategy"]
        )
    if "propagate_tags" in value:
        out["propagateTags"] = value["propagate_tags"]
    if "timeout" in value:
        import capo_batch.types.job_timeout

        out["timeout"] = capo_batch.types.job_timeout.serialize_json(value["timeout"])
    if "tags" in value:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.serialize_json(value["tags"])
    if "eks_properties_override" in value:
        import capo_batch.types.eks_properties_override

        out["eksPropertiesOverride"] = (
            capo_batch.types.eks_properties_override.serialize_json(
                value["eks_properties_override"]
            )
        )
    if "ecs_properties_override" in value:
        import capo_batch.types.ecs_properties_override

        out["ecsPropertiesOverride"] = (
            capo_batch.types.ecs_properties_override.serialize_json(
                value["ecs_properties_override"]
            )
        )
    if "consumable_resource_properties_override" in value:
        import capo_batch.types.consumable_resource_properties

        out["consumableResourcePropertiesOverride"] = (
            capo_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties_override"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubmitJobRequest:
    out: SubmitJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    if data.get("jobQueue") is not None:
        out["job_queue"] = data["jobQueue"]
    if data.get("shareIdentifier") is not None:
        out["share_identifier"] = data["shareIdentifier"]
    if data.get("schedulingPriorityOverride") is not None:
        out["scheduling_priority_override"] = data["schedulingPriorityOverride"]
    if data.get("arrayProperties") is not None:
        import capo_batch.types.array_properties

        out["array_properties"] = capo_batch.types.array_properties.deserialize_json(
            data["arrayProperties"]
        )
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
    if data.get("containerOverrides") is not None:
        import capo_batch.types.container_overrides

        out["container_overrides"] = (
            capo_batch.types.container_overrides.deserialize_json(
                data["containerOverrides"]
            )
        )
    if data.get("nodeOverrides") is not None:
        import capo_batch.types.node_overrides

        out["node_overrides"] = capo_batch.types.node_overrides.deserialize_json(
            data["nodeOverrides"]
        )
    if data.get("retryStrategy") is not None:
        import capo_batch.types.retry_strategy

        out["retry_strategy"] = capo_batch.types.retry_strategy.deserialize_json(
            data["retryStrategy"]
        )
    if data.get("propagateTags") is not None:
        out["propagate_tags"] = data["propagateTags"]
    if data.get("timeout") is not None:
        import capo_batch.types.job_timeout

        out["timeout"] = capo_batch.types.job_timeout.deserialize_json(data["timeout"])
    if data.get("tags") is not None:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    if data.get("eksPropertiesOverride") is not None:
        import capo_batch.types.eks_properties_override

        out["eks_properties_override"] = (
            capo_batch.types.eks_properties_override.deserialize_json(
                data["eksPropertiesOverride"]
            )
        )
    if data.get("ecsPropertiesOverride") is not None:
        import capo_batch.types.ecs_properties_override

        out["ecs_properties_override"] = (
            capo_batch.types.ecs_properties_override.deserialize_json(
                data["ecsPropertiesOverride"]
            )
        )
    if data.get("consumableResourcePropertiesOverride") is not None:
        import capo_batch.types.consumable_resource_properties

        out["consumable_resource_properties_override"] = (
            capo_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourcePropertiesOverride"]
            )
        )
    return out
