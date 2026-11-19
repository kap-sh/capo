"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluator_filter_list
    import capo_bedrock_agentcore.types.ground_truth_field_list


class GroundTruthConfig(TypedDict, closed=True):
    fields: "capo_bedrock_agentcore.types.ground_truth_field_list.GroundTruthFieldList"
    """<p>The reference fields to copy. Values are copied from the session as observed, not generated.</p>"""
    quality_filters: NotRequired[
        "capo_bedrock_agentcore.types.evaluator_filter_list.EvaluatorFilterList"
    ]
    """<p>Evaluator conditions that a selected session must also meet to have reference fields copied. If you don't specify these, the generation uses the evaluator filters from <code>selection</code>. If the selection names sessions and traces by ID, every selected session gets reference fields. Specify an empty list to give every selected session reference fields. You can't specify quality filters with a <code>cloudWatchLogs</code> source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.ground_truth_field_list

    out["fields"] = capo_bedrock_agentcore.types.ground_truth_field_list.serialize_json(
        value["fields"]
    )
    if "quality_filters" in value:
        import capo_bedrock_agentcore.types.evaluator_filter_list

        out["qualityFilters"] = (
            capo_bedrock_agentcore.types.evaluator_filter_list.serialize_json(
                value["quality_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GroundTruthConfig:
    out: GroundTruthConfig = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_bedrock_agentcore.types.ground_truth_field_list

        out["fields"] = (
            capo_bedrock_agentcore.types.ground_truth_field_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        out["fields"] = []
    if data.get("qualityFilters") is not None:
        import capo_bedrock_agentcore.types.evaluator_filter_list

        out["quality_filters"] = (
            capo_bedrock_agentcore.types.evaluator_filter_list.deserialize_json(
                data["qualityFilters"]
            )
        )
    return out
