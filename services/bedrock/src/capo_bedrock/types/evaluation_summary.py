"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.application_type
    import capo_bedrock.types.evaluation_bedrock_knowledge_base_identifiers
    import capo_bedrock.types.evaluation_bedrock_model_identifiers
    import capo_bedrock.types.evaluation_inference_config_summary
    import capo_bedrock.types.evaluation_job_arn
    import capo_bedrock.types.evaluation_job_name
    import capo_bedrock.types.evaluation_job_status
    import capo_bedrock.types.evaluation_job_type
    import capo_bedrock.types.evaluation_task_types
    import capo_bedrock.types.evaluator_model_identifiers
    import capo_bedrock.types.timestamp


class EvaluationSummary(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.evaluation_job_arn.EvaluationJobArn"
    """<p>The Amazon Resource Name (ARN) of the evaluation job.</p>"""
    job_name: "capo_bedrock.types.evaluation_job_name.EvaluationJobName"
    """<p>The name for the evaluation job.</p>"""
    status: "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus"
    """<p>The current status of the evaluation job.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The time the evaluation job was created.</p>"""
    job_type: "capo_bedrock.types.evaluation_job_type.EvaluationJobType"
    """<p>Specifies whether the evaluation job is automated or human-based.</p>"""
    evaluation_task_types: (
        "capo_bedrock.types.evaluation_task_types.EvaluationTaskTypes"
    )
    """<p>The type of task for model evaluation.</p>"""
    model_identifiers: "capo_bedrock.types.evaluation_bedrock_model_identifiers.EvaluationBedrockModelIdentifiers"
    """<p>The Amazon Resource Names (ARNs) of the model(s) used for the evaluation job.</p>"""
    rag_identifiers: NotRequired[
        "capo_bedrock.types.evaluation_bedrock_knowledge_base_identifiers.EvaluationBedrockKnowledgeBaseIdentifiers"
    ]
    """<p>The Amazon Resource Names (ARNs) of the knowledge base resources used for a knowledge base evaluation job.</p>"""
    evaluator_model_identifiers: NotRequired[
        "capo_bedrock.types.evaluator_model_identifiers.EvaluatorModelIdentifiers"
    ]
    """<p>The Amazon Resource Names (ARNs) of the models used to compute the metrics for a knowledge base evaluation job.</p>"""
    custom_metrics_evaluator_model_identifiers: NotRequired[
        "capo_bedrock.types.evaluator_model_identifiers.EvaluatorModelIdentifiers"
    ]
    """<p>The Amazon Resource Names (ARNs) of the models used to compute custom metrics in an Amazon Bedrock evaluation job.</p>"""
    inference_config_summary: NotRequired[
        "capo_bedrock.types.evaluation_inference_config_summary.EvaluationInferenceConfigSummary"
    ]
    """<p>Identifies the models, Knowledge Bases, or other RAG sources evaluated in a model or Knowledge Base evaluation job.</p>"""
    application_type: NotRequired["capo_bedrock.types.application_type.ApplicationType"]
    """<p>Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    import capo_bedrock.types.evaluation_job_status

    out["status"] = capo_bedrock.types.evaluation_job_status.serialize_json(
        value["status"]
    )
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    import capo_bedrock.types.evaluation_job_type

    out["jobType"] = capo_bedrock.types.evaluation_job_type.serialize_json(
        value["job_type"]
    )
    import capo_bedrock.types.evaluation_task_types

    out["evaluationTaskTypes"] = (
        capo_bedrock.types.evaluation_task_types.serialize_json(
            value["evaluation_task_types"]
        )
    )
    import capo_bedrock.types.evaluation_bedrock_model_identifiers

    out["modelIdentifiers"] = (
        capo_bedrock.types.evaluation_bedrock_model_identifiers.serialize_json(
            value.get("model_identifiers", [])
        )
    )
    if "rag_identifiers" in value:
        import capo_bedrock.types.evaluation_bedrock_knowledge_base_identifiers

        out["ragIdentifiers"] = (
            capo_bedrock.types.evaluation_bedrock_knowledge_base_identifiers.serialize_json(
                value["rag_identifiers"]
            )
        )
    if "evaluator_model_identifiers" in value:
        import capo_bedrock.types.evaluator_model_identifiers

        out["evaluatorModelIdentifiers"] = (
            capo_bedrock.types.evaluator_model_identifiers.serialize_json(
                value["evaluator_model_identifiers"]
            )
        )
    if "custom_metrics_evaluator_model_identifiers" in value:
        import capo_bedrock.types.evaluator_model_identifiers

        out["customMetricsEvaluatorModelIdentifiers"] = (
            capo_bedrock.types.evaluator_model_identifiers.serialize_json(
                value["custom_metrics_evaluator_model_identifiers"]
            )
        )
    if "inference_config_summary" in value:
        import capo_bedrock.types.evaluation_inference_config_summary

        out["inferenceConfigSummary"] = (
            capo_bedrock.types.evaluation_inference_config_summary.serialize_json(
                value["inference_config_summary"]
            )
        )
    if "application_type" in value:
        import capo_bedrock.types.application_type

        out["applicationType"] = capo_bedrock.types.application_type.serialize_json(
            value["application_type"]
        )
    return out


def deserialize_json(data: dict) -> EvaluationSummary:
    out: EvaluationSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("status") is not None:
        import capo_bedrock.types.evaluation_job_status

        out["status"] = capo_bedrock.types.evaluation_job_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus", ""
        )
    if data.get("creationTime") is not None:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("jobType") is not None:
        import capo_bedrock.types.evaluation_job_type

        out["job_type"] = capo_bedrock.types.evaluation_job_type.deserialize_json(
            data["jobType"]
        )
    else:
        import typing

        out["job_type"] = typing.cast(
            "capo_bedrock.types.evaluation_job_type.EvaluationJobType", ""
        )
    if data.get("evaluationTaskTypes") is not None:
        import capo_bedrock.types.evaluation_task_types

        out["evaluation_task_types"] = (
            capo_bedrock.types.evaluation_task_types.deserialize_json(
                data["evaluationTaskTypes"]
            )
        )
    else:
        out["evaluation_task_types"] = []
    if data.get("modelIdentifiers") is not None:
        import capo_bedrock.types.evaluation_bedrock_model_identifiers

        out["model_identifiers"] = (
            capo_bedrock.types.evaluation_bedrock_model_identifiers.deserialize_json(
                data["modelIdentifiers"]
            )
        )
    else:
        out["model_identifiers"] = []
    if data.get("ragIdentifiers") is not None:
        import capo_bedrock.types.evaluation_bedrock_knowledge_base_identifiers

        out["rag_identifiers"] = (
            capo_bedrock.types.evaluation_bedrock_knowledge_base_identifiers.deserialize_json(
                data["ragIdentifiers"]
            )
        )
    if data.get("evaluatorModelIdentifiers") is not None:
        import capo_bedrock.types.evaluator_model_identifiers

        out["evaluator_model_identifiers"] = (
            capo_bedrock.types.evaluator_model_identifiers.deserialize_json(
                data["evaluatorModelIdentifiers"]
            )
        )
    if data.get("customMetricsEvaluatorModelIdentifiers") is not None:
        import capo_bedrock.types.evaluator_model_identifiers

        out["custom_metrics_evaluator_model_identifiers"] = (
            capo_bedrock.types.evaluator_model_identifiers.deserialize_json(
                data["customMetricsEvaluatorModelIdentifiers"]
            )
        )
    if data.get("inferenceConfigSummary") is not None:
        import capo_bedrock.types.evaluation_inference_config_summary

        out["inference_config_summary"] = (
            capo_bedrock.types.evaluation_inference_config_summary.deserialize_json(
                data["inferenceConfigSummary"]
            )
        )
    if data.get("applicationType") is not None:
        import capo_bedrock.types.application_type

        out["application_type"] = capo_bedrock.types.application_type.deserialize_json(
            data["applicationType"]
        )
    return out
