"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeRetrainingSchedulerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.lookback_window
    import capo_lookoutequipment.types.model_arn
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.model_promote_mode
    import capo_lookoutequipment.types.retraining_frequency
    import capo_lookoutequipment.types.retraining_scheduler_status
    import capo_lookoutequipment.types.timestamp


class DescribeRetrainingSchedulerResponse(TypedDict, closed=True):
    model_name: NotRequired["capo_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the model that the retraining scheduler is attached to. </p>"""
    model_arn: NotRequired["capo_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The ARN of the model that the retraining scheduler is attached to. </p>"""
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
    status: NotRequired[
        "capo_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
    ]
    """<p>The status of the retraining scheduler. </p>"""
    promote_mode: NotRequired[
        "capo_lookoutequipment.types.model_promote_mode.ModelPromoteMode"
    ]
    """<p>Indicates how the service uses new models. In <code>MANAGED</code> mode, new models are used for inference if they have better performance than the current model. In <code>MANUAL</code> mode, the new models are not used until they are <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/versioning-model.html#model-activation">manually activated</a>.</p>"""
    created_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the time and date at which the retraining scheduler was created. </p>"""
    updated_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the time and date at which the retraining scheduler was updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRetrainingSchedulerResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
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
    if "status" in value:
        import capo_lookoutequipment.types.retraining_scheduler_status

        out["Status"] = (
            capo_lookoutequipment.types.retraining_scheduler_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "promote_mode" in value:
        import capo_lookoutequipment.types.model_promote_mode

        out["PromoteMode"] = (
            capo_lookoutequipment.types.model_promote_mode.serialize_aws_json_1_0(
                value["promote_mode"]
            )
        )
    if "created_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreatedAt"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["UpdatedAt"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRetrainingSchedulerResponse:
    out: DescribeRetrainingSchedulerResponse = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
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
    if data.get("Status") is not None:
        import capo_lookoutequipment.types.retraining_scheduler_status

        out["status"] = (
            capo_lookoutequipment.types.retraining_scheduler_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("PromoteMode") is not None:
        import capo_lookoutequipment.types.model_promote_mode

        out["promote_mode"] = (
            capo_lookoutequipment.types.model_promote_mode.deserialize_aws_json_1_0(
                data["PromoteMode"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_lookoutequipment.types.timestamp

        out["created_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_lookoutequipment.types.timestamp

        out["updated_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    return out
