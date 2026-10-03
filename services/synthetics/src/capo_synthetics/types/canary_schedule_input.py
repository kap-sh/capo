"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryScheduleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_synthetics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_synthetics.types.max_one_year_in_seconds
    import capo_synthetics.types.retry_config_input
    import capo_synthetics.types.string


class CanaryScheduleInput(TypedDict, closed=True):
    expression: "capo_synthetics.types.string.String"
    """<p>A <code>rate</code> expression or a <code>cron</code> expression that defines how often the canary is to run.</p> <p>For a rate expression, The syntax is <code>rate(<i>number unit</i>)</code>. <i>unit</i> can be <code>minute</code>, <code>minutes</code>, or <code>hour</code>. </p> <p>For example, <code>rate(1 minute)</code> runs the canary once a minute, <code>rate(10 minutes)</code> runs it once every 10 minutes, and <code>rate(1 hour)</code> runs it once every hour. You can specify a frequency between <code>rate(1 minute)</code> and <code>rate(1 hour)</code>.</p> <p>Specifying <code>rate(0 minute)</code> or <code>rate(0 hour)</code> is a special value that causes the canary to run only once when it is started.</p> <p>Use <code>cron(<i>expression</i>)</code> to specify a cron expression. You can't schedule a canary to wait for more than a year before running. For information about the syntax for cron expressions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html"> Scheduling canary runs using cron</a>.</p>"""
    duration_in_seconds: NotRequired[
        "capo_synthetics.types.max_one_year_in_seconds.MaxOneYearInSeconds"
    ]
    """<p>How long, in seconds, for the canary to continue making regular runs according to the schedule in the <code>Expression</code> value. If you specify 0, the canary continues making runs until you stop it. If you omit this field, the default of 0 is used.</p>"""
    retry_config: NotRequired[
        "capo_synthetics.types.retry_config_input.RetryConfigInput"
    ]
    """<p>A structure that contains the retry configuration for a canary</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryScheduleInput) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    if "retry_config" in value:
        import capo_synthetics.types.retry_config_input

        out["RetryConfig"] = capo_synthetics.types.retry_config_input.serialize_json(
            value["retry_config"]
        )
    return out


def deserialize_json(data: dict) -> CanaryScheduleInput:
    out: CanaryScheduleInput = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("CanaryScheduleInput.expression required")
    if data.get("DurationInSeconds") is not None:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    if data.get("RetryConfig") is not None:
        import capo_synthetics.types.retry_config_input

        out["retry_config"] = capo_synthetics.types.retry_config_input.deserialize_json(
            data["RetryConfig"]
        )
    return out
