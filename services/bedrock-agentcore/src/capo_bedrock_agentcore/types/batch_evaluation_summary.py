"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchEvaluationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.batch_evaluation_arn
    import capo_bedrock_agentcore.types.batch_evaluation_description
    import capo_bedrock_agentcore.types.batch_evaluation_id
    import capo_bedrock_agentcore.types.batch_evaluation_name
    import capo_bedrock_agentcore.types.batch_evaluation_status
    import capo_bedrock_agentcore.types.error_details_list
    import capo_bedrock_agentcore.types.evaluation_job_results
    import capo_bedrock_agentcore.types.evaluator_list
    import capo_bedrock_agentcore.types.insight_list
    import capo_bedrock_agentcore.types.kms_key_arn


class BatchEvaluationSummary(TypedDict, closed=True):
    batch_evaluation_id: (
        "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    )
    """<p>The unique identifier of the batch evaluation.</p>"""
    batch_evaluation_arn: (
        "capo_bedrock_agentcore.types.batch_evaluation_arn.BatchEvaluationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the batch evaluation.</p>"""
    batch_evaluation_name: (
        "capo_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName"
    )
    """<p>The name of the batch evaluation.</p>"""
    status: "capo_bedrock_agentcore.types.batch_evaluation_status.BatchEvaluationStatus"
    """<p>The current status of the batch evaluation.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the batch evaluation was created.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"
    ]
    """<p>The description of the batch evaluation.</p>"""
    evaluators: NotRequired["capo_bedrock_agentcore.types.evaluator_list.EvaluatorList"]
    """<p>The list of evaluators applied during the batch evaluation.</p>"""
    insights: NotRequired["capo_bedrock_agentcore.types.insight_list.InsightList"]
    """<p>The list of insight analyses applied during the batch evaluation.</p>"""
    evaluation_results: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_job_results.EvaluationJobResults"
    ]
    """<p>The aggregated evaluation results.</p>"""
    error_details: NotRequired[
        "capo_bedrock_agentcore.types.error_details_list.ErrorDetailsList"
    ]
    """<p>The error details if the batch evaluation encountered failures.</p>"""
    kms_key_arn: NotRequired["capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key used to encrypt evaluation data.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the batch evaluation was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluationSummary) -> dict:
    out: dict = {}
    out["batchEvaluationId"] = value["batch_evaluation_id"]
    out["batchEvaluationArn"] = value["batch_evaluation_arn"]
    out["batchEvaluationName"] = value["batch_evaluation_name"]
    import capo_bedrock_agentcore.types.batch_evaluation_status

    out["status"] = capo_bedrock_agentcore.types.batch_evaluation_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore._protocol.serialize

    out["createdAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "evaluators" in value:
        import capo_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = capo_bedrock_agentcore.types.evaluator_list.serialize_json(
            value["evaluators"]
        )
    if "insights" in value:
        import capo_bedrock_agentcore.types.insight_list

        out["insights"] = capo_bedrock_agentcore.types.insight_list.serialize_json(
            value["insights"]
        )
    if "evaluation_results" in value:
        import capo_bedrock_agentcore.types.evaluation_job_results

        out["evaluationResults"] = (
            capo_bedrock_agentcore.types.evaluation_job_results.serialize_json(
                value["evaluation_results"]
            )
        )
    if "error_details" in value:
        import capo_bedrock_agentcore.types.error_details_list

        out["errorDetails"] = (
            capo_bedrock_agentcore.types.error_details_list.serialize_json(
                value["error_details"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "updated_at" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["updatedAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> BatchEvaluationSummary:
    out: BatchEvaluationSummary = {}  # type: ignore[typeddict-item]
    if data.get("batchEvaluationId") is not None:
        out["batch_evaluation_id"] = data["batchEvaluationId"]
    else:
        out["batch_evaluation_id"] = ""
    if data.get("batchEvaluationArn") is not None:
        out["batch_evaluation_arn"] = data["batchEvaluationArn"]
    else:
        out["batch_evaluation_arn"] = ""
    if data.get("batchEvaluationName") is not None:
        out["batch_evaluation_name"] = data["batchEvaluationName"]
    else:
        out["batch_evaluation_name"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.batch_evaluation_status

        out["status"] = (
            capo_bedrock_agentcore.types.batch_evaluation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.batch_evaluation_status.BatchEvaluationStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("evaluators") is not None:
        import capo_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = (
            capo_bedrock_agentcore.types.evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    if data.get("insights") is not None:
        import capo_bedrock_agentcore.types.insight_list

        out["insights"] = capo_bedrock_agentcore.types.insight_list.deserialize_json(
            data["insights"]
        )
    if data.get("evaluationResults") is not None:
        import capo_bedrock_agentcore.types.evaluation_job_results

        out["evaluation_results"] = (
            capo_bedrock_agentcore.types.evaluation_job_results.deserialize_json(
                data["evaluationResults"]
            )
        )
    if data.get("errorDetails") is not None:
        import capo_bedrock_agentcore.types.error_details_list

        out["error_details"] = (
            capo_bedrock_agentcore.types.error_details_list.deserialize_json(
                data["errorDetails"]
            )
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
