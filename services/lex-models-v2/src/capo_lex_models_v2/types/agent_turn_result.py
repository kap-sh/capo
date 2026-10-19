"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AgentTurnResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.execution_error_details
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.test_result_slot_name
    import capo_lex_models_v2.types.test_set_agent_prompt


class AgentTurnResult(TypedDict, closed=True):
    expected_agent_prompt: (
        "capo_lex_models_v2.types.test_set_agent_prompt.TestSetAgentPrompt"
    )
    """<p>The expected agent prompt for the agent turn in a test set execution.</p>"""
    actual_agent_prompt: NotRequired[
        "capo_lex_models_v2.types.test_set_agent_prompt.TestSetAgentPrompt"
    ]
    """<p>The actual agent prompt for the agent turn in a test set execution.</p>"""
    error_details: NotRequired[
        "capo_lex_models_v2.types.execution_error_details.ExecutionErrorDetails"
    ]
    actual_elicited_slot: NotRequired[
        "capo_lex_models_v2.types.test_result_slot_name.TestResultSlotName"
    ]
    """<p>The actual elicited slot for the agent turn in a test set execution.</p>"""
    actual_intent: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The actual intent for the agent turn in a test set execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentTurnResult) -> dict:
    out: dict = {}
    out["expectedAgentPrompt"] = value["expected_agent_prompt"]
    if "actual_agent_prompt" in value:
        out["actualAgentPrompt"] = value["actual_agent_prompt"]
    if "error_details" in value:
        import capo_lex_models_v2.types.execution_error_details

        out["errorDetails"] = (
            capo_lex_models_v2.types.execution_error_details.serialize_json(
                value["error_details"]
            )
        )
    if "actual_elicited_slot" in value:
        out["actualElicitedSlot"] = value["actual_elicited_slot"]
    if "actual_intent" in value:
        out["actualIntent"] = value["actual_intent"]
    return out


def deserialize_json(data: dict) -> AgentTurnResult:
    out: AgentTurnResult = {}  # type: ignore[typeddict-item]
    if data.get("expectedAgentPrompt") is not None:
        out["expected_agent_prompt"] = data["expectedAgentPrompt"]
    else:
        out["expected_agent_prompt"] = ""
    if data.get("actualAgentPrompt") is not None:
        out["actual_agent_prompt"] = data["actualAgentPrompt"]
    if data.get("errorDetails") is not None:
        import capo_lex_models_v2.types.execution_error_details

        out["error_details"] = (
            capo_lex_models_v2.types.execution_error_details.deserialize_json(
                data["errorDetails"]
            )
        )
    if data.get("actualElicitedSlot") is not None:
        out["actual_elicited_slot"] = data["actualElicitedSlot"]
    if data.get("actualIntent") is not None:
        out["actual_intent"] = data["actualIntent"]
    return out
