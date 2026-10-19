"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.numerical_bot_version
    import capo_lex_models_v2.types.skip_resource_in_use_check


class DeleteBotVersionRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot that contains the version.</p>"""
    bot_version: "capo_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    """<p>The version of the bot to delete.</p>"""
    skip_resource_in_use_check: NotRequired[
        "capo_lex_models_v2.types.skip_resource_in_use_check.SkipResourceInUseCheck"
    ]
    """<p>By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a <code>ResourceInUseException</code> exception if the version is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the version even if it is being used by another resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotVersionRequest:
    out: DeleteBotVersionRequest = {}  # type: ignore[typeddict-item]
    return out
