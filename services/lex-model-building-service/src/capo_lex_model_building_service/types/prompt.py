"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Prompt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.message_list
    import capo_lex_model_building_service.types.prompt_max_attempts
    import capo_lex_model_building_service.types.response_card


class Prompt(TypedDict, closed=True):
    messages: "capo_lex_model_building_service.types.message_list.MessageList"
    """<p>An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).</p>"""
    max_attempts: (
        "capo_lex_model_building_service.types.prompt_max_attempts.PromptMaxAttempts"
    )
    """<p>The number of times to prompt the user for information.</p>"""
    response_card: NotRequired[
        "capo_lex_model_building_service.types.response_card.ResponseCard"
    ]
    """<p>A response card. Amazon Lex uses this prompt at runtime, in the <code>PostText</code> API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see <a>ex-resp-card</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Prompt) -> dict:
    out: dict = {}
    import capo_lex_model_building_service.types.message_list

    out["messages"] = capo_lex_model_building_service.types.message_list.serialize_json(
        value["messages"]
    )
    out["maxAttempts"] = value["max_attempts"]
    if "response_card" in value:
        out["responseCard"] = value["response_card"]
    return out


def deserialize_json(data: dict) -> Prompt:
    out: Prompt = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_lex_model_building_service.types.message_list

        out["messages"] = (
            capo_lex_model_building_service.types.message_list.deserialize_json(
                data["messages"]
            )
        )
    else:
        out["messages"] = []
    if data.get("maxAttempts") is not None:
        out["max_attempts"] = data["maxAttempts"]
    else:
        out["max_attempts"] = 0
    if data.get("responseCard") is not None:
        out["response_card"] = data["responseCard"]
    return out
