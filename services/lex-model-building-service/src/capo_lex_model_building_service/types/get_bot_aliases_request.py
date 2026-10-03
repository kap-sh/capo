"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.alias_name
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.max_results
    import capo_lex_model_building_service.types.next_token


class GetBotAliasesRequest(TypedDict, closed=True):
    bot_name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot.</p>"""
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request. </p>"""
    max_results: NotRequired[
        "capo_lex_model_building_service.types.max_results.MaxResults"
    ]
    """<p>The maximum number of aliases to return in the response. The default is 50. . </p>"""
    name_contains: NotRequired[
        "capo_lex_model_building_service.types.alias_name.AliasName"
    ]
    """<p>Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotAliasesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotAliasesRequest:
    out: GetBotAliasesRequest = {}  # type: ignore[typeddict-item]
    return out
