"""Generated from Smithy shape ``com.amazonaws.batch#JobQueueDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.compute_environment_orders
    import capo_batch.types.integer
    import capo_batch.types.job_queue_type
    import capo_batch.types.job_state_time_limit_actions
    import capo_batch.types.jq_state
    import capo_batch.types.jq_status
    import capo_batch.types.service_environment_orders
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map


class JobQueueDetail(TypedDict, closed=True):
    job_queue_name: NotRequired["capo_batch.types.string.String"]
    """<p>The job queue name.</p>"""
    job_queue_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job queue.</p>"""
    state: NotRequired["capo_batch.types.jq_state.JQState"]
    """<p>Describes the ability of the queue to accept new jobs. If the job queue state is <code>ENABLED</code>, it can accept jobs. If the job queue state is <code>DISABLED</code>, new jobs can't be added to the queue, but jobs already in the queue can finish.</p>"""
    scheduling_policy_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the scheduling policy. The format is <code>aws:<i>Partition</i>:batch:<i>Region</i>:<i>Account</i>:scheduling-policy/<i>Name</i> </code>. For example, <code>aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy</code>.</p>"""
    status: NotRequired["capo_batch.types.jq_status.JQStatus"]
    """<p>The status of the job queue (for example, <code>CREATING</code> or <code>VALID</code>).</p>"""
    status_reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short, human-readable string to provide additional details for the current status of the job queue.</p>"""
    priority: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The priority of the job queue. Job queue priority determines the order that job queues are evaluated when multiple queues dispatch jobs within a shared compute environment. A higher value for <code>priority</code> indicates a higher priority. Queues are evaluated in cycles, in descending order by priority. For example, a job queue with a priority value of <code>10</code> is evaluated before a queue with a priority value of <code>1</code>. All of the compute environments must be either Amazon EC2 (<code>EC2</code> or <code>SPOT</code>) or Fargate (<code>FARGATE</code> or <code>FARGATE_SPOT</code>). Amazon EC2 and Fargate compute environments can't be mixed.</p> <note> <p>Job queue priority doesn't guarantee that a particular job executes before a job in a lower priority queue. Jobs added to higher priority queues during the queue evaluation cycle might not be evaluated until the next cycle. A job is dispatched from a queue only if resources are available when the queue is evaluated. If there are insufficient resources available at that time, the cycle proceeds to the next queue. This means that jobs added to higher priority queues might have to wait for jobs in multiple lower priority queues to complete before they are dispatched. You can use job dependencies to control the order for jobs from queues with different priorities. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/job_dependencies.html">Job Dependencies</a> in the <i>Batch User Guide</i>.</p> </note>"""
    compute_environment_order: NotRequired[
        "capo_batch.types.compute_environment_orders.ComputeEnvironmentOrders"
    ]
    """<p>The compute environments that are attached to the job queue and the order that job placement is preferred. Compute environments are selected for job placement in ascending order.</p>"""
    service_environment_order: NotRequired[
        "capo_batch.types.service_environment_orders.ServiceEnvironmentOrders"
    ]
    """<p>The order of the service environment associated with the job queue. Job queues with a higher priority are evaluated first when associated with the same service environment.</p>"""
    job_queue_type: NotRequired["capo_batch.types.job_queue_type.JobQueueType"]
    """<p>The type of job queue. For service jobs that run on SageMaker Training, this value is <code>SAGEMAKER_TRAINING</code>. For regular container jobs, this value is <code>EKS</code>, <code>ECS</code>, or <code>ECS_FARGATE</code> depending on the compute environment.</p>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that are applied to the job queue. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging your Batch resources</a> in <i>Batch User Guide</i>.</p>"""
    job_state_time_limit_actions: NotRequired[
        "capo_batch.types.job_state_time_limit_actions.JobStateTimeLimitActions"
    ]
    """<p>The set of actions that Batch perform on jobs that remain at the head of the job queue in the specified state longer than specified times. Batch will perform each action after <code>maxTimeSeconds</code> has passed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobQueueDetail) -> dict:
    out: dict = {}
    if "job_queue_name" in value:
        out["jobQueueName"] = value["job_queue_name"]
    if "job_queue_arn" in value:
        out["jobQueueArn"] = value["job_queue_arn"]
    if "state" in value:
        import capo_batch.types.jq_state

        out["state"] = capo_batch.types.jq_state.serialize_json(value["state"])
    if "scheduling_policy_arn" in value:
        out["schedulingPolicyArn"] = value["scheduling_policy_arn"]
    if "status" in value:
        import capo_batch.types.jq_status

        out["status"] = capo_batch.types.jq_status.serialize_json(value["status"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "compute_environment_order" in value:
        import capo_batch.types.compute_environment_orders

        out["computeEnvironmentOrder"] = (
            capo_batch.types.compute_environment_orders.serialize_json(
                value["compute_environment_order"]
            )
        )
    if "service_environment_order" in value:
        import capo_batch.types.service_environment_orders

        out["serviceEnvironmentOrder"] = (
            capo_batch.types.service_environment_orders.serialize_json(
                value["service_environment_order"]
            )
        )
    if "job_queue_type" in value:
        import capo_batch.types.job_queue_type

        out["jobQueueType"] = capo_batch.types.job_queue_type.serialize_json(
            value["job_queue_type"]
        )
    if "tags" in value:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.serialize_json(value["tags"])
    if "job_state_time_limit_actions" in value:
        import capo_batch.types.job_state_time_limit_actions

        out["jobStateTimeLimitActions"] = (
            capo_batch.types.job_state_time_limit_actions.serialize_json(
                value["job_state_time_limit_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobQueueDetail:
    out: JobQueueDetail = {}  # type: ignore[typeddict-item]
    if data.get("jobQueueName") is not None:
        out["job_queue_name"] = data["jobQueueName"]
    if data.get("jobQueueArn") is not None:
        out["job_queue_arn"] = data["jobQueueArn"]
    if data.get("state") is not None:
        import capo_batch.types.jq_state

        out["state"] = capo_batch.types.jq_state.deserialize_json(data["state"])
    if data.get("schedulingPolicyArn") is not None:
        out["scheduling_policy_arn"] = data["schedulingPolicyArn"]
    if data.get("status") is not None:
        import capo_batch.types.jq_status

        out["status"] = capo_batch.types.jq_status.deserialize_json(data["status"])
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("computeEnvironmentOrder") is not None:
        import capo_batch.types.compute_environment_orders

        out["compute_environment_order"] = (
            capo_batch.types.compute_environment_orders.deserialize_json(
                data["computeEnvironmentOrder"]
            )
        )
    if data.get("serviceEnvironmentOrder") is not None:
        import capo_batch.types.service_environment_orders

        out["service_environment_order"] = (
            capo_batch.types.service_environment_orders.deserialize_json(
                data["serviceEnvironmentOrder"]
            )
        )
    if data.get("jobQueueType") is not None:
        import capo_batch.types.job_queue_type

        out["job_queue_type"] = capo_batch.types.job_queue_type.deserialize_json(
            data["jobQueueType"]
        )
    if data.get("tags") is not None:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    if data.get("jobStateTimeLimitActions") is not None:
        import capo_batch.types.job_state_time_limit_actions

        out["job_state_time_limit_actions"] = (
            capo_batch.types.job_state_time_limit_actions.deserialize_json(
                data["jobStateTimeLimitActions"]
            )
        )
    return out
