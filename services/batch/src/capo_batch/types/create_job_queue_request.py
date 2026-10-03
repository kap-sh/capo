"""Generated from Smithy shape ``com.amazonaws.batch#CreateJobQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.compute_environment_orders
    import capo_batch.types.integer
    import capo_batch.types.job_queue_type
    import capo_batch.types.job_state_time_limit_actions
    import capo_batch.types.jq_state
    import capo_batch.types.service_environment_orders
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map


class CreateJobQueueRequest(TypedDict, closed=True):
    job_queue_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the job queue. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    state: NotRequired["capo_batch.types.jq_state.JQState"]
    """<p>The state of the job queue. If the job queue state is <code>ENABLED</code>, it is able to accept jobs. If the job queue state is <code>DISABLED</code>, new jobs can't be added to the queue, but jobs already in the queue can finish.</p>"""
    scheduling_policy_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the fair-share scheduling policy. Job queues that don't have a fair-share scheduling policy are scheduled in a first-in, first-out (FIFO) model. After a job queue has a fair-share scheduling policy, it can be replaced but can't be removed.</p> <p>The format is <code>aws:<i>Partition</i>:batch:<i>Region</i>:<i>Account</i>:scheduling-policy/<i>Name</i> </code>.</p> <p>An example is <code>aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy</code>.</p> <p>A job queue without a fair-share scheduling policy is scheduled as a FIFO job queue and can't have a fair-share scheduling policy added. Jobs queues with a fair-share scheduling policy can have a maximum of 500 active share identifiers. When the limit has been reached, submissions of any jobs that add a new share identifier fail.</p>"""
    priority: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The priority of the job queue. Job queues with a higher priority (or a higher integer value for the <code>priority</code> parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of <code>10</code> is given scheduling preference over a job queue with a priority value of <code>1</code>. All of the compute environments must be either EC2 (<code>EC2</code> or <code>SPOT</code>) or Fargate (<code>FARGATE</code> or <code>FARGATE_SPOT</code>); EC2 and Fargate compute environments can't be mixed.</p>"""
    compute_environment_order: NotRequired[
        "capo_batch.types.compute_environment_orders.ComputeEnvironmentOrders"
    ]
    """<p>The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the <code>VALID</code> state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 (<code>EC2</code> or <code>SPOT</code>) or Fargate (<code>FARGATE</code> or <code>FARGATE_SPOT</code>); EC2 and Fargate compute environments can't be mixed.</p> <note> <p>All compute environments that are associated with a job queue must share the same architecture. Batch doesn't support mixing compute environment architecture types in a single job queue.</p> </note>"""
    service_environment_order: NotRequired[
        "capo_batch.types.service_environment_orders.ServiceEnvironmentOrders"
    ]
    """<p>A list of service environments that this job queue can use to allocate jobs. All serviceEnvironments must have the same type. A job queue can't have both a serviceEnvironmentOrder and a computeEnvironmentOrder field.</p>"""
    job_queue_type: NotRequired["capo_batch.types.job_queue_type.JobQueueType"]
    """<p>The type of job queue. For service jobs that run on SageMaker Training, this value is <code>SAGEMAKER_TRAINING</code>. For regular container jobs, this value is <code>EKS</code>, <code>ECS</code>, or <code>ECS_FARGATE</code> depending on the compute environment.</p>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that you apply to the job queue to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging your Batch resources</a> in <i>Batch User Guide</i>.</p>"""
    job_state_time_limit_actions: NotRequired[
        "capo_batch.types.job_state_time_limit_actions.JobStateTimeLimitActions"
    ]
    """<p>The set of actions that Batch performs on jobs that remain at the head of the job queue in the specified state longer than specified times. Batch will perform each action after <code>maxTimeSeconds</code> has passed. (<b>Note</b>: The minimum value for maxTimeSeconds is 600 (10 minutes) and its maximum value is 86,400 (24 hours).)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobQueueRequest) -> dict:
    out: dict = {}
    if "job_queue_name" in value:
        out["jobQueueName"] = value["job_queue_name"]
    if "state" in value:
        import capo_batch.types.jq_state

        out["state"] = capo_batch.types.jq_state.serialize_json(value["state"])
    if "scheduling_policy_arn" in value:
        out["schedulingPolicyArn"] = value["scheduling_policy_arn"]
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


def deserialize_json(data: dict) -> CreateJobQueueRequest:
    out: CreateJobQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobQueueName") is not None:
        out["job_queue_name"] = data["jobQueueName"]
    if data.get("state") is not None:
        import capo_batch.types.jq_state

        out["state"] = capo_batch.types.jq_state.deserialize_json(data["state"])
    if data.get("schedulingPolicyArn") is not None:
        out["scheduling_policy_arn"] = data["schedulingPolicyArn"]
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
