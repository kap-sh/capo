"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#DeleteUtterancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.user_id


class DeleteUtterancesRequest(TypedDict, closed=True):
    bot_name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot that stored the utterances.</p>"""
    user_id: "capo_lex_model_building_service.types.user_id.UserId"
    """<p> The unique identifier for the user that made the utterances. This is the user ID that was sent in the <a href="http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html">PostContent</a> or <a href="http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html">PostText</a> operation request that contained the utterance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUtterancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUtterancesRequest:
    out: DeleteUtterancesRequest = {}  # type: ignore[typeddict-item]
    return out
