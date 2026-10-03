"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#RetrainingSchedulerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.lookback_window
    import capo_lookoutequipment.types.model_arn
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.retraining_frequency
    import capo_lookoutequipment.types.retraining_scheduler_status
    import capo_lookoutequipment.types.timestamp


class RetrainingSchedulerSummary(TypedDict, closed=True):
    model_name: NotRequired["capo_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the model that the retraining scheduler is attached to. </p>"""
    model_arn: NotRequired["capo_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The ARN of the model that the retraining scheduler is attached to. </p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
    ]
    """<p>The status of the retraining scheduler. </p>"""
    retraining_start_date: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the nearest UTC day.</p>"""
    retraining_frequency: NotRequired[
        "capo_lookoutequipment.types.retraining_frequency.RetrainingFrequency"
    ]
    """<p>The frequency at which the model retraining is set. This follows the <a href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601</a> guidelines.</p>"""
    lookback_window: NotRequired[
        "capo_lookoutequipment.types.lookback_window.LookbackWindow"
    ]
    """<p>The number of past days of data used for retraining.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RetrainingSchedulerSummary) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "status" in value:
        import capo_lookoutequipment.types.retraining_scheduler_status

        out["Status"] = (
            capo_lookoutequipment.types.retraining_scheduler_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "retraining_start_date" in value:
        import capo_lookoutequipment.types.timestamp

        out["RetrainingStartDate"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["retraining_start_date"]
            )
        )
    if "retraining_frequency" in value:
        out["RetrainingFrequency"] = value["retraining_frequency"]
    if "lookback_window" in value:
        out["LookbackWindow"] = value["lookback_window"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RetrainingSchedulerSummary:
    out: RetrainingSchedulerSummary = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("Status") is not None:
        import capo_lookoutequipment.types.retraining_scheduler_status

        out["status"] = (
            capo_lookoutequipment.types.retraining_scheduler_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("RetrainingStartDate") is not None:
        import capo_lookoutequipment.types.timestamp

        out["retraining_start_date"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["RetrainingStartDate"]
            )
        )
    if data.get("RetrainingFrequency") is not None:
        out["retraining_frequency"] = data["RetrainingFrequency"]
    if data.get("LookbackWindow") is not None:
        out["lookback_window"] = data["LookbackWindow"]
    return out
