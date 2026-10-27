"""Generated from Smithy shape ``com.amazonaws.deadline#WeightedBalancedSchedulingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.scheduling_error_weight
    import capo_deadline.types.scheduling_max_priority_override
    import capo_deadline.types.scheduling_min_priority_override
    import capo_deadline.types.scheduling_priority_weight
    import capo_deadline.types.scheduling_rendering_task_buffer
    import capo_deadline.types.scheduling_rendering_task_weight
    import capo_deadline.types.scheduling_submission_time_weight


class WeightedBalancedSchedulingConfiguration(TypedDict, closed=True):
    priority_weight: (
        "capo_deadline.types.scheduling_priority_weight.SchedulingPriorityWeight"
    )
    """The weight applied to job priority in the scheduling formula. Higher values give more influence to job priority. A value of <code>0</code> means priority is ignored. The default value is <code>100.0</code>."""
    error_weight: "capo_deadline.types.scheduling_error_weight.SchedulingErrorWeight"
    """The weight applied to the number of errors on a job. A negative value means jobs without errors are scheduled first. A value of <code>0</code> means errors are ignored. The default value is <code>-10.0</code>."""
    submission_time_weight: "capo_deadline.types.scheduling_submission_time_weight.SchedulingSubmissionTimeWeight"
    """The weight applied to job submission time. A positive value means earlier jobs are scheduled first. A value of <code>0</code> means submission time is ignored. The default value is <code>3.0</code>."""
    rendering_task_weight: "capo_deadline.types.scheduling_rendering_task_weight.SchedulingRenderingTaskWeight"
    """The weight applied to the number of tasks currently rendering on a job. A negative value means jobs that are not already rendering are scheduled next. A value of <code>0</code> means the rendering state is ignored. The default value is <code>-100.0</code>."""
    rendering_task_buffer: "capo_deadline.types.scheduling_rendering_task_buffer.SchedulingRenderingTaskBuffer"
    """The rendering task buffer is subtracted from the number of rendering tasks before applying the rendering task weight. This creates a stickiness effect where workers prefer to stay with their current job. Higher values make workers stickier. The default value is <code>1</code>. The buffer is only applied in the weight calculation for a job if the worker is currently assigned to that job."""
    max_priority_override: NotRequired[
        "capo_deadline.types.scheduling_max_priority_override.SchedulingMaxPriorityOverride"
    ]
    """Overrides the weighted scheduling formula for jobs at the maximum priority (100). When set, jobs with priority 100 are always scheduled first regardless of their calculated weight. When absent, maximum priority jobs use the standard weighted formula."""
    min_priority_override: NotRequired[
        "capo_deadline.types.scheduling_min_priority_override.SchedulingMinPriorityOverride"
    ]
    """Overrides the weighted scheduling formula for jobs at the minimum priority (0). When set, jobs with priority 0 are always scheduled last regardless of their calculated weight. When absent, minimum priority jobs use the standard weighted formula."""


# --- restJson1 ser/de ---
def serialize_json(value: WeightedBalancedSchedulingConfiguration) -> dict:
    out: dict = {}
    out["priorityWeight"] = (
        "NaN"
        if value.get("priority_weight", 100.0) != value.get("priority_weight", 100.0)
        else "Infinity"
        if value.get("priority_weight", 100.0) == float("inf")
        else "-Infinity"
        if value.get("priority_weight", 100.0) == float("-inf")
        else value.get("priority_weight", 100.0)
    )
    out["errorWeight"] = (
        "NaN"
        if value.get("error_weight", -10.0) != value.get("error_weight", -10.0)
        else "Infinity"
        if value.get("error_weight", -10.0) == float("inf")
        else "-Infinity"
        if value.get("error_weight", -10.0) == float("-inf")
        else value.get("error_weight", -10.0)
    )
    out["submissionTimeWeight"] = (
        "NaN"
        if value.get("submission_time_weight", 3.0)
        != value.get("submission_time_weight", 3.0)
        else "Infinity"
        if value.get("submission_time_weight", 3.0) == float("inf")
        else "-Infinity"
        if value.get("submission_time_weight", 3.0) == float("-inf")
        else value.get("submission_time_weight", 3.0)
    )
    out["renderingTaskWeight"] = (
        "NaN"
        if value.get("rendering_task_weight", -100.0)
        != value.get("rendering_task_weight", -100.0)
        else "Infinity"
        if value.get("rendering_task_weight", -100.0) == float("inf")
        else "-Infinity"
        if value.get("rendering_task_weight", -100.0) == float("-inf")
        else value.get("rendering_task_weight", -100.0)
    )
    out["renderingTaskBuffer"] = value.get("rendering_task_buffer", 1)
    if "max_priority_override" in value:
        import capo_deadline.types.scheduling_max_priority_override

        out["maxPriorityOverride"] = (
            capo_deadline.types.scheduling_max_priority_override.serialize_json(
                value["max_priority_override"]
            )
        )
    if "min_priority_override" in value:
        import capo_deadline.types.scheduling_min_priority_override

        out["minPriorityOverride"] = (
            capo_deadline.types.scheduling_min_priority_override.serialize_json(
                value["min_priority_override"]
            )
        )
    return out


def deserialize_json(data: dict) -> WeightedBalancedSchedulingConfiguration:
    out: WeightedBalancedSchedulingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("priorityWeight") is not None:
        out["priority_weight"] = float(data["priorityWeight"])
    else:
        out["priority_weight"] = 100.0
    if data.get("errorWeight") is not None:
        out["error_weight"] = float(data["errorWeight"])
    else:
        out["error_weight"] = -10.0
    if data.get("submissionTimeWeight") is not None:
        out["submission_time_weight"] = float(data["submissionTimeWeight"])
    else:
        out["submission_time_weight"] = 3.0
    if data.get("renderingTaskWeight") is not None:
        out["rendering_task_weight"] = float(data["renderingTaskWeight"])
    else:
        out["rendering_task_weight"] = -100.0
    if data.get("renderingTaskBuffer") is not None:
        out["rendering_task_buffer"] = data["renderingTaskBuffer"]
    else:
        out["rendering_task_buffer"] = 1
    if data.get("maxPriorityOverride") is not None:
        import capo_deadline.types.scheduling_max_priority_override

        out["max_priority_override"] = (
            capo_deadline.types.scheduling_max_priority_override.deserialize_json(
                data["maxPriorityOverride"]
            )
        )
    if data.get("minPriorityOverride") is not None:
        import capo_deadline.types.scheduling_min_priority_override

        out["min_priority_override"] = (
            capo_deadline.types.scheduling_min_priority_override.deserialize_json(
                data["minPriorityOverride"]
            )
        )
    return out
