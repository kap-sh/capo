"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartBotResourceGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.generation_input
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class StartBotResourceGenerationRequest(TypedDict, closed=True):
    generation_input_prompt: "capo_lex_models_v2.types.generation_input.GenerationInput"
    """<p>The prompt to generate intents and slot types for the bot locale. Your description should be both <i>detailed</i> and <i>precise</i> to help generate appropriate and sufficient intents for your bot. Include a list of actions to improve the intent creation process.</p>"""
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot for which to generate intents and slot types.</p>"""
    bot_version: "capo_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot for which to generate intents and slot types.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale of the bot for which to generate intents and slot types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBotResourceGenerationRequest) -> dict:
    out: dict = {}
    out["generationInputPrompt"] = value["generation_input_prompt"]
    return out


def deserialize_json(data: dict) -> StartBotResourceGenerationRequest:
    out: StartBotResourceGenerationRequest = {}  # type: ignore[typeddict-item]
    if data.get("generationInputPrompt") is not None:
        out["generation_input_prompt"] = data["generationInputPrompt"]
    else:
        out["generation_input_prompt"] = ""
    return out
