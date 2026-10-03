"""Generated from Smithy shape ``com.amazonaws.batch#JobDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.consumable_resource_properties
    import capo_batch.types.container_properties
    import capo_batch.types.ecs_properties
    import capo_batch.types.eks_properties
    import capo_batch.types.integer
    import capo_batch.types.job_timeout
    import capo_batch.types.node_properties
    import capo_batch.types.orchestration_type
    import capo_batch.types.parameters_map
    import capo_batch.types.platform_capability_list
    import capo_batch.types.retry_strategy
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map


class JobDefinition(TypedDict, closed=True):
    job_definition_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the job definition.</p>"""
    job_definition_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the job definition.</p>"""
    revision: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The revision of the job definition.</p>"""
    status: NotRequired["capo_batch.types.string.String"]
    """<p>The status of the job definition.</p>"""
    type: NotRequired["capo_batch.types.string.String"]
    """<p>The type of job definition. It's either <code>container</code> or <code>multinode</code>. If the job is run on Fargate resources, then <code>multinode</code> isn't supported. For more information about multi-node parallel jobs, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html">Creating a multi-node parallel job definition</a> in the <i>Batch User Guide</i>.</p>"""
    scheduling_priority: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The scheduling priority of the job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.</p>"""
    parameters: NotRequired["capo_batch.types.parameters_map.ParametersMap"]
    """<p>Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a <code>SubmitJob</code> request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html">Job definition parameters</a> in the <i>Batch User Guide</i>.</p>"""
    retry_strategy: NotRequired["capo_batch.types.retry_strategy.RetryStrategy"]
    """<p>The retry strategy to use for failed jobs that are submitted with this job definition.</p>"""
    container_properties: NotRequired[
        "capo_batch.types.container_properties.ContainerProperties"
    ]
    """<p>An object with properties specific to Amazon ECS-based jobs. When <code>containerProperties</code> is used in the job definition, it can't be used in addition to <code>eksProperties</code>, <code>ecsProperties</code>, or <code>nodeProperties</code>.</p>"""
    timeout: NotRequired["capo_batch.types.job_timeout.JobTimeout"]
    """<p>The timeout time for jobs that are submitted with this job definition. After the amount of time you specify passes, Batch terminates your jobs if they aren't finished.</p>"""
    node_properties: NotRequired["capo_batch.types.node_properties.NodeProperties"]
    """<p>An object with properties that are specific to multi-node parallel jobs. When <code>nodeProperties</code> is used in the job definition, it can't be used in addition to <code>containerProperties</code>, <code>ecsProperties</code>, or <code>eksProperties</code>.</p> <note> <p>If the job runs on Fargate resources, don't specify <code>nodeProperties</code>. Use <code>containerProperties</code> instead.</p> </note>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that are applied to the job definition.</p>"""
    propagate_tags: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the <code>FAILED</code> state.</p>"""
    platform_capabilities: NotRequired[
        "capo_batch.types.platform_capability_list.PlatformCapabilityList"
    ]
    """<p>The platform capabilities required by the job definition. If no value is specified, it defaults to <code>EC2</code>. Jobs run on Fargate resources specify <code>FARGATE</code>. Jobs run on Amazon ECS Managed Instances specify <code>MANAGED_INSTANCES</code>.</p>"""
    ecs_properties: NotRequired["capo_batch.types.ecs_properties.EcsProperties"]
    """<p>An object that contains the properties for the Amazon ECS resources of a job.When <code>ecsProperties</code> is used in the job definition, it can't be used in addition to <code>containerProperties</code>, <code>eksProperties</code>, or <code>nodeProperties</code>.</p>"""
    eks_properties: NotRequired["capo_batch.types.eks_properties.EksProperties"]
    """<p>An object with properties that are specific to Amazon EKS-based jobs. When <code>eksProperties</code> is used in the job definition, it can't be used in addition to <code>containerProperties</code>, <code>ecsProperties</code>, or <code>nodeProperties</code>.</p>"""
    container_orchestration_type: NotRequired[
        "capo_batch.types.orchestration_type.OrchestrationType"
    ]
    """<p>The orchestration type of the compute environment. The valid values are <code>ECS</code> (default) or <code>EKS</code>.</p>"""
    consumable_resource_properties: NotRequired[
        "capo_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>Contains a list of consumable resources required by the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDefinition) -> dict:
    out: dict = {}
    if "job_definition_name" in value:
        out["jobDefinitionName"] = value["job_definition_name"]
    if "job_definition_arn" in value:
        out["jobDefinitionArn"] = value["job_definition_arn"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "status" in value:
        out["status"] = value["status"]
    if "type" in value:
        out["type"] = value["type"]
    if "scheduling_priority" in value:
        out["schedulingPriority"] = value["scheduling_priority"]
    if "parameters" in value:
        import capo_batch.types.parameters_map

        out["parameters"] = capo_batch.types.parameters_map.serialize_json(
            value["parameters"]
        )
    if "retry_strategy" in value:
        import capo_batch.types.retry_strategy

        out["retryStrategy"] = capo_batch.types.retry_strategy.serialize_json(
            value["retry_strategy"]
        )
    if "container_properties" in value:
        import capo_batch.types.container_properties

        out["containerProperties"] = (
            capo_batch.types.container_properties.serialize_json(
                value["container_properties"]
            )
        )
    if "timeout" in value:
        import capo_batch.types.job_timeout

        out["timeout"] = capo_batch.types.job_timeout.serialize_json(value["timeout"])
    if "node_properties" in value:
        import capo_batch.types.node_properties

        out["nodeProperties"] = capo_batch.types.node_properties.serialize_json(
            value["node_properties"]
        )
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
    if "ecs_properties" in value:
        import capo_batch.types.ecs_properties

        out["ecsProperties"] = capo_batch.types.ecs_properties.serialize_json(
            value["ecs_properties"]
        )
    if "eks_properties" in value:
        import capo_batch.types.eks_properties

        out["eksProperties"] = capo_batch.types.eks_properties.serialize_json(
            value["eks_properties"]
        )
    if "container_orchestration_type" in value:
        import capo_batch.types.orchestration_type

        out["containerOrchestrationType"] = (
            capo_batch.types.orchestration_type.serialize_json(
                value["container_orchestration_type"]
            )
        )
    if "consumable_resource_properties" in value:
        import capo_batch.types.consumable_resource_properties

        out["consumableResourceProperties"] = (
            capo_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobDefinition:
    out: JobDefinition = {}  # type: ignore[typeddict-item]
    if data.get("jobDefinitionName") is not None:
        out["job_definition_name"] = data["jobDefinitionName"]
    if data.get("jobDefinitionArn") is not None:
        out["job_definition_arn"] = data["jobDefinitionArn"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("schedulingPriority") is not None:
        out["scheduling_priority"] = data["schedulingPriority"]
    if data.get("parameters") is not None:
        import capo_batch.types.parameters_map

        out["parameters"] = capo_batch.types.parameters_map.deserialize_json(
            data["parameters"]
        )
    if data.get("retryStrategy") is not None:
        import capo_batch.types.retry_strategy

        out["retry_strategy"] = capo_batch.types.retry_strategy.deserialize_json(
            data["retryStrategy"]
        )
    if data.get("containerProperties") is not None:
        import capo_batch.types.container_properties

        out["container_properties"] = (
            capo_batch.types.container_properties.deserialize_json(
                data["containerProperties"]
            )
        )
    if data.get("timeout") is not None:
        import capo_batch.types.job_timeout

        out["timeout"] = capo_batch.types.job_timeout.deserialize_json(data["timeout"])
    if data.get("nodeProperties") is not None:
        import capo_batch.types.node_properties

        out["node_properties"] = capo_batch.types.node_properties.deserialize_json(
            data["nodeProperties"]
        )
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
    if data.get("ecsProperties") is not None:
        import capo_batch.types.ecs_properties

        out["ecs_properties"] = capo_batch.types.ecs_properties.deserialize_json(
            data["ecsProperties"]
        )
    if data.get("eksProperties") is not None:
        import capo_batch.types.eks_properties

        out["eks_properties"] = capo_batch.types.eks_properties.deserialize_json(
            data["eksProperties"]
        )
    if data.get("containerOrchestrationType") is not None:
        import capo_batch.types.orchestration_type

        out["container_orchestration_type"] = (
            capo_batch.types.orchestration_type.deserialize_json(
                data["containerOrchestrationType"]
            )
        )
    if data.get("consumableResourceProperties") is not None:
        import capo_batch.types.consumable_resource_properties

        out["consumable_resource_properties"] = (
            capo_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourceProperties"]
            )
        )
    return out
