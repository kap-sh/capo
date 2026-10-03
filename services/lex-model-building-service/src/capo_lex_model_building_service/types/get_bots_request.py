"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.max_results
    import capo_lex_model_building_service.types.next_token


class GetBotsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request. </p>"""
    max_results: NotRequired[
        "capo_lex_model_building_service.types.max_results.MaxResults"
    ]
    """<p>The maximum number of bots to return in the response that the request will return. The default is 10.</p>"""
    name_contains: NotRequired["capo_lex_model_building_service.types.bot_name.BotName"]
    """<p>Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotsRequest:
    out: GetBotsRequest = {}  # type: ignore[typeddict-item]
    return out
