"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionMetadataShape``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ground_truth_source
    import capo_bedrock_agentcore.types.string_map


class SessionMetadataShape(TypedDict, closed=True):
    session_id: "str"
    """<p>The unique identifier of the session this metadata applies to.</p>"""
    test_scenario_id: NotRequired["str"]
    """<p>An optional test scenario identifier for categorizing and tracking evaluation results.</p>"""
    ground_truth: NotRequired[
        "capo_bedrock_agentcore.types.ground_truth_source.GroundTruthSource"
    ]
    """<p>The ground truth data for this session, including expected responses and assertions.</p>"""
    metadata: NotRequired["capo_bedrock_agentcore.types.string_map.StringMap"]
    """<p>Additional key-value metadata associated with this session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionMetadataShape) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    if "test_scenario_id" in value:
        out["testScenarioId"] = value["test_scenario_id"]
    if "ground_truth" in value:
        import capo_bedrock_agentcore.types.ground_truth_source

        out["groundTruth"] = (
            capo_bedrock_agentcore.types.ground_truth_source.serialize_json(
                value["ground_truth"]
            )
        )
    if "metadata" in value:
        import capo_bedrock_agentcore.types.string_map

        out["metadata"] = capo_bedrock_agentcore.types.string_map.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> SessionMetadataShape:
    out: SessionMetadataShape = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("testScenarioId") is not None:
        out["test_scenario_id"] = data["testScenarioId"]
    if data.get("groundTruth") is not None:
        import capo_bedrock_agentcore.types.ground_truth_source

        out["ground_truth"] = (
            capo_bedrock_agentcore.types.ground_truth_source.deserialize_json(
                data["groundTruth"]
            )
        )
    if data.get("metadata") is not None:
        import capo_bedrock_agentcore.types.string_map

        out["metadata"] = capo_bedrock_agentcore.types.string_map.deserialize_json(
            data["metadata"]
        )
    return out
