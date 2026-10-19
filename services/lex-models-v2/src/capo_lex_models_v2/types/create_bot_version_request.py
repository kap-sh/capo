"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version_locale_specification
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.id


class CreateBotVersionRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to create the version for.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>A description of the version. Use the description to help identify the version in lists.</p>"""
    bot_version_locale_specification: "capo_lex_models_v2.types.bot_version_locale_specification.BotVersionLocaleSpecification"
    """<p>Specifies the locales that Amazon Lex adds to this version. You can choose the <code>Draft</code> version or any other previously published version for each locale. When you specify a source version, the locale data is copied from the source version to the new version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_lex_models_v2.types.bot_version_locale_specification

    out["botVersionLocaleSpecification"] = (
        capo_lex_models_v2.types.bot_version_locale_specification.serialize_json(
            value["bot_version_locale_specification"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateBotVersionRequest:
    out: CreateBotVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("botVersionLocaleSpecification") is not None:
        import capo_lex_models_v2.types.bot_version_locale_specification

        out["bot_version_locale_specification"] = (
            capo_lex_models_v2.types.bot_version_locale_specification.deserialize_json(
                data["botVersionLocaleSpecification"]
            )
        )
    else:
        out["bot_version_locale_specification"] = {}
    return out
