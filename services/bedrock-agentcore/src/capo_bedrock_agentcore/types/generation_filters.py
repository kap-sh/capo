"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluator_filter_list
    import capo_bedrock_agentcore.types.generation_attribute_filter_list
    import capo_bedrock_agentcore.types.turn_count_range


class GenerationFilters(TypedDict, closed=True):
    attribute_filters: NotRequired[
        "capo_bedrock_agentcore.types.generation_attribute_filter_list.GenerationAttributeFilterList"
    ]
    """<p>Attribute conditions, up to 5. A session must meet all of them. An attribute on a span matches when any span in the session meets the condition.</p>"""
    turn_count: NotRequired[
        "capo_bedrock_agentcore.types.turn_count_range.TurnCountRange"
    ]
    """<p>The range of turns a session can have. For example, set <code>max</code> to 1 for single-turn sessions only, or <code>min</code> to 2 for multi-turn sessions only. Sessions with more than 100 turns are never selected.</p>"""
    evaluator_filters: NotRequired[
        "capo_bedrock_agentcore.types.evaluator_filter_list.EvaluatorFilterList"
    ]
    """<p>Conditions on evaluation results, up to 10. A session must meet all of them. You can use these only with an <code>onlineEvaluation</code> or <code>batchEvaluation</code> source. A <code>cloudWatchLogs</code> source has no evaluation results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationFilters) -> dict:
    out: dict = {}
    if "attribute_filters" in value:
        import capo_bedrock_agentcore.types.generation_attribute_filter_list

        out["attributeFilters"] = (
            capo_bedrock_agentcore.types.generation_attribute_filter_list.serialize_json(
                value["attribute_filters"]
            )
        )
    if "turn_count" in value:
        import capo_bedrock_agentcore.types.turn_count_range

        out["turnCount"] = capo_bedrock_agentcore.types.turn_count_range.serialize_json(
            value["turn_count"]
        )
    if "evaluator_filters" in value:
        import capo_bedrock_agentcore.types.evaluator_filter_list

        out["evaluatorFilters"] = (
            capo_bedrock_agentcore.types.evaluator_filter_list.serialize_json(
                value["evaluator_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GenerationFilters:
    out: GenerationFilters = {}  # type: ignore[typeddict-item]
    if data.get("attributeFilters") is not None:
        import capo_bedrock_agentcore.types.generation_attribute_filter_list

        out["attribute_filters"] = (
            capo_bedrock_agentcore.types.generation_attribute_filter_list.deserialize_json(
                data["attributeFilters"]
            )
        )
    if data.get("turnCount") is not None:
        import capo_bedrock_agentcore.types.turn_count_range

        out["turn_count"] = (
            capo_bedrock_agentcore.types.turn_count_range.deserialize_json(
                data["turnCount"]
            )
        )
    if data.get("evaluatorFilters") is not None:
        import capo_bedrock_agentcore.types.evaluator_filter_list

        out["evaluator_filters"] = (
            capo_bedrock_agentcore.types.evaluator_filter_list.deserialize_json(
                data["evaluatorFilters"]
            )
        )
    return out
