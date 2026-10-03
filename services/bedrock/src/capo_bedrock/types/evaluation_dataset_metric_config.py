"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationDatasetMetricConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_dataset
    import capo_bedrock.types.evaluation_metric_names
    import capo_bedrock.types.evaluation_task_type


class EvaluationDatasetMetricConfig(TypedDict, closed=True):
    task_type: "capo_bedrock.types.evaluation_task_type.EvaluationTaskType"
    """<p>The the type of task you want to evaluate for your evaluation job. This applies only to model evaluation jobs and is ignored for knowledge base evaluation jobs.</p>"""
    dataset: "capo_bedrock.types.evaluation_dataset.EvaluationDataset"
    """<p>Specifies the prompt dataset.</p>"""
    metric_names: "capo_bedrock.types.evaluation_metric_names.EvaluationMetricNames"
    """<p>The names of the metrics you want to use for your evaluation job.</p> <p>For knowledge base evaluation jobs that evaluate retrieval only, valid values are "<code>Builtin.ContextRelevance</code>", "<code>Builtin.ContextCoverage</code>".</p> <p>For knowledge base evaluation jobs that evaluate retrieval with response generation, valid values are "<code>Builtin.Correctness</code>", "<code>Builtin.Completeness</code>", "<code>Builtin.Helpfulness</code>", "<code>Builtin.LogicalCoherence</code>", "<code>Builtin.Faithfulness</code>", "<code>Builtin.Harmfulness</code>", "<code>Builtin.Stereotyping</code>", "<code>Builtin.Refusal</code>".</p> <p>For automated model evaluation jobs, valid values are "<code>Builtin.Accuracy</code>", "<code>Builtin.Robustness</code>", and "<code>Builtin.Toxicity</code>". In model evaluation jobs that use a LLM as judge you can specify "<code>Builtin.Correctness</code>", "<code>Builtin.Completeness"</code>, "<code>Builtin.Faithfulness"</code>, "<code>Builtin.Helpfulness</code>", "<code>Builtin.Coherence</code>", "<code>Builtin.Relevance</code>", "<code>Builtin.FollowingInstructions</code>", "<code>Builtin.ProfessionalStyleAndTone</code>", You can also specify the following responsible AI related metrics only for model evaluation job that use a LLM as judge "<code>Builtin.Harmfulness</code>", "<code>Builtin.Stereotyping</code>", and "<code>Builtin.Refusal</code>".</p> <p>For human-based model evaluation jobs, the list of strings must match the <code>name</code> parameter specified in <code>HumanEvaluationCustomMetric</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationDatasetMetricConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.evaluation_task_type

    out["taskType"] = capo_bedrock.types.evaluation_task_type.serialize_json(
        value["task_type"]
    )
    import capo_bedrock.types.evaluation_dataset

    out["dataset"] = capo_bedrock.types.evaluation_dataset.serialize_json(
        value["dataset"]
    )
    import capo_bedrock.types.evaluation_metric_names

    out["metricNames"] = capo_bedrock.types.evaluation_metric_names.serialize_json(
        value["metric_names"]
    )
    return out


def deserialize_json(data: dict) -> EvaluationDatasetMetricConfig:
    out: EvaluationDatasetMetricConfig = {}  # type: ignore[typeddict-item]
    if data.get("taskType") is not None:
        import capo_bedrock.types.evaluation_task_type

        out["task_type"] = capo_bedrock.types.evaluation_task_type.deserialize_json(
            data["taskType"]
        )
    else:
        raise DeserializationError("EvaluationDatasetMetricConfig.task_type required")
    if data.get("dataset") is not None:
        import capo_bedrock.types.evaluation_dataset

        out["dataset"] = capo_bedrock.types.evaluation_dataset.deserialize_json(
            data["dataset"]
        )
    else:
        raise DeserializationError("EvaluationDatasetMetricConfig.dataset required")
    if data.get("metricNames") is not None:
        import capo_bedrock.types.evaluation_metric_names

        out["metric_names"] = (
            capo_bedrock.types.evaluation_metric_names.deserialize_json(
                data["metricNames"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationDatasetMetricConfig.metric_names required"
        )
    return out
