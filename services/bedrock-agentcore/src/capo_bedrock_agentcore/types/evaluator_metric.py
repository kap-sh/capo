"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.control_stats
    import capo_bedrock_agentcore.types.variant_result_list


class EvaluatorMetric(TypedDict, closed=True):
    evaluator_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the evaluator.</p>"""
    control_stats: "capo_bedrock_agentcore.types.control_stats.ControlStats"
    """<p>The statistics for the control variant.</p>"""
    variant_results: (
        "capo_bedrock_agentcore.types.variant_result_list.VariantResultList"
    )
    """<p>The results for each treatment variant compared against the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorMetric) -> dict:
    out: dict = {}
    out["evaluatorArn"] = value["evaluator_arn"]
    import capo_bedrock_agentcore.types.control_stats

    out["controlStats"] = capo_bedrock_agentcore.types.control_stats.serialize_json(
        value["control_stats"]
    )
    import capo_bedrock_agentcore.types.variant_result_list

    out["variantResults"] = (
        capo_bedrock_agentcore.types.variant_result_list.serialize_json(
            value["variant_results"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluatorMetric:
    out: EvaluatorMetric = {}  # type: ignore[typeddict-item]
    if data.get("evaluatorArn") is not None:
        out["evaluator_arn"] = data["evaluatorArn"]
    else:
        out["evaluator_arn"] = ""
    if data.get("controlStats") is not None:
        import capo_bedrock_agentcore.types.control_stats

        out["control_stats"] = (
            capo_bedrock_agentcore.types.control_stats.deserialize_json(
                data["controlStats"]
            )
        )
    else:
        raise DeserializationError("EvaluatorMetric.control_stats required")
    if data.get("variantResults") is not None:
        import capo_bedrock_agentcore.types.variant_result_list

        out["variant_results"] = (
            capo_bedrock_agentcore.types.variant_result_list.deserialize_json(
                data["variantResults"]
            )
        )
    else:
        out["variant_results"] = []
    return out
