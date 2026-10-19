"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.skip_resource_in_use_check


class DeleteBotRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to delete. </p>"""
    skip_resource_in_use_check: NotRequired[
        "capo_lex_models_v2.types.skip_resource_in_use_check.SkipResourceInUseCheck"
    ]
    """<p>By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a <code>ResourceInUseException</code> exception if the bot is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the bot even if it is being used by another resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotRequest:
    out: DeleteBotRequest = {}  # type: ignore[typeddict-item]
    return out
