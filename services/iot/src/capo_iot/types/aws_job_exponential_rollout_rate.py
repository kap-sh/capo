"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobExponentialRolloutRate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_job_rate_increase_criteria
    import capo_iot.types.aws_job_rollout_increment_factor
    import capo_iot.types.aws_job_rollout_rate_per_minute


class AwsJobExponentialRolloutRate(TypedDict, closed=True):
    base_rate_per_minute: (
        "capo_iot.types.aws_job_rollout_rate_per_minute.AwsJobRolloutRatePerMinute"
    )
    """<p>The minimum number of things that will be notified of a pending job, per minute, at the start of the job rollout. This is the initial rate of the rollout.</p>"""
    increment_factor: (
        "capo_iot.types.aws_job_rollout_increment_factor.AwsJobRolloutIncrementFactor"
    )
    """<p>The rate of increase for a job rollout. The number of things notified is multiplied by this factor.</p>"""
    rate_increase_criteria: (
        "capo_iot.types.aws_job_rate_increase_criteria.AwsJobRateIncreaseCriteria"
    )
    """<p>The criteria to initiate the increase in rate of rollout for a job.</p> <p>Amazon Web Services IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobExponentialRolloutRate) -> dict:
    out: dict = {}
    out["baseRatePerMinute"] = value["base_rate_per_minute"]
    out["incrementFactor"] = (
        "NaN"
        if value.get("increment_factor", 0) != value.get("increment_factor", 0)
        else "Infinity"
        if value.get("increment_factor", 0) == float("inf")
        else "-Infinity"
        if value.get("increment_factor", 0) == float("-inf")
        else value.get("increment_factor", 0)
    )
    import capo_iot.types.aws_job_rate_increase_criteria

    out["rateIncreaseCriteria"] = (
        capo_iot.types.aws_job_rate_increase_criteria.serialize_json(
            value["rate_increase_criteria"]
        )
    )
    return out


def deserialize_json(data: dict) -> AwsJobExponentialRolloutRate:
    out: AwsJobExponentialRolloutRate = {}  # type: ignore[typeddict-item]
    if data.get("baseRatePerMinute") is not None:
        out["base_rate_per_minute"] = data["baseRatePerMinute"]
    else:
        out["base_rate_per_minute"] = 0
    if data.get("incrementFactor") is not None:
        out["increment_factor"] = float(data["incrementFactor"])
    else:
        out["increment_factor"] = 0
    if data.get("rateIncreaseCriteria") is not None:
        import capo_iot.types.aws_job_rate_increase_criteria

        out["rate_increase_criteria"] = (
            capo_iot.types.aws_job_rate_increase_criteria.deserialize_json(
                data["rateIncreaseCriteria"]
            )
        )
    else:
        raise DeserializationError(
            "AwsJobExponentialRolloutRate.rate_increase_criteria required"
        )
    return out
