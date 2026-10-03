"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteSlotTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.skip_resource_in_use_check


class DeleteSlotTypeRequest(TypedDict, closed=True):
    slot_type_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the slot type to delete.</p>"""
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with the slot type.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot associated with the slot type.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale that the slot type will be deleted from. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    skip_resource_in_use_check: (
        "capo_lex_models_v2.types.skip_resource_in_use_check.SkipResourceInUseCheck"
    )
    """<p>By default, the <code>DeleteSlotType</code> operations throws a <code>ResourceInUseException</code> exception if you try to delete a slot type used by a slot. Set the <code>skipResourceInUseCheck</code> parameter to <code>true</code> to skip this check and remove the slot type even if a slot uses it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlotTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSlotTypeRequest:
    out: DeleteSlotTypeRequest = {}  # type: ignore[typeddict-item]
    return out
