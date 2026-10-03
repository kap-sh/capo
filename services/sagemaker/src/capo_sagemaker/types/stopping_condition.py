"""Generated from Smithy shape ``com.amazonaws.sagemaker#StoppingCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_pending_time_in_seconds
    import capo_sagemaker.types.max_runtime_in_seconds
    import capo_sagemaker.types.max_wait_time_in_seconds


class StoppingCondition(TypedDict, closed=True):
    max_runtime_in_seconds: NotRequired[
        "capo_sagemaker.types.max_runtime_in_seconds.MaxRuntimeInSeconds"
    ]
    """<p>The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.</p> <p>For compilation jobs, if the job does not complete during this time, a <code>TimeOut</code> error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.</p> <p>For all other jobs, if the job does not complete during this time, SageMaker ends the job. When <code>RetryStrategy</code> is specified in the job request, <code>MaxRuntimeInSeconds</code> specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.</p> <p>The maximum time that a <code>TrainingJob</code> can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.</p>"""
    max_wait_time_in_seconds: NotRequired[
        "capo_sagemaker.types.max_wait_time_in_seconds.MaxWaitTimeInSeconds"
    ]
    """<p>The maximum length of time, in seconds, that a managed Spot training job has to complete. It is the amount of time spent waiting for Spot capacity plus the amount of time the job can run. It must be equal to or greater than <code>MaxRuntimeInSeconds</code>. If the job does not complete during this time, SageMaker ends the job.</p> <p>When <code>RetryStrategy</code> is specified in the job request, <code>MaxWaitTimeInSeconds</code> specifies the maximum time for all of the attempts in total, not each individual attempt.</p>"""
    max_pending_time_in_seconds: NotRequired[
        "capo_sagemaker.types.max_pending_time_in_seconds.MaxPendingTimeInSeconds"
    ]
    """<p>The maximum length of time, in seconds, that a training or compilation job can be pending before it is stopped.</p> <note> <p>When working with training jobs that use capacity from <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html">training plans</a>, not all <code>Pending</code> job states count against the <code>MaxPendingTimeInSeconds</code> limit. The following scenarios do not increment the <code>MaxPendingTimeInSeconds</code> counter:</p> <ul> <li> <p>The plan is in a <code>Scheduled</code> state: Jobs queued (in <code>Pending</code> status) before a plan's start date (waiting for scheduled start time)</p> </li> <li> <p>Between capacity reservations: Jobs temporarily back to <code>Pending</code> status between two capacity reservation periods</p> </li> </ul> <p> <code>MaxPendingTimeInSeconds</code> only increments when jobs are actively waiting for capacity in an <code>Active</code> plan.</p> </note> <note> <ul> <li> <p> <code>MaxPendingTimeInSeconds</code> takes effect only for jobs that request accelerated computing instance types, such as instances in the <code>ml.p</code>, <code>ml.g</code>, and <code>ml.trn</code> families. It has no effect on jobs that request CPU-only instance types.</p> </li> <li> <p>If the job specifies <code>InstancePreferences</code>, <code>MaxPendingTimeInSeconds</code> bounds the total time SageMaker spends working through your list of instance types. It is not applied per instance type preference, and takes effect only when the list includes at least one accelerated computing instance type.</p> </li> </ul> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StoppingCondition) -> dict:
    out: dict = {}
    if "max_runtime_in_seconds" in value:
        out["MaxRuntimeInSeconds"] = value["max_runtime_in_seconds"]
    if "max_wait_time_in_seconds" in value:
        out["MaxWaitTimeInSeconds"] = value["max_wait_time_in_seconds"]
    if "max_pending_time_in_seconds" in value:
        out["MaxPendingTimeInSeconds"] = value["max_pending_time_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StoppingCondition:
    out: StoppingCondition = {}  # type: ignore[typeddict-item]
    if data.get("MaxRuntimeInSeconds") is not None:
        out["max_runtime_in_seconds"] = data["MaxRuntimeInSeconds"]
    if data.get("MaxWaitTimeInSeconds") is not None:
        out["max_wait_time_in_seconds"] = data["MaxWaitTimeInSeconds"]
    if data.get("MaxPendingTimeInSeconds") is not None:
        out["max_pending_time_in_seconds"] = data["MaxPendingTimeInSeconds"]
    return out
