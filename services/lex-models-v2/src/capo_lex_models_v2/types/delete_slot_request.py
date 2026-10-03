"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteSlotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class DeleteSlotRequest(TypedDict, closed=True):
    slot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the slot to delete. </p>"""
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with the slot to delete.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot associated with the slot to delete.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale that the slot will be deleted from. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    intent_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the intent associated with the slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSlotRequest:
    out: DeleteSlotRequest = {}  # type: ignore[typeddict-item]
    return out
