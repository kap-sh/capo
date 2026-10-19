"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationReferenceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.context
    import capo_bedrock_agentcore.types.evaluation_content
    import capo_bedrock_agentcore.types.evaluation_content_list
    import capo_bedrock_agentcore.types.evaluation_expected_trajectory


class EvaluationReferenceInput(TypedDict, closed=True):
    context: "capo_bedrock_agentcore.types.context.Context"
    """<p> The span context that identifies which session or trace this reference input applies to, used for correlating ground truth with agent output. </p>"""
    expected_response: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_content.EvaluationContent"
    ]
    """<p> The expected response for trace-level evaluation. Built-in evaluators that support this field compare the agent's actual response against this value for assessment. Custom evaluators can access it through the <code>{expected_response}</code> placeholder in their instructions. </p>"""
    assertions: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_content_list.EvaluationContentList"
    ]
    """<p> A list of assertion statements for session-level evaluation. Each assertion describes an expected behavior or outcome the agent should demonstrate during the session. </p>"""
    expected_trajectory: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_expected_trajectory.EvaluationExpectedTrajectory"
    ]
    """<p> The expected tool call sequence for session-level trajectory evaluation. Contains a list of tool names representing the tools the agent is expected to invoke. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReferenceInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.context

    out["context"] = capo_bedrock_agentcore.types.context.serialize_json(
        value["context"]
    )
    if "expected_response" in value:
        import capo_bedrock_agentcore.types.evaluation_content

        out["expectedResponse"] = (
            capo_bedrock_agentcore.types.evaluation_content.serialize_json(
                value["expected_response"]
            )
        )
    if "assertions" in value:
        import capo_bedrock_agentcore.types.evaluation_content_list

        out["assertions"] = (
            capo_bedrock_agentcore.types.evaluation_content_list.serialize_json(
                value["assertions"]
            )
        )
    if "expected_trajectory" in value:
        import capo_bedrock_agentcore.types.evaluation_expected_trajectory

        out["expectedTrajectory"] = (
            capo_bedrock_agentcore.types.evaluation_expected_trajectory.serialize_json(
                value["expected_trajectory"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationReferenceInput:
    out: EvaluationReferenceInput = {}  # type: ignore[typeddict-item]
    if data.get("context") is not None:
        import capo_bedrock_agentcore.types.context

        out["context"] = capo_bedrock_agentcore.types.context.deserialize_json(
            data["context"]
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["context"] = capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
    if data.get("expectedResponse") is not None:
        import capo_bedrock_agentcore.types.evaluation_content

        out["expected_response"] = (
            capo_bedrock_agentcore.types.evaluation_content.deserialize_json(
                data["expectedResponse"]
            )
        )
    if data.get("assertions") is not None:
        import capo_bedrock_agentcore.types.evaluation_content_list

        out["assertions"] = (
            capo_bedrock_agentcore.types.evaluation_content_list.deserialize_json(
                data["assertions"]
            )
        )
    if data.get("expectedTrajectory") is not None:
        import capo_bedrock_agentcore.types.evaluation_expected_trajectory

        out["expected_trajectory"] = (
            capo_bedrock_agentcore.types.evaluation_expected_trajectory.deserialize_json(
                data["expectedTrajectory"]
            )
        )
    return out
