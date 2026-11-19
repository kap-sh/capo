"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelIterationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.any_length_string
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.flywheel_iteration_id
    import capo_comprehend.types.flywheel_iteration_status
    import capo_comprehend.types.flywheel_model_evaluation_metrics
    import capo_comprehend.types.s3_uri
    import capo_comprehend.types.timestamp


class FlywheelIterationProperties(TypedDict, closed=True):
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p></p>"""
    flywheel_iteration_id: NotRequired[
        "capo_comprehend.types.flywheel_iteration_id.FlywheelIterationId"
    ]
    """<p></p>"""
    creation_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The creation start time of the flywheel iteration.</p>"""
    end_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The completion time of this flywheel iteration.</p>"""
    status: NotRequired[
        "capo_comprehend.types.flywheel_iteration_status.FlywheelIterationStatus"
    ]
    """<p>The status of the flywheel iteration.</p>"""
    message: NotRequired["capo_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of the flywheel iteration.</p>"""
    evaluated_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The ARN of the evaluated model associated with this flywheel iteration.</p>"""
    evaluated_model_metrics: NotRequired[
        "capo_comprehend.types.flywheel_model_evaluation_metrics.FlywheelModelEvaluationMetrics"
    ]
    trained_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The ARN of the trained model associated with this flywheel iteration.</p>"""
    trained_model_metrics: NotRequired[
        "capo_comprehend.types.flywheel_model_evaluation_metrics.FlywheelModelEvaluationMetrics"
    ]
    """<p>The metrics associated with the trained model.</p>"""
    evaluation_manifest_s3_prefix: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelIterationProperties) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "flywheel_iteration_id" in value:
        out["FlywheelIterationId"] = value["flywheel_iteration_id"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "end_time" in value:
        import capo_comprehend.types.timestamp

        out["EndTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status" in value:
        import capo_comprehend.types.flywheel_iteration_status

        out["Status"] = (
            capo_comprehend.types.flywheel_iteration_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "evaluated_model_arn" in value:
        out["EvaluatedModelArn"] = value["evaluated_model_arn"]
    if "evaluated_model_metrics" in value:
        import capo_comprehend.types.flywheel_model_evaluation_metrics

        out["EvaluatedModelMetrics"] = (
            capo_comprehend.types.flywheel_model_evaluation_metrics.serialize_aws_json_1_1(
                value["evaluated_model_metrics"]
            )
        )
    if "trained_model_arn" in value:
        out["TrainedModelArn"] = value["trained_model_arn"]
    if "trained_model_metrics" in value:
        import capo_comprehend.types.flywheel_model_evaluation_metrics

        out["TrainedModelMetrics"] = (
            capo_comprehend.types.flywheel_model_evaluation_metrics.serialize_aws_json_1_1(
                value["trained_model_metrics"]
            )
        )
    if "evaluation_manifest_s3_prefix" in value:
        out["EvaluationManifestS3Prefix"] = value["evaluation_manifest_s3_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlywheelIterationProperties:
    out: FlywheelIterationProperties = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("FlywheelIterationId") is not None:
        out["flywheel_iteration_id"] = data["FlywheelIterationId"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("EndTime") is not None:
        import capo_comprehend.types.timestamp

        out["end_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("Status") is not None:
        import capo_comprehend.types.flywheel_iteration_status

        out["status"] = (
            capo_comprehend.types.flywheel_iteration_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("EvaluatedModelArn") is not None:
        out["evaluated_model_arn"] = data["EvaluatedModelArn"]
    if data.get("EvaluatedModelMetrics") is not None:
        import capo_comprehend.types.flywheel_model_evaluation_metrics

        out["evaluated_model_metrics"] = (
            capo_comprehend.types.flywheel_model_evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluatedModelMetrics"]
            )
        )
    if data.get("TrainedModelArn") is not None:
        out["trained_model_arn"] = data["TrainedModelArn"]
    if data.get("TrainedModelMetrics") is not None:
        import capo_comprehend.types.flywheel_model_evaluation_metrics

        out["trained_model_metrics"] = (
            capo_comprehend.types.flywheel_model_evaluation_metrics.deserialize_aws_json_1_1(
                data["TrainedModelMetrics"]
            )
        )
    if data.get("EvaluationManifestS3Prefix") is not None:
        out["evaluation_manifest_s3_prefix"] = data["EvaluationManifestS3Prefix"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlywheelIterationProperties) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "flywheel_iteration_id" in value:
        out["FlywheelIterationId"] = value["flywheel_iteration_id"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["creation_time"]
        )
    if "end_time" in value:
        import capo_comprehend.types.timestamp

        out["EndTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "status" in value:
        import capo_comprehend.types.flywheel_iteration_status

        out["Status"] = capo_comprehend.types.flywheel_iteration_status.serialize_cbor(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "evaluated_model_arn" in value:
        out["EvaluatedModelArn"] = value["evaluated_model_arn"]
    if "evaluated_model_metrics" in value:
        import capo_comprehend.types.flywheel_model_evaluation_metrics

        out["EvaluatedModelMetrics"] = (
            capo_comprehend.types.flywheel_model_evaluation_metrics.serialize_cbor(
                value["evaluated_model_metrics"]
            )
        )
    if "trained_model_arn" in value:
        out["TrainedModelArn"] = value["trained_model_arn"]
    if "trained_model_metrics" in value:
        import capo_comprehend.types.flywheel_model_evaluation_metrics

        out["TrainedModelMetrics"] = (
            capo_comprehend.types.flywheel_model_evaluation_metrics.serialize_cbor(
                value["trained_model_metrics"]
            )
        )
    if "evaluation_manifest_s3_prefix" in value:
        out["EvaluationManifestS3Prefix"] = value["evaluation_manifest_s3_prefix"]
    return out


def deserialize_cbor(data: dict) -> FlywheelIterationProperties:
    out: FlywheelIterationProperties = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("FlywheelIterationId") is not None:
        out["flywheel_iteration_id"] = data["FlywheelIterationId"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("EndTime") is not None:
        import capo_comprehend.types.timestamp

        out["end_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["EndTime"]
        )
    if data.get("Status") is not None:
        import capo_comprehend.types.flywheel_iteration_status

        out["status"] = (
            capo_comprehend.types.flywheel_iteration_status.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("EvaluatedModelArn") is not None:
        out["evaluated_model_arn"] = data["EvaluatedModelArn"]
    if data.get("EvaluatedModelMetrics") is not None:
        import capo_comprehend.types.flywheel_model_evaluation_metrics

        out["evaluated_model_metrics"] = (
            capo_comprehend.types.flywheel_model_evaluation_metrics.deserialize_cbor(
                data["EvaluatedModelMetrics"]
            )
        )
    if data.get("TrainedModelArn") is not None:
        out["trained_model_arn"] = data["TrainedModelArn"]
    if data.get("TrainedModelMetrics") is not None:
        import capo_comprehend.types.flywheel_model_evaluation_metrics

        out["trained_model_metrics"] = (
            capo_comprehend.types.flywheel_model_evaluation_metrics.deserialize_cbor(
                data["TrainedModelMetrics"]
            )
        )
    if data.get("EvaluationManifestS3Prefix") is not None:
        out["evaluation_manifest_s3_prefix"] = data["EvaluationManifestS3Prefix"]
    return out
