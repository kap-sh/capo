"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.evaluator_metric_list


class ABTestResults(TypedDict, closed=True):
    analysis_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the analysis was performed.</p>"""
    evaluator_metrics: (
        "capo_bedrock_agentcore.types.evaluator_metric_list.EvaluatorMetricList"
    )
    """<p>The per-evaluator metrics comparing control and treatment variants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ABTestResults) -> dict:
    out: dict = {}
    if "analysis_timestamp" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["analysisTimestamp"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["analysis_timestamp"]
            )
        )
    import capo_bedrock_agentcore.types.evaluator_metric_list

    out["evaluatorMetrics"] = (
        capo_bedrock_agentcore.types.evaluator_metric_list.serialize_json(
            value["evaluator_metrics"]
        )
    )
    return out


def deserialize_json(data: dict) -> ABTestResults:
    out: ABTestResults = {}  # type: ignore[typeddict-item]
    if data.get("analysisTimestamp") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["analysis_timestamp"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["analysisTimestamp"]
            )
        )
    if data.get("evaluatorMetrics") is not None:
        import capo_bedrock_agentcore.types.evaluator_metric_list

        out["evaluator_metrics"] = (
            capo_bedrock_agentcore.types.evaluator_metric_list.deserialize_json(
                data["evaluatorMetrics"]
            )
        )
    else:
        out["evaluator_metrics"] = []
    return out
