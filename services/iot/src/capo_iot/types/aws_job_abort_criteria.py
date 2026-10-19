"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobAbortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_job_abort_criteria_abort_action
    import capo_iot.types.aws_job_abort_criteria_abort_threshold_percentage
    import capo_iot.types.aws_job_abort_criteria_failure_type
    import capo_iot.types.aws_job_abort_criteria_minimum_number_of_executed_things


class AwsJobAbortCriteria(TypedDict, closed=True):
    failure_type: "capo_iot.types.aws_job_abort_criteria_failure_type.AwsJobAbortCriteriaFailureType"
    """<p>The type of job execution failures that can initiate a job abort.</p>"""
    action: "capo_iot.types.aws_job_abort_criteria_abort_action.AwsJobAbortCriteriaAbortAction"
    """<p>The type of job action to take to initiate the job abort.</p>"""
    threshold_percentage: "capo_iot.types.aws_job_abort_criteria_abort_threshold_percentage.AwsJobAbortCriteriaAbortThresholdPercentage"
    """<p>The minimum percentage of job execution failures that must occur to initiate the job abort.</p> <p>Amazon Web Services IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).</p>"""
    min_number_of_executed_things: "capo_iot.types.aws_job_abort_criteria_minimum_number_of_executed_things.AwsJobAbortCriteriaMinimumNumberOfExecutedThings"
    """<p>The minimum number of things which must receive job execution notifications before the job can be aborted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobAbortCriteria) -> dict:
    out: dict = {}
    import capo_iot.types.aws_job_abort_criteria_failure_type

    out["failureType"] = (
        capo_iot.types.aws_job_abort_criteria_failure_type.serialize_json(
            value["failure_type"]
        )
    )
    import capo_iot.types.aws_job_abort_criteria_abort_action

    out["action"] = capo_iot.types.aws_job_abort_criteria_abort_action.serialize_json(
        value["action"]
    )
    out["thresholdPercentage"] = (
        "NaN"
        if value["threshold_percentage"] != value["threshold_percentage"]
        else "Infinity"
        if value["threshold_percentage"] == float("inf")
        else "-Infinity"
        if value["threshold_percentage"] == float("-inf")
        else value["threshold_percentage"]
    )
    out["minNumberOfExecutedThings"] = value["min_number_of_executed_things"]
    return out


def deserialize_json(data: dict) -> AwsJobAbortCriteria:
    out: AwsJobAbortCriteria = {}  # type: ignore[typeddict-item]
    if data.get("failureType") is not None:
        import capo_iot.types.aws_job_abort_criteria_failure_type

        out["failure_type"] = (
            capo_iot.types.aws_job_abort_criteria_failure_type.deserialize_json(
                data["failureType"]
            )
        )
    else:
        import typing

        out["failure_type"] = typing.cast(
            "capo_iot.types.aws_job_abort_criteria_failure_type.AwsJobAbortCriteriaFailureType",
            "",
        )
    if data.get("action") is not None:
        import capo_iot.types.aws_job_abort_criteria_abort_action

        out["action"] = (
            capo_iot.types.aws_job_abort_criteria_abort_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_iot.types.aws_job_abort_criteria_abort_action.AwsJobAbortCriteriaAbortAction",
            "",
        )
    if data.get("thresholdPercentage") is not None:
        out["threshold_percentage"] = float(data["thresholdPercentage"])
    else:
        out["threshold_percentage"] = 0.0
    if data.get("minNumberOfExecutedThings") is not None:
        out["min_number_of_executed_things"] = data["minNumberOfExecutedThings"]
    else:
        out["min_number_of_executed_things"] = 0
    return out
