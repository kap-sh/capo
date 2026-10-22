"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#WaitAndContinueSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.response_specification
    import capo_lex_models_v2.types.still_waiting_response_specification


class WaitAndContinueSpecification(TypedDict, closed=True):
    waiting_response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    """<p>The response that Amazon Lex sends to indicate that the bot is waiting for the conversation to continue. Required unless the bot locale's <code>assistedNluMode</code> is <code>DialogManager</code>.</p>"""
    continue_response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    """<p>The response that Amazon Lex sends to indicate that the bot is ready to continue the conversation. Required unless the bot locale's <code>assistedNluMode</code> is <code>DialogManager</code>.</p>"""
    still_waiting_response: NotRequired[
        "capo_lex_models_v2.types.still_waiting_response_specification.StillWaitingResponseSpecification"
    ]
    """<p>A response that Amazon Lex sends periodically to the user to indicate that the bot is still waiting for input from the user.</p>"""
    active: NotRequired["capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether the bot will wait for a user to respond. When this field is false, wait and continue responses for a slot aren't used. If the <code>active</code> field isn't specified, the default is true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitAndContinueSpecification) -> dict:
    out: dict = {}
    if "waiting_response" in value:
        import capo_lex_models_v2.types.response_specification

        out["waitingResponse"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["waiting_response"]
            )
        )
    if "continue_response" in value:
        import capo_lex_models_v2.types.response_specification

        out["continueResponse"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["continue_response"]
            )
        )
    if "still_waiting_response" in value:
        import capo_lex_models_v2.types.still_waiting_response_specification

        out["stillWaitingResponse"] = (
            capo_lex_models_v2.types.still_waiting_response_specification.serialize_json(
                value["still_waiting_response"]
            )
        )
    if "active" in value:
        out["active"] = value["active"]
    return out


def deserialize_json(data: dict) -> WaitAndContinueSpecification:
    out: WaitAndContinueSpecification = {}  # type: ignore[typeddict-item]
    if data.get("waitingResponse") is not None:
        import capo_lex_models_v2.types.response_specification

        out["waiting_response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["waitingResponse"]
            )
        )
    if data.get("continueResponse") is not None:
        import capo_lex_models_v2.types.response_specification

        out["continue_response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["continueResponse"]
            )
        )
    if data.get("stillWaitingResponse") is not None:
        import capo_lex_models_v2.types.still_waiting_response_specification

        out["still_waiting_response"] = (
            capo_lex_models_v2.types.still_waiting_response_specification.deserialize_json(
                data["stillWaitingResponse"]
            )
        )
    if data.get("active") is not None:
        out["active"] = data["active"]
    return out
