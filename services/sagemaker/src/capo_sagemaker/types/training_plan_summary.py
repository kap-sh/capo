"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.available_instance_count
    import capo_sagemaker.types.currency_code
    import capo_sagemaker.types.in_use_instance_count
    import capo_sagemaker.types.reserved_capacity_summaries
    import capo_sagemaker.types.sage_maker_resource_names
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.total_instance_count
    import capo_sagemaker.types.training_plan_arn
    import capo_sagemaker.types.training_plan_duration_hours
    import capo_sagemaker.types.training_plan_duration_minutes
    import capo_sagemaker.types.training_plan_name
    import capo_sagemaker.types.training_plan_status
    import capo_sagemaker.types.training_plan_status_message
    import capo_sagemaker.types.ultra_server_count


class TrainingPlanSummary(TypedDict, closed=True):
    training_plan_arn: NotRequired[
        "capo_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the training plan.</p>"""
    training_plan_name: NotRequired[
        "capo_sagemaker.types.training_plan_name.TrainingPlanName"
    ]
    """<p>The name of the training plan.</p>"""
    status: NotRequired["capo_sagemaker.types.training_plan_status.TrainingPlanStatus"]
    """<p>The current status of the training plan (e.g., Pending, Active, Expired). To see the complete list of status values available for a training plan, refer to the <code>Status</code> attribute within the <code> <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingPlanSummary.html">TrainingPlanSummary</a> </code> object.</p>"""
    status_message: NotRequired[
        "capo_sagemaker.types.training_plan_status_message.TrainingPlanStatusMessage"
    ]
    """<p>A message providing additional information about the current status of the training plan.</p>"""
    duration_hours: NotRequired[
        "capo_sagemaker.types.training_plan_duration_hours.TrainingPlanDurationHours"
    ]
    """<p>The number of whole hours in the total duration for this training plan.</p>"""
    duration_minutes: NotRequired[
        "capo_sagemaker.types.training_plan_duration_minutes.TrainingPlanDurationMinutes"
    ]
    """<p>The additional minutes beyond whole hours in the total duration for this training plan.</p>"""
    start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The start time of the training plan.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The end time of the training plan.</p>"""
    upfront_fee: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The upfront fee for the training plan.</p>"""
    currency_code: NotRequired["capo_sagemaker.types.currency_code.CurrencyCode"]
    """<p>The currency code for the upfront fee (e.g., USD).</p>"""
    total_instance_count: NotRequired[
        "capo_sagemaker.types.total_instance_count.TotalInstanceCount"
    ]
    """<p>The total number of instances reserved in this training plan.</p>"""
    available_instance_count: NotRequired[
        "capo_sagemaker.types.available_instance_count.AvailableInstanceCount"
    ]
    """<p>The number of instances currently available for use in this training plan.</p>"""
    in_use_instance_count: NotRequired[
        "capo_sagemaker.types.in_use_instance_count.InUseInstanceCount"
    ]
    """<p>The number of instances currently in use from this training plan.</p>"""
    total_ultra_server_count: NotRequired[
        "capo_sagemaker.types.ultra_server_count.UltraServerCount"
    ]
    """<p>The total number of UltraServers allocated to this training plan.</p>"""
    target_resources: NotRequired[
        "capo_sagemaker.types.sage_maker_resource_names.SageMakerResourceNames"
    ]
    """<p>The target resources (e.g., training jobs, HyperPod clusters, Endpoints, Studio apps) that can use this training plan.</p> <p>Training plans are specific to their target resource.</p> <ul> <li> <p>A training plan designed for SageMaker training jobs can only be used to schedule and run training jobs.</p> </li> <li> <p>A training plan for HyperPod clusters can be used exclusively to provide compute resources to a cluster's instance group.</p> </li> <li> <p>A training plan for SageMaker endpoints can be used exclusively to provide compute resources to SageMaker endpoints for model deployment.</p> </li> <li> <p>A training plan for Studio apps can be used to launch JupyterLab and Code Editor apps on reserved training plan capacity.</p> </li> </ul>"""
    reserved_capacity_summaries: NotRequired[
        "capo_sagemaker.types.reserved_capacity_summaries.ReservedCapacitySummaries"
    ]
    """<p>A list of reserved capacities associated with this training plan, including details such as instance types, counts, and availability zones.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanSummary) -> dict:
    out: dict = {}
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    if "training_plan_name" in value:
        out["TrainingPlanName"] = value["training_plan_name"]
    if "status" in value:
        import capo_sagemaker.types.training_plan_status

        out["Status"] = (
            capo_sagemaker.types.training_plan_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "duration_hours" in value:
        out["DurationHours"] = value["duration_hours"]
    if "duration_minutes" in value:
        out["DurationMinutes"] = value["duration_minutes"]
    if "start_time" in value:
        import capo_sagemaker.types.timestamp

        out["StartTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "upfront_fee" in value:
        out["UpfrontFee"] = value["upfront_fee"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "total_instance_count" in value:
        out["TotalInstanceCount"] = value["total_instance_count"]
    if "available_instance_count" in value:
        out["AvailableInstanceCount"] = value["available_instance_count"]
    if "in_use_instance_count" in value:
        out["InUseInstanceCount"] = value["in_use_instance_count"]
    if "total_ultra_server_count" in value:
        out["TotalUltraServerCount"] = value["total_ultra_server_count"]
    if "target_resources" in value:
        import capo_sagemaker.types.sage_maker_resource_names

        out["TargetResources"] = (
            capo_sagemaker.types.sage_maker_resource_names.serialize_aws_json_1_1(
                value["target_resources"]
            )
        )
    if "reserved_capacity_summaries" in value:
        import capo_sagemaker.types.reserved_capacity_summaries

        out["ReservedCapacitySummaries"] = (
            capo_sagemaker.types.reserved_capacity_summaries.serialize_aws_json_1_1(
                value["reserved_capacity_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingPlanSummary:
    out: TrainingPlanSummary = {}  # type: ignore[typeddict-item]
    if data.get("TrainingPlanArn") is not None:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    if data.get("TrainingPlanName") is not None:
        out["training_plan_name"] = data["TrainingPlanName"]
    if data.get("Status") is not None:
        import capo_sagemaker.types.training_plan_status

        out["status"] = (
            capo_sagemaker.types.training_plan_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("DurationHours") is not None:
        out["duration_hours"] = data["DurationHours"]
    if data.get("DurationMinutes") is not None:
        out["duration_minutes"] = data["DurationMinutes"]
    if data.get("StartTime") is not None:
        import capo_sagemaker.types.timestamp

        out["start_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("UpfrontFee") is not None:
        out["upfront_fee"] = data["UpfrontFee"]
    if data.get("CurrencyCode") is not None:
        out["currency_code"] = data["CurrencyCode"]
    if data.get("TotalInstanceCount") is not None:
        out["total_instance_count"] = data["TotalInstanceCount"]
    if data.get("AvailableInstanceCount") is not None:
        out["available_instance_count"] = data["AvailableInstanceCount"]
    if data.get("InUseInstanceCount") is not None:
        out["in_use_instance_count"] = data["InUseInstanceCount"]
    if data.get("TotalUltraServerCount") is not None:
        out["total_ultra_server_count"] = data["TotalUltraServerCount"]
    if data.get("TargetResources") is not None:
        import capo_sagemaker.types.sage_maker_resource_names

        out["target_resources"] = (
            capo_sagemaker.types.sage_maker_resource_names.deserialize_aws_json_1_1(
                data["TargetResources"]
            )
        )
    if data.get("ReservedCapacitySummaries") is not None:
        import capo_sagemaker.types.reserved_capacity_summaries

        out["reserved_capacity_summaries"] = (
            capo_sagemaker.types.reserved_capacity_summaries.deserialize_aws_json_1_1(
                data["ReservedCapacitySummaries"]
            )
        )
    return out
