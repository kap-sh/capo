"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.skip_resource_in_use_check


class DeleteBotAliasRequest(TypedDict, closed=True):
    bot_alias_id: "capo_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The unique identifier of the bot alias to delete.</p>"""
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot associated with the alias to delete.</p>"""
    skip_resource_in_use_check: NotRequired[
        "capo_lex_models_v2.types.skip_resource_in_use_check.SkipResourceInUseCheck"
    ]
    """<p>By default, Amazon Lex checks if any other resource, such as a bot network, is using the bot alias before it is deleted and throws a <code>ResourceInUseException</code> exception if the alias is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the alias even if it is being used by another resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotAliasRequest:
    out: DeleteBotAliasRequest = {}  # type: ignore[typeddict-item]
    return out
